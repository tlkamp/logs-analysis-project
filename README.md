# Logs Analysis Project
Gathering insights from a relational database via SQL queries and Python.

## The Data
The `news` database has the following tables:
* articles
* authors
* log

And those tables have the following structure/relationships:

**Authors**

| name | bio | id |
|------|-----|----|
|      |     | PK |

**Articles**

| author | title | slug | lead | body | time | id |
|--------|-------|------|------|------|------|----|
|F.K. to authors(id)| |unique text, matches path in log|      |      |      |PK|

**Log**

| path | ip | method | status | time | id |
|------|----|--------|--------|------|----|
|URI, contains slug of articles.   |    |HTTP methods        | HTTP response codes       |      |   PK |

## Questions and Answers
1. What are the three most popular articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?