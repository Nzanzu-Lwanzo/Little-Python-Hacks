# coding : utf-8

from tkinter import *
import math

# FONCTIONS D'OPERATION

def show_number(number):
	"""A function that displays numbers in the entry field as the user push buttons"""

	# Stocker la valeur courant dans une variable
	current = ent.get()

	# Supprimer chaque fois le champ de saisie pour éviter que les valeurs se répètent
	ent.delete(0,END)

	# La valeur à afficher chaque fois
	all_nums = str(current) + str(number)

	# Insérer la valeur stockée dans la variable current dans le champ de saisie
	ent.insert(0,all_nums)

def clear_all():
	"""A function that clear all that is in the entry field"""
	ent.delete(0,END)

def suppr():
	"""A function that suppress values in the entry field from the end but doesn't delete all"""
	
	# Stocker les éléments entrées dans le champ de saisie dans une variable sous forme de tableau
	values_tab = list(ent.get())
	# Trouver la longeur de la valeur en cours
	value_len = len(ent.get())
	# Supprimer le dernier élément
	ent.delete(value_len-1,END)

def dot():
	"""Function that inserts a dot in a value that's being entered in the entry field"""
	ent.insert(END,".")


def add():
	"""Function that performs addition operations"""
	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "addition"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def substract():
	"""Function that performs substraction operations"""
	
	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "substraction"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def multiply():
	"""Function that performs multiplication operations"""
	
	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "multiplication"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def divide():
	"""Function that performs division operations"""
	
	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "division"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def expon():
	"""Function that performs exponential operations"""

	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "square"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def square():
	"""Function that performs square root operations"""

	global sq,do_this

	# Variable qui sera utilisée par la fonction to_round
	do_this = "square"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)
	# Insérer la racine carrée du nombre entré
	sq = math.sqrt(int_value)
	ent.insert(0,sq)

def modulo():
	"""Function that performs modulo operations"""
	
	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "modulo"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def to_round():
	"""Function thats allow get the round number"""

	# Supprimer tout ce qui est dans le champ de saisie
	ent.delete(0,END)
	# Insérer l'arrondi du résultat
	if do_this=="round_from_to_one":
		ent.insert(0,round(from_to_one,2))
	elif do_this=="square":
		ent.insert(0,f'± {round(sq)}')
	else:
		ent.insert(0,round(result))

def expon_two():
	"""Function that gives the exponential 2 of a given number"""

	# Prendre le nombre entré
	number = ent.get()
	# Supprimer tout ce qui est dans le champ de saisie
	ent.delete(0,END)
	# Insérer l'exposant 2 du nombre donné
	re = int(number)**2
	ent.insert(0,re)

def expon():
	"""Function that arises a number to a given exponential"""

	global int_value,operation

	# Opération censée être effectuée par la fonction
	operation = "exponential"
	# Stocker la valeur entrée dans le champ de saisie dans une variable pour pouvoir l'utiliser
	stored_value = ent.get()
	# Caster la valeur puisqu'elle est reçue comme chaîne de caractères
	int_value = int(stored_value)
	# Supprimer tout ce qui était dans le champ de saisie avant de le stocker dans une variable
	ent.delete(0,END)

def to_one():
	"""Function thats gives the result while dividing 1 by a given number"""

	global do_this,from_to_one

	# Variable qui sera utilisée par la fonction to_round
	do_this = "round_from_to_one"
	# Récupérer la valeur entrée
	var = int(ent.get())
	# Supprimer tout ce qui est dans le champ de saisie
	ent.delete(0,END)
	# Insérer le résultat dans le même champ de saisie
	from_to_one = 1/var
	ent.insert(0,from_to_one)

def equal():
	"""Function that displays the result in the entry field"""

	global result

	# Stocker la valeur courante dans une variable
	current_value = ent.get()
	# Caster la valeur contenue dans la variable current_value puisqu'elle est reçue comme chaîne des caractères
	current_value = int(current_value)
	# Supprimer tout ce qui est dans le champ de saisie pour pouvoir afficher le resultat
	ent.delete(0,END)

	# Afficher différents résultats selon la valeur de la variable globle operation
	result=None
	if operation=="addition":
		result=int_value+current_value
		ent.insert(0,result)
	elif operation=="substraction":
		result=int_value-current_value
		ent.insert(0,result)
	elif operation=="multiplication":
		result=int_value*current_value
		ent.insert(0,result)
	elif operation=="division":
		result=int_value/current_value
		ent.insert(0,result)
	elif operation=="modulo":
		result=int_value%current_value
		ent.insert(0,result)
	elif operation=="exponential":
		result=int_value**current_value
		ent.insert(0,result)



# GUI interface
interface = Tk()



# GUI configuration

interface.title('Calculatrice')
interface.config(background='#2C3539')
interface.resizable(width=False,height=False)



# FRAMES

frm_1 = Frame(
	master=interface,
	background="#2C3539",
	)

frm_1.pack(expand="YES",fill=X,side="top")


frm_2 = Frame(
	master=interface,
	background="#2C3539"
	)
frm_2.pack(expand='YES',fill="both",side='top')



# WIDGETS

lbl_is = Label(
	master=frm_1,
	text="CALCULATOR",
	bg="#2C3539",
	fg="lightgreen",
	font=('Helvetica',20)
	)
lbl_is.pack(pady=20)


lbl_title = Label(
	master=frm_1,
	text="Powered with Python",
	bg="#2C3539",
	fg="orange",
	font=("Helvetica",15)
	)
lbl_title.pack()


ent = Entry(
	master=frm_1,
	fg="#2C3539",
	font=('Helvetica',18),
	)
ent.pack(pady=20)


number_0 = Button(
	master=frm_2,
	text="0",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(0)
)

number_1 = Button(
	master=frm_2,
	text="1",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(1)
)

number_2 = Button(
	master=frm_2,
	text="2",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(2)
)

number_3 = Button(
	master=frm_2,
	text="3",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(3)
)

number_4 = Button(
	master=frm_2,
	text="4",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(4)
)

number_5 = Button(
	master=frm_2,
	text="5",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(5)
)

number_6 = Button(
	master=frm_2,
	text="6",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(6)
)

number_7 = Button(
	master=frm_2,
	text="7",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(7)
)

number_8 = Button(
	master=frm_2,
	text="8",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(8)
)

number_9 = Button(
	master=frm_2,
	text="9",
	width=8,
	height=3,
	background="#FEFCFF",
	foreground="red",
	font=("Helvetica",10),
	command = lambda : show_number(9)
)



number_1.grid(row=1 ,column =0 )
number_2.grid(row=1 ,column =1)
number_3.grid(row=1 ,column =2)

number_4.grid(row=2 ,column =0)
number_5.grid(row=2 ,column =1)
number_6.grid(row=2 ,column =2)

number_7.grid(row=3 ,column =0)
number_8.grid(row=3 ,column =1)
number_9.grid(row=3 ,column =2)

number_0.grid(row=4 ,column =0)


btn_mult = Button(master=frm_2,text="X",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=multiply)
btn_add = Button(master=frm_2,text="+",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=add)
btn_sub = Button(master=frm_2,text="-",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=substract)
btn_div = Button(master=frm_2,text="/",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=divide)


btn_add.grid(row = 1, column = 3 ) 
btn_sub.grid(row = 2, column = 3 ) 
btn_mult.grid(row = 3, column = 3 ) 
btn_div.grid(row = 4, column = 3 ) 


btn_clear = Button(master=frm_2,text="AC",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=clear_all)
btn_eq = Button(master=frm_2,text="=",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=equal)


btn_clear.grid(row=4,column=1)
btn_eq.grid(row=4,column=2)


btn_dot = Button(master=frm_2,text=".",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=dot)
btn_square = Button(master=frm_2,text="Sqr",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=square)
modulo_btn = Button(master=frm_2,text="%",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=modulo)
round_button = Button(master=frm_2,text="Round",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=to_round)


btn_dot.grid(row = 5 , column = 0)
btn_square.grid(row = 5 , column = 1 )
modulo_btn.grid(row = 5, column = 2)
round_button.grid(row = 5, column = 3)


btn_expon_two = Button(master=frm_2,text="X^2",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=expon_two)
btn_exp = Button(master=frm_2,text="X^y",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=expon)
btn_one_on = Button(master=frm_2,text="1/X",width=8,height=3,background="#FEFCFF",foreground="blue",font=('Helvetica',10),command=to_one)
btn_supp = Button(master=frm_2,text="Del",width=8,height=3,background="#FEFCFF",foreground="green",font=('Helvetica',10),command=suppr)


btn_expon_two.grid(row=6,column=0)
btn_exp.grid(row=6,column=1)
btn_one_on.grid(row=6,column=2)
btn_supp.grid(row=6,column=3)

# INFINITE LOOP
interface.mainloop()