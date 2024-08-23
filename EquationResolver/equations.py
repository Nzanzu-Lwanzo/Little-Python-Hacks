# coding : utf-8

import math

class EqFirstDeg:
	
	"""Classe qui résout les équations du premier degré"""

	def __init__(self,a=2,b=1,c=0):
		self.a = a
		self.b = b 
		self.c = c

		# Si la valeur avec laquelle on veut vérifier l'équation est différente de 0
		# On la passe dans le premier membre, on additionne son contraire avec le terme indépendant et on la remène à 0
		if self.c!=0:
			self.b += -(self.c)
			self.c = 0



	# Redéfinir la méthode __str__ qui donne l'identité de l'objet instancié
	def __str__(self):

		# Stocker les différentes valeurs dans des variables pour pouvoir contrôler l'affichage des signes
		first_term = self.a
		second_term = self.b
		equal_to = self.c 

		# Spécificier le signe devant précéder le deuxième terme, au moyen d'une petite structure conditionelle
		if second_term>0:
			second_term = f'+{second_term}'

		return f'Equation de forme {first_term}x{second_term}={equal_to}'

	# Propriété qui permet d'accéder à l'identité de l'objet instancié
	@property
	def equation(self):
		return self.__str__()



	# Fonction qui résout l'équation
	def resolve(self):

		# Stocker les valeur avec lesquelles travailler dans des variables
		coeff_x = self.a
		ind_term = self.b

		# Diviser le contraire du terme indépendant par le coefficient du premier terme du premier membre
		# Nous supposons ici que les termes sont ordonnés et que le premier coefficient est celui de la variable plus grande
		result = -ind_term*10/coeff_x

		# Retourner le résultat de l'opération
		return result



	# Fonction qui affiche les résultats à l'utilisateur
	def resolution(self):

		result = f'Le résltat est {self.resolve()}'
		return result



class EqSecondDeg:

	"""Classe représentant et résolvant une équation du second degré"""

	def __init__(self,a=1,b=1,c=1,d=0):
		self.a = int(a)
		self.b = int(b)
		self.c = int(c)
		self.d = int(d)

		# Au cas où on veut vérifier l'équation avec une valeur différente de zéro
		# On la passe dans le premier membre et on additionne son contraire au terme indépendant
		if self.d != 0:
			self.c += -(self.d)
			self.d = 0



	# Redéfinition de la méthode __str__ qui définit l'identité de l'objet
	def __str__(self):

		# Les termes de l'équation dans des variables pour pouvoir contrôler leur affichage selon les signes dont ils sont précédés
		first_term = f'{self.a}x²'
		second_term = f'{self.b}x'
		third_term = f'{self.c}'
		equal_to = f'{self.d}'

		# Gérer le cas où les nombres sont supérieurs à 0 pour afficher les signes + que Python n'affiche pas par défaut
		if self.b>0:
			second_term = f'+{second_term}'
		if self.c>0:
			third_term = f'+{third_term}'

		return f'Equation de forme {first_term}{second_term}{third_term}={equal_to}'



	# Propriété qui permettra d'accéder à l'identité de l'objet
	@property
	def equation(self):
		return self.__str__()



	# Calcul de delta : delta est égal à b²-4ac
	def delta(self):

		# Calculer delta
		dlt = (self.b**2) - 4*(self.a)*(self.c)

		# Conditions pour savoir ce qui sera rendu
		# Cas 1 : si delta est supérieur à 0, on le rend
		# Cas 2 : si delta est égal à 0, on rend 1
		# cas 3 : si delta est inférieur à 0, on ne renvoie rien
		if dlt>0:
			return dlt
		elif dlt==0:
			dlt = math.floor(dlt)
			return 0
		elif dlt<0:
			return -1



	# Calculer la racine carrée de delta
	def deltaRoot(self):

		# Si le retour de la fonction delta() a été inférieur à 0, on renvoie un message à l'utilisateur
		if self.delta()<0:
			return 'Impossible de calculer la racine carré de delta puisqu\'il est inférieur à 0'

		# Sinon, calculer la racine carré de la valeur renvoyée par la fonction delta()
		dlt_sqrt = round(math.sqrt(self.delta()))
		return dlt_sqrt



	# Résoudre l'équation du second degré 
	def resolve(self):

		# Résoudre l'équation dans le cas où le retour de la fonction delta() a été supérieur à 0
		if self.delta()>0:
			
			# Démembrer opérations en stockant les différentes parties dans des variables pour pouvoir gérer le cas où on a des fractions
			# et qu'on veut les afficher en entier.

			# Stocker la valeur de -b + rc delta dans une variable qui constituera le numérateur de l'opération conduisant à x1
			# Stocker la valeur de -b - rc delta dans une variable qui constituera le numérateur de l'opération conduisant à x2
			# Stocker leur dénominateur commun qui est 2a dans une variable également.
			x1_num = -self.b + self.deltaRoot()
			x2_num = -self.b - self.deltaRoot()
			denom = 2*self.a

			# Calculer la valeur de x1 et de x2 en utilisant spécifiquement les variables spécifiées ci-dessus et leur associées
			# en les divisant par le dénominateur et en les arrondissant.
			x1 = round(x1_num / denom)
			x2 = round(x2_num / denom)

			# Gérer le cas où on a des fractions et qu'au lieu d'afficher des nombres décimaux, on veut renvoyer une fraction
			# Alors, on a généralement des décimaux lorsque les numérateurs sont inférieurs aux dénominateurs.
			# C'est sur base de ce constat que nous allons nous baser. 
			# Mais il faudra également que nous gérions  le cas où les décimaux sont produits par des fractions pour lesquelles
			# C'est le dénominateur qui est inférieur au dénominateur


			if x1_num < denom and x1==float(x1) or x1_num>denom and x1==float(x1):
				# Calculer les pgcd des deux membres de la fraction 
				gcd_1 = round(math.gcd(x1_num,denom))
				# Divise le numérateur et le dénominateur par le pgcd
				x1_num /= gcd_1
				denom /= gcd_1


				x1 = f'{round(x1_num)}/{round(denom)}'
			elif x2_num < denom and x2==float(x2) or x2_num>denom and x2==float(x2):
				# Calculer les pgcd des deux membres de la fraction 
				gcd_2 = round(math.gcd(x2_num,denom))
				# Divise le numérateur et le dénominateur par le pgcd
				x2_num /= gcd_2
				denom /= gcd_2

				# Retourner les résultats obtenus mais sous forme de chaîne de caractère
				x2 = f'{round(x2_num)}/{round(denom)}'

			return x1,x2

		# Résoudre l'équation dans le cas où delta a été égal à 0 c'est-à-dire la fonction delta() retourne 1
		elif self.delta()==0:
			x_num = -(self.b)
			denom = 2*self.a
			x = round(x_num // denom)

			if x_num>denom and x==float(x) or x_num<denom and x==float(x):

				# Calculer les pgcd des deux membres de la fraction 
				gcd = round(math.gcd(x_num,denom))
				# Divise le numérateur et le dénominateur par le pgcd
				x_num /= gcd
				denom /= gcd

				# Retourner le résultat formaté en chaîne de caractères
				x = f'{round(x_num)}/{round(denom)}'

			return x

		# Résoudre l'équation dans le cas où delta a été inférieur à 0. On renvoie un simple message.
		if self.delta()<0:
			return 'Lorsque delta (b²-4ac) donne 0, il n\'existe aucune résolution réelle !'



	# Afficher alors les différents résultats, selon les cas produits par la fonction construite
	def resolution(self):
		if self.delta()>0:
			x1,x2 = self.resolve()
			result = f'X1 sera {x1} et X2 sera {x2}'

		elif self.delta()==0:
			x = self.resolve()
			result = f'X aura la valeur {x}'

		elif self.delta()<0:
			result = 'Equation irresolvable !'

		return result



	# Fonction qui prend les valeurs que nous avons mises en string pour pouvoir afficher des fractions 
	# et les retourne en valeurs rendant des décimaux en bruts, permettant d'effectuer des calculs avec ses résultats
	def float_resolve(self):

		if self.delta()>0:
			# Prendre les variables x1_num, x2_num et denom
			x1_num = -self.b + self.deltaRoot()
			x2_num = -self.b - self.deltaRoot()
			denom = 2*self.a

			# Pour refaire de nouveaux résultats
			x1 = x1_num/denom
			x2 = x2_num/denom

			return x1,x2
		elif self.delta()==0:
			x_num = -(self.b)
			denom = 2*self.a
			x = x_num // denom

			return x
		elif self.delta()<0:

			return 'Lorsque delta (b²-4ac) donne 0, il n\'existe aucune résolution réelle !'



	# Fonction qui affiche les résultats rendus en brut c'est-à-dire avec les décimaux, ignorant les fractions qu'on est obligé de caster
	# en string, rendant ainsi impossible d'effectuer des calculs avec eux.
	def float_resolution(self):

		if self.delta()>0:
			x1,x2 = self.float_resolve()
			# Afficher ces résultats à l'utilisateur
			result = f'X1 sera {x1} et X2 sera {x2}'

		elif self.delta()==0:
			x = self.float_resolve()
			result = f'X aura la valeur {x}'

		elif self.delta()<0:
			result = 'Equation irresolvable !'

		return result



	# Méthode temporaire seulement pour mon déboggage
	def debug(self):
		pass