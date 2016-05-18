#!/usr/bin/python
import requests
import sqlite3

def get_category(url):
    response1 = requests.post(
        'http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?readkey=PjwkZVJnxWHi&url=' + 'www.url.com')
    print response1.content
    return response1.content


conn = sqlite3.connect('db.sqlite3')
print "Opened database successfully";
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

cursor = conn.execute("SELECT * FROM get_url_website WHERE category=\'\'")
#'body', 'view_count', 'average_view_time', 'category', 'url'
names = list(map(lambda x: x[0], cursor.description))
print names

for row in cursor:
    print row
    print row[4]
    update_command = "UPDATE get_url_website SET (category) VALUES ("+get_category(row[4])+") WHERE url="+str(row[4])
    conn.execute("""UPDATE get_url_website SET category = ? WHERE url= ? """, (get_category(row[4]),row[4]))


conn.commit()
conn.close()