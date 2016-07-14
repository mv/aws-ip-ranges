#
#

import sqlite3


con = ''
cur = ''


def create_db():
    con = sqlite3.connect('ranges.sqlite')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ranges
            ( ip        TEXT
            , region    TEXT
            , service   TEXT
            )
    ''')


def load_ranges(ranges):

    list_of_tuples = []
    for item in ranges:
        list_of_tuples.append( (item['ip_prefix'], item['region'], item['service']) )

    cur.execute('''
        INSERT INTO ranges
            ( ip
            , region
            , service
            )
        VALUES( ?, ?, ?)''', list_of_tuples)
    conn.commit


def print_all():

    sql = '''
        SELECT region, service, ip
          FROM ranges
         ORDER BY region, service, ip
    '''
    for row in cur.execute(sql):
        print(row[0], row[1], row[2])


