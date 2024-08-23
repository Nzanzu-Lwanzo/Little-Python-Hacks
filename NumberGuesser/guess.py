# coding : utf-8

import random as r 

# Générer la valeur que le joueur devra déviner
to_guess = round(r.random()*10)

# Le nombre total d'essais qu'a l'utilisateur
total_rounds = 10

while total_rounds > 0:
	# Demander à l'utilisateur une valeur
	user_guess = int(input("Dévinez la valeur : "))

	# Decrémenter la valeur total_rounds
	total_rounds-=1

	# Si les deux valeurs sont les mêmes 
	if int(to_guess) == int(user_guess):
		# Il a gagné-On quitte la boucle
		print('Vous avez gagné !')
		break
	# Sinon
	else:
		# Afficher un message - Redémander une valeur
		print('Echec ! Tour ' + str(total_rounds))
		continue