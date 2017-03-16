#!/usr/bin/python
import csv
import sqlite3
import sys

con = sqlite3.connect('test.db')
cur = con.cursor()

# Create table installation
try:
	cur.execute('''CREATE TABLE installation
             (numero INTEGER PRIMARY KEY, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT)''') #latitude real, longitude real
except sqlite3.Error:
	print("		Erreur: CREATE TABLE installation\n")

# Create table activite
try:
	cur.execute('''CREATE TABLE activite
             (numero INTEGER PRIMARY KEY, nom TEXT)''')
except sqlite3.Error:
	print("		Erreur: CREATE TABLE activite\n")

# Create table equipement
try:
	cur.execute('''CREATE TABLE equipement
             (numero INTEGER PRIMARY KEY, nom TEXT, numero_installation INTEGER)''')
except sqlite3.Error:
	print("		Erreur: CREATE TABLE equipement\n")



#Prepare the statment to insert values into the database
sql = ('INSERT INTO installation (numero, nom, adresse, code_postal, ville) VALUES ' '(?, ?, ?, ?, ?)')

# Insert each row of data from installation.csv
installations_data = csv.reader(open("data/csv/installationsMod.csv", "r"))
for row in installations_data:
	cur.execute(sql, (row[1], row[0], row[6]+" "+row[7], row[4], row[2]))

sql = ('INSERT INTO activite (numero, nom) VALUES ' '(?, ?)')
activite_data = csv.reader(open("data/csv/activiteMod.csv", "r"))
for row in activite_data:
	cur.execute(sql, (row[2], row[0], row[6]+" "+row[7], row[4], row[2]))

sql = ('INSERT INTO equipement (numero, nom, adresse) VALUES ' '(?, ?, ?)')
equipement_data = csv.reader(open("data/csv/equipementsMod.csv", "r"))
for row in equipement_data:
	cur.execute(sql, (row[4], row[5], row[2]))





cur.execute("SELECT * FROM installation")
for row in cur:
	print(row)



con.commit()

cur.close()
con.close()




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