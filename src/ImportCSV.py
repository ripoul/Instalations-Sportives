import csv


activite_data = csv.reader(open("data/csv/activite.csv", "r"))
equipements_data = csv.reader(open("data/csv/equipements.csv", "r"))
installations_data = csv.reader(open("data/csv/installations.csv", "r"))

for row in activite_data:
	print("[Activite] - " + row[4] + " | " + row[5] + " | " + row[1])

for row in equipements_data:
	print("[Equipements] - " + row[3] + " | " + row[5] + " | " + row[1])

for row in installations_data:
	print("[Installations] - " + row[1] + " | " + row[0] + " | " + row[2])