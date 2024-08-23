# coding : utf-8

# SIMULATION D'UNE STRUCTURE SWITCH CASE EN PYTHON ET 
# UTILISATION DES STRUCTURES CONDITIONNELLES TERNAIRES

# Créer des fonctions qui réalise les actions qu'on aurait pu retrouver dans les case
def action1():
	print('Lundi')

def action2():
	print('Mardi')

def action3():
	print('Mercredi')
# Pour notre cas, nous n'allons pas les utiliser. Nous allons directement utiliser des fonctions lambda.
# Cette méthode peut être utilisée lorsque nous avons des plus d'actions à réaliser qu'un simple affichage de jours de la semaine
# ou le retour simple d'une seule valeur.

# Définir un dictionnaire dont les clés sont les cases et les valeurs les actions à exécuter. Dans notre cas, ce sera des fonctions
# fonctions qui seront executées lorsqu'on entre la clé. Ces fonctions afficherons un jour qui correspond à leur clé.

switch = {
	1:lambda : 'Il est Lundi'.upper(),
	2:lambda : 'Il est Mardi'.swapcase(),
	3:lambda : 'Il est Mercredi'.lower(),
	4:lambda : 'Il est Jeudi'.title(),
	5:lambda : 'Il est Vendredi'.center(50,'*'),
	6:lambda : 'Il est Samedi'[7:],
	7:lambda : 'Il est Dimanche'
}

# Demander à l'utilisateur d'entrer un nombre et le convertir en nombre cas les clés de notre dictionnaire sont des integers
choix=int(input('Number ... '))

# Le default on le gère ici puisqu'on ne peut pas le mettre dans le dictionnaire. C'est-à-dire le cas où le nombre entré par l'utilisateur
# ne fait pas partie des cases c'est-à-dire des clés.
def verify():
	return True if 1<=choix<=len(switch.keys()) else False
	# Structure ternaire en Python. Va retourner True si le nombre de l'utilisateur se situe entre 1 et la longeur de la liste des valeurs
	# c'est-à-dire entre 1 et 7. 

	# (-|-)Mais que faire si les clés ne sont pas des entiers mais des valeurs chaîne de caractères ?(-|-)


# Ensuite perform l'action qui devra être executée selon que la fonction verify renvoie True ou False
def tell_day():
	if verify():
		return switch[choix]()
		# La paire de parenthèses est ajoutée à la fin puisque switch[n] va renvoyer une fonction lambda. 
		# Pour appeler cette fonction, il va falloir mettre des parenthèses. 
	else:
		return 'Ce jour n\'existe pas !'

# switch.get(choix,lambda:print("Choix invalide"))() ---> Cette ligne de code peut produire le même résulta que la fonction ci-dessus

# Afficher la valeur correspondant à la clé de l'utilisateur
print(tell_day())

# TOUT FONCTIONNE A MERVEILLE
