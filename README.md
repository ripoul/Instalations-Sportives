# Instalations-Sportives
### Import des donnees : 
Les donnees proviennent du site http://data.paysdelaloire.fr. On recupere les csv installation.csv, activité.csv et equipement.csv pour etablire notre base de donné. Nous avons fait le choix d'utiliser sqlite3 comme support pour cette base de donnee. voir : src/BD/importCSV.py
### Reverse Géocoding : 
On utilisise [mapquestAPI](https://developer.mapquest.com/documentation/) pour le reverse geocoding et la creation des differentes carte de l'application. voir : src/BD/ReverseGeocoding(proxy).py
### Serveur : 
La partie serveur est gerer par [bottle](https://bottlepy.org/docs/dev/tutorial.html).
