# coding : utf-8

import string as st

# Les mots à filtrer, qu'ils soient dans un fichier texte ou une base de données,
# doivent passer par une variable words_to_filter_list qui sera une liste.
# L'idéal c'est que ces mots banis soient stockés dans un fichier .json ou .txt
words_to_filter_list = [
	'putain',',putain,',
	'merde',',merde',
	"border",",bordel",
	"sexe",",sexe"
]

# C'est le pourcentage de rejection d'un énoncé. Si les mots bannis représentent
# plus que ce pourcentage, alors l'énoncé est rejeté.
rejection_rate = 40

# Créer la fonction qui filtrera les messages des utilisateurs
def filter_user_input(user_input):

	global filtred_words,user_words

	# Transformer l'entrée de l'utilisateur en liste de mots
	user_words = user_input.split(' ')
	
	# Variable qui ira en s'incrémentant chaque fois qu'un nouveau mot à filtrer est trouvé
	filtred_words = 0

	# Parcourir la liste de mots à filtrer
	for word_to_filter in words_to_filter_list:

		# Parcourir la liste de mots de l'utilisateur
		for user_word in user_words:

			# Si deux mots correspondent
			if user_word.casefold() == word_to_filter.casefold():

				# Incrémenter la variable filtred_words
				filtred_words+=1

				# On récupère l'index du mot correspondant dans l'entrée de l'utilisateur
				word_index = user_words.index(user_word)

				# Récupérer la longueur du mot
				word_length = len(user_word)

				# On insère une chaîne d'étoiles de la longueur du mot remplacé
				user_words.insert(word_index,'*'*word_length)

				# Ensuite on supprime le mot remplacé qui aura été repoussé au prochain indice
				user_words.pop(word_index+1)

	# Joindre la nouvelle liste en une nouvelle phrase
	new_message = ' '.join(user_words)

	# Retourner la nouvelle phrase
	return new_message

# Fonction qui renvoie false si les mots filtrés constituent plus de 40% des mots du message
def to_post():

	# Stocker la liste de mots de l'utilisateur pris dans la fonction précédente dans une nouvelle variable
	words_to_check = user_words

	# Transformer la liste de mots de l'utilisateur en set
	user_words_set = set(words_to_check)

	# Parcourir les éléments qui sont dans la set
	for element in user_words_set:
		# Si un de ces mots est égal à une ponctuation ou si un il est égal à vide
		if element in st.punctuation or element in st.digits or element.isspace():
			# Supprimer cet élément de la liste de mots de l'utilisateur
			words_to_check.remove(element)

	# Récupérer la longueur de la liste de mots de l'utilisateur
	user_words_length = len(words_to_check)

	# Le nombre de mots filtrés est stocké dans la variable filtred_words de la fonction prédédente
	# laquelle variable nous avons globalisé pour pouvoir l'utiliser ici

	# Calculer le pourcentage,
	# On prendra filtred_words/user_words_length
	# On égalisera par x/100
	# Ensuite produit des moyens est égal au produit des extrêmes
	# On obtiendra 
	# user_words_length*x = filtred_words*100 
	# Pour obtenir le x
	# On divisera le deuxième membre par son coefficient

	percent = round((filtred_words*100)/user_words_length,2)

	# La variable qui stockera la décision prise selon la valeur de percent
	verdict = True if percent<rejection_rate else False

	# Retourner le verdict et le pourcentage pour le test
	return percent,verdict,words_to_check


# ****************** TEST DU PROGRAMMES ****************************

# Prendre l'entrée de l'utilisateur
message = str(input('Entrez votre message ::: '))

# Appeler la fonction de filtrage sur cette entrée et imprimer le message filtrée
print(filter_user_input(message))

# Obtenir les valeurs de retour
# 1. Dans notre alogirthme, on calcule combien de pourcentage les mots bannis représentent dans la phrase entière. Si ce pourcentage est supérieur au taux de rejection (rejection_rate), alors cet énoncé sera considéré inacceptable.
# 2. "verdict" c'est une valeur booléenne qui détermine si oui ou non l'énoncé est acceptable, sur base du taux de rejection.
# 3. Une liste des mots contenus dans l'énoncé

percent,verdict,words_to_check = to_post()

print(f"{percent}% de rejection.")
print(f"Acceptable ? : {'Oui' if verdict else 'Non'}")
print("Les mots analysés sont : ", words_to_check)
