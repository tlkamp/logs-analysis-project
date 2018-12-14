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
|URI, contains slug of articles.   |    |HTTP methods, all are 'GET'        | HTTP response codes       |      |   PK |

## Questions and Answers
1. What are the three most popular articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Running the Python Code
The project has the following structure:

```
project-logs-analysis/
├── README.md
├── code
│   └── reports.py
└── requirements.txt
```

* [`requirements.txt`](requirements.txt) - a file containing the list of all dependencies of my Python application. Can be passed to `pip install` directly to install all necessary dependencies.
* [`reports.py`](code/reports.py) - the Python code that prints the answers to the questions above.