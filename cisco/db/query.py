import sqlite3

con = sqlite3.connect('employees.db')
cur = con.cursor()
records = cur.execute('select * from records').fetchall()

for record in records:
    print(f'Record {record[0]}\n\tFirst name: {record[1]}\n\tLast name: {record[2]}\n\tRole: {record[3]}\n')