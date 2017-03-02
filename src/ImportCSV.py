#!/usr/bin/python
import csv
import sqlite3
import sys

con = sqlite3.connect('test.db')
cur = con.cursor()

# Create table installation
cur.execute('''CREATE TABLE installation
             (numero INTEGER PRIMARY KEY, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT)''') #latitude real, longitude real

# Insert each row of data from installation.csv
installations_data = csv.reader(open("data/csv/installations.csv", "r"))
for row in installations_data:
	cur.execute("INSERT INTO installation VALUES ("+row[1]+",'"+row[0]+"','"+row[6]+" "+row[7]+"','"+row[4]+"','"+row[2]+"')")

cur.execute("SELECT * FROM installation")
for row in cur:
	print(row)

"""
activite_data = csv.reader(open("data/csv/activite.csv", "r"))
equipements_data = csv.reader(open("data/csv/equipements.csv", "r"))


for row in activite_data:
	print("[Activite] - " + row[4] + " | " + row[5] + " | " + row[1])

for row in equipements_data:
	print("[Equipements] - " + row[3] + " | " + row[5] + " | " + row[1])

for row in installations_data:
	print("[Installations] - " + row[1] + " | " + row[0] + " | " + row[2])
"""

con.commit()

cur.close()
con.close()