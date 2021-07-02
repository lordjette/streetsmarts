

import csv
import sqlite3
import sys

db_filename = 'testing.db'
data_filename = 'rice_library.csv'


#INSERT or IGNORE INTO post(title, date_posted, content, user_id)
# VALUES (?, ?, ?, ?)

SQL = """
insert into post(title, date_posted, content, user_id)
values (:Title, :Publication Date, :Summary, '5' )
"""
#":Publication date + '-06-05 11:34:40.714731'"
#2020-06-05 11:34:40.714731

with open(data_filename, 'rt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)