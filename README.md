# About the NewsQuery Project
The included news.py program is a reporting tool to query the data in the "news" database, for the "Logs Analysis Project" from the Udacity Full Stack Nanodegree program.

### Dependencies
[Python](https://www.python.org)

[PostgreSQL](https://www.postgresql.org/)

[Psycopg2](http://initd.org/psycopg/)

### Installation
1. Clone the repository:
```
git clone https://github.com/realomgitsdave/newsquery.git
```
- or -

[download a zip file](https://github.com/realomgitsdave/newsquery/archive/master.zip)


2. Import the database views:
```
psql -d news -f views.sql
```

### Database Views
Query the top articles of all time by number of views:
```
CREATE VIEW top_articles
AS
SELECT count(*) as views, title FROM articles JOIN log ON '/article/' || articles.slug = log.path GROUP BY title ORDER BY views DESC;
```

Query the top authors of all time by number of views:
```
CREATE VIEW top_authors
AS
SELECT count(*) as views, name 
FROM authors au
JOIN articles ar ON
au.id = ar.author
JOIN log on '/article/' || ar.slug = log.path
GROUP BY name
ORDER BY views DESC;
```

Count the total number of HTTP requests by date:
```
CREATE VIEW count_requests
AS
SELECT to_char(date(time), 'Mon DD, YYYY') AS date, count(status) AS totals
FROM log
GROUP BY date;
```

Count the total number of HTTP errors by date:
```
CREATE VIEW count_errors
AS
SELECT to_char(date(time), 'Mon DD, YYYY') AS date, count(status) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY date;
```

Calculate the percentage of HTTP errors/total requests by date:
```
CREATE VIEW errorpct
AS
SELECT (ce.errors::numeric / cr.totals::numeric * 100)::numeric(7,1) as pct, ce.date
FROM count_errors ce
JOIN count_requests cr ON ce.date = cr.date;
```

### Usage
```
python news.py
```

### Output
```
The three most popular articles of all time are: 

"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views


Authors by page views: 

Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views


Days on which errors exceeded 1%: 

Jul 17, 2016 - 2.3% errors
```