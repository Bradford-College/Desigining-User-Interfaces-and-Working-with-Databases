#!/usr/bin/env /Applications/MAMP/Library/bin/python

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'expensesDB',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(dictionary=True)

cursor.execute('SELECT * FROM `Expenses`')

results = cursor.fetchall()

for row in results:
    id = row['id']
    title = row['name']
    print('%s | %s' % (id, title))

cnx.close()