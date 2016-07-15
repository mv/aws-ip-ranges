#
#

import sqlite3
import logging


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
        logging.info('creating db')
        cur.execute(sql)
    except Exception as e:
        logging.error('creating db: [%s]', e )


def insert_range(item):
    sql = '''
        INSERT INTO ranges
            ( region
            , service
            , ip
            )
        VALUES( ?, ?, ?)
    '''
    try:
        tup = (item['region'], item['service'], item['ip_prefix'])
        logging.debug('insert_range: [%s]', item['ip_prefix'])
        cur.execute(sql, tup)
        con.commit()
    except Exception as e:
        logging.error('insert_range: [%s]', e)


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
        logging.info('db closed')
    except Exception as e:
        logging.error('close_db: [%s]', e)

