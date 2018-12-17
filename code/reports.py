#!/usr/bin/env python2
import psycopg2

# View definitions
DATEREQS = """
create view datereqs as
select date(time) as date, count(status) as reqs
group by date;
"""

DATEERRS = """
create view dateerrs as
select date(time) as date, count(status) as errs
from log
where not status = '200 OK'
group by date;
"""

OKPATHS = """
create view okpaths as
select path from log where status = '200 OK';
"""

TOTALVIEWS = """
create view totalviews as
select path, count(path) from okpaths
group by path;
"""

AUTHORTOARTICLE = """
create view authortoarticle as
select authors.name, articles.slug from authors, articles
where authors.id = articles.author;
"""

DB_VIEW_Q = {
    'datereqs': DATEREQS,
    'dateerrs': DATEERRS,
    'okpaths': OKPATHS,
    'totalviews': TOTALVIEWS,
    'authortoarticle': AUTHORTOARTICLE
}

DBNAME = 'news'

# Queries
GET_VIEWS = """
select table_name
from INFORMATION_SCHEMA.views
WHERE table_schema = ANY (current_schemas(false));
"""

MOST_POP_3_ART = """
select articles.title, count(articles.title) as views
from articles, log
where log.path like concat('%',articles.slug,'%')
and log.status = '200 OK'
group by articles.title
order by views desc
limit 3;
"""

RANK_AUTHORS_POP = """
select authortoarticle.name, sum(totalviews.count) as views
from authortoarticle, totalviews
where totalviews.path like concat('%', authortoarticle.slug)
group by authortoarticle.name
order by views desc;
"""

CALC_PERC = """
select * from (
  select dateerrs.date, CAST(dateerrs.errs as FLOAT)/CAST(datereqs.reqs as FLOAT) * 100 as perct
  from dateerrs join datereqs
  on dateerrs.date = datereqs.date
) as f
where perct >= 1;
"""


def do_setup():
    print "Checking for user-created views..."
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(GET_VIEWS)
        existing = [x[0] for x in cursor.fetchall()]
        for view_name in DB_VIEW_Q.keys():
            if view_name not in existing:
                print "\t", view_name, "does not exist, creating it now..."
                cursor.execute(DB_VIEW_Q[view_name])
                cursor.commit()
            else:
                print "\t", view_name, "exists, continuing..."


def rank_authors_popularity():
    print ""
    print "2. Who are the most popular article authors of all time?"
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(RANK_AUTHORS_POP)
        for author_name, total_views in cursor.fetchall():
            print "\t", author_name, '--', total_views


def get_days_with_errs():
    print ""
    print "3. On which days did more than 1% of requests lead to errors?"
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(CALC_PERC)
        for date, perc in cursor.fetchall():
            print "\t", str(date), '--', '{0:.2f}%'.format(perc)


def get_three_most_pop():
    print ""
    print "1. What are the most popular three articles of all time?"
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(MOST_POP_3_ART)
        for title, views in cursor.fetchall():
            print "\t", '"' + title + '"', '--', views, "views"


if __name__ == "__main__":
    do_setup()
    get_three_most_pop()
    rank_authors_popularity()
    get_days_with_errs()
