#!/usr/bin/env python
# -*- coding: UTF-8 -*

"""Similar.py - Find websites similar to site given and build a database containing the data
    by Sotd - twitter.com/#!/Sotd_ """
    
import sys
from lib.parse import results
from lib.db import Db

def similar(url):
    sites = results(url)
    for site in sites:
        print site
    Db(url)
    db = Db()
    db.add(sites, url)

def main():
    """Get results, parse and add to database"""
    sites = results(sys.argv[1])
    for site in sites:
        print site
    Db(sys.argv[1])
    db = Db()
    db.add(sites, sys.argv[1])

def db_data():
    """Return data from a table in the database"""
    db = Db()
    data = db.read_data(sys.argv[2])
    for returned in data:
        print returned

def db_tables():
    """Return tables in database"""
    db = Db()
    tables = db.read_tables()
    for table in tables:
        print table


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Eg: ./similar.py google.com'
        print 'Or: ./similar.py read <site> to read from db'
        print 'Or: ./similar.py read to get existing tables'
        sys.exit(1)
    elif len(sys.argv) == 3 and 'read' in sys.argv[1]:
        db_data()
    elif len(sys.argv) == 2 and sys.argv[1] == 'read':
        db_tables()
    else:
        main()
