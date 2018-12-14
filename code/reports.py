#!/usr/bin/env python
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


def get_three_most_pop():
    print "\n1. What are the most popular three articles of all time?"
    with psycopg2.connect(dbname=DBNAME) as db:
        cursor = db.cursor()
        cursor.execute(MOST_POP_3_ART)
        for title, views in cursor.fetchall():
            print '"' + title + '"', '--', views, "views"


if __name__ == "__main__":
    get_three_most_pop()
