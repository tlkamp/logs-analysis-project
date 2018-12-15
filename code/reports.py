#!/usr/bin/env python2
import psycopg2

DBNAME = 'news'

MOST_POP_3_ART = """
select articles.title, count(articles.title) as views
from articles, log
where log.path like concat('%',articles.slug,'%')
and log.status = '200 OK'
group by articles.title
order by views desc
limit 3;
"""

CALC_PERC = """
select * from (
  select dateerrs.date, CAST(dateerrs.errs as FLOAT)/CAST(datereqs.reqs as FLOAT) * 100 as perct
  from dateerrs join datereqs
  on dateerrs.date = datereqs.date
) as f
where perct >= 1;
"""


def get_days_with_errs():
    print ""
    print "2. Get days with errors greater than 1%"
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(CALC_PERC)
        for date, perc in cursor.fetchall():
            print str(date), '--', '{0:.2f}%'.format(perc)


def get_three_most_pop():
    print ""
    print "1. What are the most popular three articles of all time?"
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(MOST_POP_3_ART)
        for title, views in cursor.fetchall():
            print '"' + title + '"', '--', views, "views"


if __name__ == "__main__":
    get_three_most_pop()
    get_days_with_errs()
