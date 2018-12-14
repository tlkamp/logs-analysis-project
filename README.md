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

