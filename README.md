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

## Running the Python Code
The project has the following structure:

```
project-logs-analysis/
├── README.md
├── code
│   └── reports.py
```

* [`reports.py`](code/reports.py) - the Python code that prints the answers to the questions above.

To run the code:
1. Ensure the [`fullstack-nanodegree-vm` project](https://github.com/udacity/fullstack-nanodegree-vm) project has been 
downloaded.
2. Ensure [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) have been installed.
3. Copy the [`reports.py`](code/reports.py) file into the `vagrant` directory of the [`fullstack-nanodegree-vm` project](https://github.com/udacity/fullstack-nanodegree-vm).
4. `vagrant up`
5. `vagrant ssh`
6. `cd /vagrant`
7. `python reports.py` or just `./reports.py`

## Understanding the Output
The output of the code varies _slightly_, depending on whether or not the views were 
created before the program was run (perhaps by running `psql` commands).

Both versions of the output are included:
  * [Output indicating creation of views](output-1.txt)
  * [Output indicating views already exist](output-2.txt)