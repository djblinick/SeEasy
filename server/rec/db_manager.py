#!/usr/bin/python

import requests
import sqlite3
import xml.etree.ElementTree as ET


def get_category(url):
    response = requests.post(
        'http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?readkey=PjwkZVJnxWHi&url=' + str(url))
    print response.content
    root = ET.fromstring(response.content)
    class_names = []
    for level1 in root:
        atrr = level1.attrib
        tag = level1.tag
        if(level1.tag == "{http://api.uclassify.com/1/ResponseSchema}readCalls"):
            for level2 in level1:
                if(level2.tag == "{http://api.uclassify.com/1/ResponseSchema}classify"):
                    for level3 in level2:
                        for level4 in level3:
                            print level4.attrib
                            class_names.append(level4.attrib)
    print class_names
    newlist = sorted(class_names, key=lambda k: k['p'],reverse=True)
    print newlist
    print newlist[0]['className']
    return newlist[0]['className']


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
    conn.execute("""UPDATE get_url_website SET category = ? WHERE url= ? """, (get_category(row[4]),row[4]))


conn.commit()
conn.close()