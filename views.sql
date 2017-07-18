CREATE VIEW top_articles
AS
SELECT count(*) as views, title FROM articles JOIN log ON '/article/' || articles.slug = log.path GROUP BY title ORDER BY views DESC;

CREATE VIEW top_authors
AS
SELECT count(*) as views, name 
FROM authors au
JOIN articles ar ON
au.id = ar.author
JOIN log on '/article/' || ar.slug = log.path
GROUP BY name
ORDER BY views DESC;

CREATE VIEW count_requests
AS
SELECT to_char(date(time), 'Mon DD, YYYY') AS day, count(status) AS totals
FROM log
GROUP BY day;

CREATE VIEW count_errors
AS
SELECT to_char(date(time), 'Mon DD, YYYY') AS day, count(status) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY day;

CREATE VIEW errorpct
AS
SELECT (ce.errors::numeric / cr.totals::numeric * 100)::numeric(7,1) as pct, ce.day
FROM count_errors ce
JOIN count_requests cr ON ce.day = cr.day;