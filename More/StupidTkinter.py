# coding : utf-8

from tkinter import *
from tkinter import messagebox
from time import *


# Create the interface window
interface = Tk()

# General configurations
interface.title('Stupid Person')
interface.geometry('720x480')
interface.resizable(width=False,height=False)

# Change the interface background color automatically after an interval of time
colors = ['#0C090A','#2C3539','#463E3F','#EDDC74','#F433FF']
interface.config(background='#AAA955')

# The message to display when one gets out of the loop
lbl = Label(master=interface,text="Vous êtes stupide comme cet algorithme !",bg="#AAA955",fg="#0C090A",font=('Helvetica',20))

# Create the message box that asks the question
says_intelligent = True
while says_intelligent:
	is_stupid = messagebox.askyesno('Etes-vous intelligent ?')

	if is_stupid==True:
		continue
	else:
		lbl.pack(expand=1,fill='both')
		break
		


# Set the infinite loop
interface.mainloop()