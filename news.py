#!/usr/bin/python
import psycopg2


# name of our database:
DBNAME = "news"
# Init database connection:
db = psycopg2.connect(database=DBNAME)
# Init database cursor
cur = db.cursor()

def get_top_articles():
    # Query database and retrieve the top 3 articles by total views

    # Execute query:
    cur.execute("SELECT title, views FROM top_articles LIMIT 3;")
    # Return results:
    return cur.fetchall()


def get_top_authors():
    # Query database and retrieve the top authors by total views

    # Initialize database connection
    db = psycopg2.connect(database=DBNAME)
    # Execute query:
    cur.execute("select name, views from top_authors;")
    # Return results:
    return cur.fetchall()


def get_errors():
    # Query database and retrieve the dates on which errors exceeded 1%:

    # Execute query:
    cur.execute("select day, pct from errorpct where pct > 1 order by day;")
    # Return results:
    return cur.fetchall()


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

# Close cursor and database connection:
cur.close()
db.close()
