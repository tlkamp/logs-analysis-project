# Logs Analysis Project
Gathering insights from a relational database via SQL queries and Python.

## Views
The Python code in [`reports.py`](code/reports.py) makes use of several views within the `news` database. **If the views do not exist at runtime, the program will create them.**

The views created by the program are:

**`datereqs`**

```sql
create view datereqs as
select date(time) as date, count(status) as reqs
group by date;
```

**`dateerrs`**

```sql
create view dateerrs as
select date(time) as date, count(status) as errs
from log
where not status = '200 OK'
group by date;
```

**`okpaths`**

```sql
create view okpaths as
select path from log where status = '200 OK';
```

**`totalviews`**

```sql
create view totalviews as
select path, count(path) from okpaths
group by path;
```

**`authortoarticle`**

```sql
create view authortoarticle as
select authors.name, articles.slug from authors, articles
where authors.id = articles.author;
```

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

To run the code:
1. Copy the [`reports.py`](code/reports.py) file into the `vagrant` directory of the virtual machine.
2. `vagrant up`
3. `vagrant ssh`
4. `cd /vagrant`
5. `python reports.py`