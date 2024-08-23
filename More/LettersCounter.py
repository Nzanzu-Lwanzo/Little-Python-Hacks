# coding : utf-8

import string


# Afficher le titre du programme
print("""Bienvenue sur notre programme : entrez un texte nous vous diront combien de fois chaque lettre de ce texte est repris""".upper())

# Demander un texte à l'utilisateur d'entrer un texte
texte = str(input('\nEntrez votre texte ::: '.center(10,' ')))

# Créer un décorateur
def decorateur(funct):
	n = '-'*20
	print('\n',n.center(96,' '),'\n',n.center(96,' '))
	return funct

# Créer la fonction qui prendra en argument un mot et renverra un dictionnaire contenant les lettres et leur fréquence de répétition
def count_Letters(text):

	global letters,dict_freq_letter

	# Transformer le mot ou la phrase en liste
	words = text.split(' ')

	# Initialiser le dictionnaire qui contiendra les lettres et leur fréquence
	dict_freq_letter = {}

	# Parcourir la liste des mots
	for word in words:
		# Pour supprimer les espaces
		if word.isspace():
			words.remove(word)

	# Ensuite joindre la nouvelle liste de mots
	new_text = ''.join(words)

	# Transformer la nouvelle liste en une liste de lettres
	letters = list(new_text)

	# Parcourir la nouvelle liste des lettres
	for letter in letters:

		# Ajouter la lettre en clé et le nombre de son occurence en valeur
		dict_freq_letter[letter] = letters.count(letter)

	# Retourner le dictionnaire
	return dict_freq_letter


# Invoquer la fonction
count_Letters(texte)

# Fonction qui viérifie si la fonction ci-dessus a bien fonctionné
def works():
	words_length = len(letters)
	dict_values_sum = 0

	# Parcourir les valeurs des clés du dictionnaire
	for value in dict_freq_letter.values():
		# Additionner ces valeurs
		dict_values_sum+=int(value)

	return words_length == dict_values_sum

@decorateur
# Formater l'affichage sur la ligne de commande
def show():
	# Parcourir les clés du dictionnaire et leurs valeurs
	for n,m in dict_freq_letter.items():
		# Afficher chaque fois la clé suivi de deux points suivi de sa fréquence qui est la valeur
		print(f'{n} est repris {m} fois !'.center(100,' '))

	# Si la fonction works renvoie true, stocker un texte dans une variable message
	debug = "The programm run successfully !" if works() else "An error occurred"

	# Afficher le message
	print(str(debug).center(100,' '))

# EXECUTION DU PROGRAMME

# Afficher les résultats sur l'écran de l'utilisateur dans sa ligne de commande
show()