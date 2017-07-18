#!/usr/bin/python
import psycopg2


DBNAME = "news"


def get_top_articles():
    # Connect to database and retrieve the top 3 articles by total views

    # Initialize database connection
    db = psycopg2.connect(database=DBNAME)
    # Open cursor for database operations:
    cur = db.cursor()
    # Execute query:
    cur.execute("select title, views from top_articles limit 3;")
    # Return results:
    return cur.fetchall()
    # Close cursor and database connection:
    cur.close()
    db.close()


def get_top_authors():
    # Connect to database and retrieve the top authors by total views

    # Initialize database connection
    db = psycopg2.connect(database=DBNAME)
    # Open cursor for database operations:
    cur = db.cursor()
    # Execute query:
    cur.execute("select name, views from top_authors;")
    # Return results:
    return cur.fetchall()
    # Close cursor and database connection:
    cur.close()
    db.close()


def get_errors():
    # Connect to database and retrieve the dates on which errors exceeded 1%:

    # Initialize database connection
    db = psycopg2.connect(database=DBNAME)
    # Open cursor for database operations:
    cur = db.cursor()
    # Execute query:
    cur.execute("select date, pct from errorpct where pct > 1 order by date;")
    # Return results:
    return cur.fetchall()
    # Close cursor and database connection:
    cur.close()
    db.close()


print ("The three most popular articles of all time are: \n")
for article in get_top_articles():
    print("\"" + article[0] + "\" - " + str(article[1]) + " views")

print("\n")

print ('Authors by page views: \n')
for author in get_top_authors():
    print(author[0] + " - " + str(author[1]) + " views")

print("\n")

print ("Days on which errors exceeded 1%: \n")
for days in get_errors():
    print(days[0] + " - " + str(days[1]) + "% errors")
