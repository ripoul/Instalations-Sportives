#!/usr/bin/python
import csv
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

# Create each of the 4 table
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
	print("Erreur lors de la création des tables\n")

#Insert value from csv to db
try:
	#Open the csv we will get data from
	installations_data = csv.reader(open("data/csv/installationsMod.csv", "r"))
	activite_data = csv.reader(open("data/csv/activiteMod.csv", "r"))
	equipement_data = csv.reader(open("data/csv/equipementsMod.csv", "r"))
	activite_data2 = csv.reader(open("data/csv/activiteMod.csv", "r"))

	#Prepare the statment to insert values into the database
	sql = ('INSERT INTO installation (numero, nom, adresse, code_postal, ville, latitude, longitude) VALUES ' '(?, ?, ?, ?, ?, ?, ?)')
	#Insert each row of data from the csv into the db
	for row in installations_data:
		cur.execute(sql, (row[1], row[0], row[6]+" "+row[7], row[4], row[2], 0.0, 0.0))

	#Prepare the statment to insert values into the database
	sql = ('INSERT OR IGNORE INTO activite (numero, nom) VALUES ' '(?, ?)')
	#Statment used to check if the activity is already in the db
	sql2 = ('SELECT * FROM activite WHERE numero IN (?)')
	for row in activite_data:
		#if the id and name of the activity is not set, ignore the row
		if((str(row[4]) != "") & (str(row[5]) != "")):
			cur.execute(sql2, (row[4],))
			#if the statment executed above returned nothing
			if cur.rowcount:
				cur.execute(sql, (row[4], row[5]))

	#Prepare the statment to insert values into the database
	sql = ('INSERT INTO equipement (numero, nom, numero_installation) VALUES ' '(?, ?, ?)')
	#Insert each row of data from the csv into the db
	for row in equipement_data:
		cur.execute(sql, (row[4], row[5], row[2]))

	#Prepare the statment to insert values into the database
	sql = ('INSERT INTO equipement_activite (numero_equipement, numero_activite) VALUES ' '(?, ?)')
	#Insert each row of data from the csv into the db
	for row in activite_data2:
		cur.execute(sql, (row[2], row[4]))

except sqlite3.Error:
	print("Erreur lors des insertions dans les tables\n")


con.commit()

cur.close()
con.close()