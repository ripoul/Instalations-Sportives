#!/usr/bin/python
import csv
import sqlite3
import sys

con = sqlite3.connect('test.db')
cur = con.cursor()

# Create table
try:
	cur.execute('''CREATE TABLE installation
             (numero INTEGER PRIMARY KEY, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT,  latitude REAL, longitude REAL)''')
	cur.execute('''CREATE TABLE activite
             (numero INTEGER PRIMARY KEY, nom TEXT)''')
	cur.execute('''CREATE TABLE equipement
             (numero INTEGER PRIMARY KEY, nom TEXT, numero_installation INTEGER)''')
	cur.execute('''CREATE TABLE equipement_activite
             (numero_equipement INTEGER , numero_activite INTEGER)''')
except sqlite3.Error:
	print("		Erreur à la création des tables\n")




#Prepare the statment to insert values into the database
sql = ('INSERT INTO installation (numero, nom, adresse, code_postal, ville) VALUES ' '(?, ?, ?, ?, ?)')

# Insert each row of data from installation.csv
installations_data = csv.reader(open("data/csv/installationsMod.csv", "r"))
for row in installations_data:
	cur.execute(sql, (row[1], row[0], row[6]+" "+row[7], row[4], row[2], 0.0, 0.0))

sql = ('INSERT INTO activite (numero, nom) VALUES ' '(?, ?)')
activite_data = csv.reader(open("data/csv/activiteMod.csv", "r"))
for row in activite_data:
	cur.execute(sql, (row[2], row[0], row[6]+" "+row[7], row[4], row[2]))

sql = ('INSERT INTO equipement (numero, nom, numero_installation) VALUES ' '(?, ?, ?)')
equipement_data = csv.reader(open("data/csv/equipementsMod.csv", "r"))
for row in equipement_data:
	cur.execute(sql, (row[4], row[5], row[2]))

sql = ('INSERT INTO equipement_activite (numero_equipement, numero_activite) VALUES ' '(?, ?)')
for row in activite_data:
	for raw in equipement_data:
		cur.execute(sql, (raw[2], row[0]))




cur.execute("SELECT * FROM installation")
for row in cur:
	print(row)



con.commit()

cur.close()
con.close()




























"""
def importActivities(filename):
	importedActivities = []

	with open(filename, "rt") as csvfile:
		activitiesReader = csv.reader(csvfile, delimiter=',', quote...)
		for row in activitiesReader:
			try:
				activityLine = parseRow(row)
				if activityLine.code not in importedActivities:
					inser



def insertActivity(activity):
	conn= sql3.connect("installations.db")
	c=conn.cursor


def parseRow(row):
	code=int(row[4].strip())
	label = row[5].strip()
	return ActivityLine(code, label)
	"""