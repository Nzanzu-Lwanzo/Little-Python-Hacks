# coding : utf-8

from tkinter import *
from tkinter import ttk
from random import *
from copy import deepcopy
import pickle
import sqlite3
import jinja2
import pdfkit
from datetime import datetime
import os 


# Set the counter to 0
current_value = 0

# List of all the numbers stored locally
numbers_list = []

# Determine where to store the generated numbers
store_in_txt = True
store_in_db = False
store_in_pdf = False

# Function that counts, incrementing, and says how many numbers we've already generated
def increment():

	global current_value
	# Increment the variable current_value
	current_value+=1

	# Return the generated value stored in the variable current_value
	return current_value

# Function that grabs the current time
def current_time():
	today = datetime.today()
	day = today.day 
	month = today.month
	year = today.year
	hour = today.hour
	minute = today.minute
	seconds = today.second 

	d = f'{day}-{month}-{year}'
	t = f'{hour}:{minute}:{seconds}'

	return d,t 


def generate():

	global counter,entire_number

	# Create a loop that is going to generate the numbers and then put them in the list
	# But also, doing so, display them in the CMD
	# Create a variable that is going to store the initial numbers
	initial = '97'

	# Create a variable that is going to hold the other numbers
	range_n = range(0,9)
	left_numbers_list = choices(range_n,k=7)

	# Create a copy of the generated liste and suppress it
	left_numbers_list_copy = deepcopy(left_numbers_list)
	left_numbers_list.clear()

	# Create a variable in which we're going to store the str values returned by the left_numbers_list
	left_numbers_str = ''

	# Loop the values in the lef_numbers_list_copy
	for value in left_numbers_list_copy:
		left_numbers_str+=str(value)

	# Join the parts to form an entire number
	hyphens_separated_left_part = ''

	# Join the two slice of an entire number
	left_part = f'{initial}{left_numbers_str}'

	# Loop through the left_part the separate them three numbers each time with an hyphens
	l = []								# Create and intermediate list to append elements to entire_number string
	for n in left_part:
		l.append(n)						# Append the content of the l list when it already stores 3 numbers
		if len(l)==3:
			h = '-'
			hyphens_separated_left_part+=f'{h}{"".join(deepcopy(l))}'	# Add a copy of the l list casted to str, adding an hyphens at the begining
			l.clear()				# Clear the l list for it to store new values

	# Form the entire number
	entire_number = f'+243{hyphens_separated_left_part}'

	# Add that number to the liste entire number with all its meta information
	int_number = [
		str(current_value),
		entire_number,
		current_time()[0],
		current_time()[1],
	]

	numbers_list.append(int_number)


	# SPECIFY A FUNCTION THAT LEADS TO WHERE THE NUMBERS ARE MEANT TO BE STORED
	
	store_numbers_in_databse() if store_in_db else None
	write_numbers_in_pdf() if store_in_pdf else None
	write_numbers_in_file() if store_in_txt else None

	# Put the value in the counter variable and then display it on the button
	counter.set(increment())

# Add the generated numbers in a file
def write_numbers_in_file():

	with open('storages/numbers_storage.txt','a') as numbers_file:
		number = f'\n{entire_number}'
		numbers_file.write(number)
	
# Add the generated numbers in a file but turning them into binary data
def write_numbers_in_file_binary():

	with open('storages/numbers_storage.txt','wb') as numbers_file:
		record_in_file = pickle.Pickler(numbers_file)
		record_in_file.dump(f'\n{entire_number}\n')

# Read in the the file
def read_in_numbers_file():

	with open('storages/numbers_storage.txt','r') as numbers_file:
		numbers_list = numbers_file.readlines()

	# Return a list of all the values taken from a database
	return numbers_list

# Store all the numbers generated in a database
def store_numbers_in_databse():
	# Establish a connection with the database
	connection = sqlite3.connect('storages/numbers_database.db')
	# Set a cursor to work with the databse
	cursor = connection.cursor()
	# Create a primary key that is going to increment itself
	number_id = cursor.lastrowid
	# Store the value to lift up in the databse in a variable and its identity
	current_number = (entire_number,)
	# Lift up the number in the database
	cursor.execute('INSERT INTO numbers VALUES (?)',current_number)
	# Commit the addition of a new number everytime
	connection.commit()
	# Close the database
	connection.close()

# A function that is going to clear the database (Don't use yet)
def clear_database():
	# Establish a connection with the database
	connection = sqlite3.connect('storages/numbers_database.db')
	# Set a cursor to work with the databse
	cursor = connection.cursor()
	# Clear all
	cursor.execute("""DELETE FROM numbers""")
	# Commit the addition of a new number everytime
	connection.commit()
	# Close the database
	connection.close()


# Function that is going to write the number in a pdffilr
def write_numbers_in_pdf():

	rep = jinja2.FileSystemLoader('./')
	temp_env = jinja2.Environment(loader=rep)
	template = temp_env.get_template('pdf-generator-utils/temp_num.html')

	context = {
		"numbers":numbers_list,
	}
	output = template.render(context)

	config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
	filename = f'generated-pdfs/CODE{str(id(counter))}GN.pdf'
	pdfkit.from_string(output,filename,configuration=config,css="pdf-generator-utils/style.css")


# Create the GUI on which we are going to have the the button that generates the numbers
interface = Tk()

# General style for the GUI
interface.title('Generate Numbers')
interface.config(background='#090A0C')
interface.geometry('200x200')
interface.resizable(width=False,height=False)

# Create the label that's going to contain the title of the programm
lbl = Message(
	master=interface,
	text="PHONE NUMBERS GENERATOR",
	bg="#090A0C",
	fg="orange",
	font=('Helvetica',12)
	)

# Put the label onto the interface
lbl.pack(expand="YES",fill='both',side='top')

# Create the variable that's going to contain the value to output in the button square
counter = IntVar()

# Create the button that is going to generate the numbers, showing by the way how many numbers will have been generated
gen_btn = ttk.Button(
	master=interface,
	textvariable=counter,
	command= generate
	)

# Put the button onto the interface
gen_btn.pack(expand=1,fill='both')

# Set the infinite loop
interface.mainloop()