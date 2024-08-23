# coding : utf-8

import sqlite3

# Etablir une connexion avec la base de données
connexion = sqlite3.connect('storages/numbers_database.db')

# Créer un curseur qui exécutera nos requêtes
cursor = connexion.cursor()

# Ecrire les requêtes ici

numbers_ = cursor.execute('SELECT COUNT(*) FROM numbers')

for number in numbers_:
	print(number)

connexion.commit()

# Fermer la connexion avec la base de données
connexion.close()