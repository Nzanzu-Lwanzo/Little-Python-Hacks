# coding : utf-8

import copy


# Créer le dictionnaire qui contient les noms des étudiants et leurs notes
students = {
	'John':12,
	'André':20,
	'Joel':20,
	'Julia':1,
	'Josiane':12,
	'Christopher':12,
	'Samantha':15,
	'Kali':1,
	'Booba':13
}

# Fonction 1 : prendre les étudiants et leurs notes 
def logData(*new_data):

	# Parcourir la liste de données entrées par l'utilisateur
	for data in new_data:
		# Caster chaque donnée en liste pour être sûr d'avoir bien des listes
		data = list(data)
		# La première donnée de la liste sera la clé et la deuxième sera la valeur
		students[data[0]] = data[1]

	# Retourner le dictionnaire entier
	return students

logData(['Anna',2],['Johana',4],['Sandy',18])

# Créer le dictionnaire qui contiendra les notes des étudiants en clé et leurs noms sous forme de liste en valeur
evaluation = {}

# Initialiser une liste qui va contenir chacune les noms des étudiants
# et un ensemble qui va contenir les notes des étudiants pour éviter les doublons
the_students = []
the_grades = set()

# Parcourir le dictionnaire de la classe
for student,grade in students.items():
	# Ajouter les noms des étudiants à la liste des noms
	the_students.append(student)
	# Ajouter les notes des étudiants à l'ensemble des notes
	the_grades.add(grade)
	
# Retransformer l'ensemble des notes en liste ordonnée
the_grades = sorted(list(the_grades))

# Liste qui fera monter la liste des noms par note dans le dictionnaire
current = []

# Parcourir les notes des étudiants (de la liste ci-dessus)
for grade in the_grades:
	# Parcourir également les noms des étudiants (dans le dictionnaire)
	for student in students.keys():			
		# Si les étudiants ont la même note 
		if grade == students[student]:
			# Ajouter le nom de l'étudiant à une liste
			current.append(student)

			# Copier la liste comme valeur associé à une note dans le dictionnaire
			evaluation[grade] = copy.deepcopy(current)

	# Puisqu'on a fini de parcourir les noms avec une note quelconque
	# et que les noms correspondant à cette note on déjà été stockés dans la variable intermédiaire current
	# on peut alors vider cette dernière (une liste) afin que, lorsqu'on parcourt les noms avec la prochaine note,
	# celle-ci soit prête à recevoir les autres noms.
	# Faire attention à l'indentation (on vide la liste current une indendation après le parcourt de la liste de notes
	# parce que vider current dépend de ce qu'on a fini de parcourir les noms des étudiants avec chaque note)
	current.clear()

# AFFICHER SUR L'ECRAN

for key,value in evaluation.items():
	if len(value) == 1:
		print(f"Un seul étudiant a eu {key} et c'est {' ,'.join(value)}")
	else:
		print(f"Les étudiants qui ont eu {key} sont au nombre de {len(value)} et sont {' ,'.join(value)}")

