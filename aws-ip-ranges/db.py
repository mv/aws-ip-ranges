#
#

import sqlite3


con = ''
cur = ''

con = sqlite3.connect('ranges.sqlite')
cur = con.cursor()

def create_db():
    sql = '''
        CREATE TABLE IF NOT EXISTS ranges
            ( region    TEXT
            , service   TEXT
            , ip        TEXT
            )
    '''
    try:
        cur.execute(sql)
    except Exception as e:
        print('Error: create_db:', e)


def insert_range(tup):
    sql = '''
        INSERT INTO ranges
            ( region
            , service
            , ip
            )
        VALUES( ?, ?, ?)
    '''
    try:
        cur.execute(sql, tup)
        con.commit()
    except Exception as e:
        print('Error: insert_range:', e)
        raise e



def print_all():
    sql = '''
        SELECT region, service, ip
          FROM ranges
         ORDER BY region, service, ip
    '''
    for row in cur.execute(sql):
        print(row[0], row[1], row[2])


def close_db():
    try:
        con.close()
    except Exception as e:
        print('Error: close_db', e)

