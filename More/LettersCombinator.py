# coding : utf-8

# Créer le tableau des premières lettres de la combinaison et initialiser leur longueur
first_letters = ['a','b','c']
f_length = len(first_letters)

# Créer le tableau des deuxièmes lettres de la combinaison et initialiser leur longueur
second_letters = ['d' ,'e']
s_length = len(second_letters)

combinations = []

# Créer une chaîne de caractère vide qui aidera à faire monter les combinaisons dans la liste
# ['ad', 'ae', 'bd', 'be','cd', 'ce']
combination = ''

# Parcourir la première liste
for n in first_letters:
	# Parcourir la deuxième liste
	for m in second_letters:
		
		# Joindre ces deux lettres en une chaîne de caractères
		combination = f'{n}{m}'

		# Faire monter chaque fois la nouvelle combinaison dans la liste combinations
		combinations.append(combination)

# Afficher la liste des combinaisons
print(combinations)

