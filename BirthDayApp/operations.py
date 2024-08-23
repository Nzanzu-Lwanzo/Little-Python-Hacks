# coding : utf-8

from datetime import date
import calendar

"""	PROGRAMME QUI CALCULE  LE NOMBRE DE JOURS QUI RESTENT AVANT LE PROCHAIN ANNIVERSAIRE DE QUELQU'UN
	  ET LUI DIT L'AGE QU'IL AURA	  """

# Implémenter une classe qui effectuera les opérations et rendra les résultats : pourra être utilisée dans une autre fichier
class Birthday:
	"""Classe qui effectue des opérations de calcul sur l'âge entré et le temps qui reste jusqu'au prochain anniversaire"""
	def __init__(self,given_date):
		self.given_date = given_date
		self.birth_values = []
		self.year = 0
		self.month = 0
		self.day = 0

	# METHODE QUI TRANSFORME LA DATE DONNEE EN UN ENSEMBLE DE TROIS VALEURS 
	def separate_string(self):
		# Si un trait d'union est trouvé dans la valeur donnée
		if '-' in self.given_date:
			# Transformer la valeur reçue en une liste de trois valeurs en utilisant ce trait d'union comme séparateur
			self.birth_values = self.given_date.split('-')
		# Sinon
		else:
			# Transformer la valeur reçue en une liste de trois valeurs en utilisant les espaces
			self.birth_values = self.given_date.split(sep=None)

	# METHODE QUI CASTE LES VALEURS CONTENUES DANS LA VARIABLE birth_values EN ENTIERS
	def cast_values(self):
		# Liste intermédiaire qui contiendra les valeurs en entier
		integer_values = []
		# Parcourir les données de la liste
		for value in self.birth_values:
			# Caster chaque valeur
			int_value = int(value)
			# Ensuite ajouter ces valeurs à la liste des valeurs en entier
			integer_values.append(int_value)
		
		# Vider la liste initiale qui contenait les valeurs en string
		self.birth_values.clear()
		# Faire fusionner cette liste vide avec la nouvelle liste de valeurs en entier
		self.birth_values.extend(integer_values)

	# METHODE QUI SEPARE LES VALEURS EN TROIS VALEURS DISTINCTES
	def separate_values(self):
		# Donner à chaque variable une valeur correspondante
		_year = self.birth_values[0]
		_month = self.birth_values[1]
		_day = self.birth_values[2]

		return _year,_month,_day

	# METHODE QUI VERIFIER QUE CES VALEURS SONT UTILISABLES
	def verify_values(self):
		
		global current_year
		
		# Stocker les valeurs rendues par la méthode de spérataion dans des variables
		_year = self.separate_values()[0]
		_month = self.separate_values()[1]
		_day = self.separate_values()[2]

		# 1. Vérifier que l'année n'est pas supérieur à l'année courante
		# récupérer l'année courante
		current_year = date.today().year
		try:
			assert 0 < _year < current_year
		except AssertionError:
			self.year = 0
			return 'E-Y'
		# Si la valeur remplit la condition de l'assertion, on l'attribue à l'attribut self.year
		else:
			self.year = _year
			
		# 2. Vérifier que le mois est bien entre 1 et 12
		try:
			assert 1 <= _month <= 12
		except AssertionError:
			self.month = 0
			return 'E-M'
		# Si la valeur remplit la condition de l'assertion, on l'attribue à l'attribut self.month
		else:
			self.month = _month

		# 3. Vérifier que le jour est bien entre 1 et 31
		try:
			assert 1 <= _day <=31
		except AssertionError:
			self.day = 0
			return 'E-D'
		# Si la valeur remplit la condition de l'assertion, on l'attribue à l'attribut self.day
		else:
			self.day = _day


	# METHODE QUI EFFECTUE LES CALCULS DE L'AGE SEULEMENT SELON L'ANNEE
	def age_years(self):
		# Prendre l'année courante moins l'année de naissance entrée
		born_year = current_year - self.year
		return born_year
	
	# METHODE QUI EFFECTUE LES CALCULS D'AGE EN TERME DE MOIS
	def  age_months(self):
		# Convertir le nombre d'années en mois
		born_month = self.age_years() * 12
		return born_month
	
	# METHODE QUI EFFECTUE LES CALCULS D'AGE EN TERME DE JOURS
	def age_days(self):
		# Convertir le nombre d'années en jours
		born_day = self.age_years() * 365

		# Calculer le nombre de jours bissextiles qui écoulées entre l'année de naissance donnée et l'année courante
		leap_days = calendar.leapdays(self.year,current_year)

		# Additionner ces jours au born_day
		born_day+=leap_days

		return born_day
	
	# METHODE QUI EFFECTUE LES CALCULS D'AGE MAIS EN TERME DE D'HEURES
	def age_hours(self):
		# Convertir le nombre de jours en heures
		born_hour = self.age_days() * 24
		return born_hour

	# METHODE QUI EFFECTUE LES CALCUS D'AGE MAIS EN TERME DE MINUTES
	def age_minute(self):
		# Converir le nombre d'heures en minutes
		born_minute = self.age_hours() * 60
		return born_minute

	# METHODE QUI DE DONNE LE NOMBRE DE JOURS ECOULES ENTRE LE JOUR COURANT ET LE PROCHAIN ANNIVERSAIRE
	def convert_dates_days(self):

		# Variable qui va stocker le nombre de jours convertis
		converted_days = 0

		# Donner à chaque mois de l'année le nombre de jours qu'il compte
		month_days = {
			'january' : 31,
			'february' : 28 ,
			'march' : 31,
			'april' : 30,
			'may' : 31,
			'june' : 30,
			'july' : 31,
			'august' : 31,
			'september' : 30,
			'october' : 31,
			'november' : 30,
			'december' : 31,
		}

		# Si l'année suivant l'année courante est bissextile
		n_y = current_year + 1
		if calendar.isleap(n_y) and date.today().month > 2 :
			# Alors fevrier aura 29 jours
			month_days['february'] = 29
		# Si  l'année suivant l'année prochaine est bissextile, que la personne est née en fevrier et le mois courant est fevrier
		if calendar.isleap(n_y) and self.month == 2 and date.today().month == 2:
			# Alors ce mois-ci garde son nombre de jours mais celui de l'année prochaine en prend 1 de plus
			# 28.5 cette année, 28.5 l'année prochaine donne le 1 jour de plus.
			month_days['february'] = 28.5

		# Stocker les mois dans une liste
		months_list = [n for n in month_days.keys()]

		# Stocker les jours des mois dans une liste
		days_list = [n for n in month_days.values()]

		# Récupérer le nom du mois courant
		from_month = months_list[date.today().month-1]

		# Récupérer le nombre de jours qui restent dans le mois courant
		left_days_this_month = month_days[from_month] - date.today().day

		# Calculer la somme des jours qui restent au mois courant et
		# des jours qui iront jusqu'au jour entrée dans la fonction
		# dans le mois donné dans la fonction
		# pour l'année prochaine
		converted_days = left_days_this_month + self.day 

		# Récupérer l'intervalle de mois situés entre le même mois cette année et l'année prochaine
		# d'abord les mois qui restent dans cette année
		# pour cela, il faut qu'on commence au mois prochain
		m = date.today().month + 1
		fork = days_list[m:]
		# ensuite les mois jusqu'au même mois l'année prochaine
		n = self.month -1
		fork_2 = days_list[:n]

		# Joindre les deux intervalles en une seule liste
		fork.extend(fork_2)
		
		# (|) Si le mois donné est supérieur au mois courant mais dans la même année
		if date.today().month < self.month <= 12:
			# Alors la fork qu'on prendra c'est seulement la première
			fork = days_list[m:self.month-1]			
		
		# Si le mois de l'anniversaire est juste celui qui vient après le mois courant
		if self.month == (date.today().month+1):
			# Alors on ne travaille qu'avec les jours
			return left_days_this_month + self.day 

		# Parcourir l'intervalle obtenue
		for days in fork:
			# Ajouter les jours des mois à la variable converted_days
			converted_days += days

		# Ensuite retourner la somme de tous les jours 	
		return converted_days

	# METHODE QUI DETERMINE LE NOMBRE DE JOURS QUI RESTENT JUSQU'AU PROCHAIN ANNIVERSAIRE
	def next_birth_left_days(self):
		next_b_d = 0

		# Si le mois de l'anniversaire est le même que le mois courant
		if self.month == date.today().month:
			# Si le jour de l'anniversaire est supérieur au jour en cours
			if self.day > date.today().day:
				# Alors on n'effectue qu'une simple soustraction pour obtenir les jours qui restent
				next_b_d = self.day - date.today().day
			# Si le jour de l'anniversaire est inférieur au jour en cours
			elif self.day < date.today().day:
				# Alors les jours qui séparent la date courante de la même date l'année prochaine est le nombre de jours qui restent
				next_b_d = self.convert_dates_days()
			# Si le jour de l'anniversaire est le même que le jour en cours
			elif self.day == date.today().day:
				# Alors on souhaite joyeux anniversaire
				return f"C'est aujourd'hui ! Joyeux anniversaire !\nVous venez d'avoir {self.age_years()}"

		# Si le mois de l'anniversaire est supérieur au mois courant ou inférieur au mois courant
		if self.month > date.today().month or self.month < date.today().month:
			# Alors, on ne fait appel qu'aux opérations de la méthode précédente
			next_b_d = self.convert_dates_days()

		# Retourner les jours qui séparent du prochain anniversaire
		return f'Il reste {next_b_d} jours avant le prochain anniversaire !'


	# METHODE QUI DETERMINE LE NOMBRE DE MOIS QUI RESTENT JUSQU'AU PROCHAIN ANNIVERSAIRE
	def next_birth_left_months(self):
		next_b_m = 0
		# Si le mois de l'anniversaire est supérieur au mois courant
		if self.month > date.today().month:
			# On effectue une simple soustraction
			next_b_m = self.month - date.today().month
		# Si le mois de l'anniversaire est inférieur au mois courant --> c'est que l'anniversaire sera dans l'année prochaine
		if self.month < date.today().month:
			# On obtient le nombre de mois restants sur l'année en cours
			left_month = 12 - date.today().month
			# Ensuite on lui ajoute le nombre du mois de l'anniversaire donné 
			next_b_m = left_month + self.month

		# Retourner le nombre de mois qui restent jusqu'au prochain anniversaire
		return f'Vous avez {next_b_m} mois !'	

	# PROPRIETE QUI LANCE LES OPERATIONS DES METHODES DE TRAITEMENT DES VALEURS
	# AU LIEU QU'ON AIT A LE FAIRE DANS LE FICHIER OU ON UTILISERA LA CLASSE
	@property
	def launch_operations(self) -> True:
		self.separate_string()
		self.cast_values()
		self.separate_values()
		self.verify_values()
