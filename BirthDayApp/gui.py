# coding : utf-8

import tkinter
from tkinter import ttk
from operations import Birthday
import time

# DEFINIR LA FONCTION QUI AFFICHERA LES RESULATS
def display_result():
        # Récupérer les résultats entrés
        value_entered = ent_date.get()

        # Vider le champ d'entrée
        ent_date.delete(0,tkinter.END)
        
        # Ensuite créer un objet Birthday
        the_birthday = Birthday(value_entered)

        the_birthday.separate_string()
        the_birthday.cast_values()
        the_birthday.separate_values()
        the_birthday.verify_values()

        # Gérer les cas d'erreur
        if the_birthday.verify_values() == "E-Y":
                result.set('Erreur rencontrée dans les valeurs entrées !')
        elif the_birthday.verify_values() == "E-M":
                result.set('Erreur rencontrée dans les valeurs entrées !')
        elif the_birthday.verify_values() == "E-D":
                result.set('Erreur rencontrée dans les valeurs entrées !')
        else:
                # Ensuite rendre dans le label résultats la valeur obtenue en utilisant la méthode age_years
                result.set(the_birthday.next_birth_left_days())

        # Ensuite afficher le label qui contient les résultats
        lbl_result.pack()





# L'interface graphique
interface = tkinter.Tk()

# STYLE GENERAL
interface.title('BIRTHDAY')
interface.config(background = '#7BCCB5')
interface.geometry('480x360')
interface.resizable(width = False, height = False)

# WIDGET

# 1. LES FRAMES
frm_1 = tkinter.Frame(master = interface, bg = "#7BCCB5")
frm_2 = tkinter.Frame(master = interface, bg = "yellow")
frm_btn = tkinter.Frame(master = frm_1, bg = "#7BCCB5")

# Mettre les frames sur l'écran
frm_1.pack(fill='y',side='top')
frm_2.pack(expand=1,fill='both',side='top')

# 2. LES LABELS
lbl_title = tkinter.Label(
        master = frm_1, 
        text="Bienvenue sur Mon application", 
        bg = "#7BCCB5", 
        fg = "#090A0C", 
        font = ('REM', 16)
        )
lbl_explain = tkinter.Label(
        master=frm_1,
        text="*Entrez votre date de naissance dans le format (yy,mm,dd), \nles valeurs étant séparées par des espaces ou par des traits-d'union\nNous vous dirons le votre âge et le temps qui vous sépare\nde votre prochain anniversaire",
        bg = "#7BCCB5", 
        fg = "#090A0C", 
        font = ('REM', 10)
        )
lbl_me = tkinter.Label(
        master=frm_2, 
        text = "NZANZU MUHAYRWA L.", 
        bg = "yellow", 
        fg = "#090A0C", 
        font = ('REM',8)
        )

   
# Mettre les labels sur l'écran
lbl_title.pack(fill= "x")
lbl_explain.pack(fill = 'x')
lbl_me.place(x = 320, y = 110)


# 3. LE CHAMP DE SAISIE
ent_date = ttk.Entry(
        master = frm_1,
        font = ('REM', 12),
        )

# Mettre le champ de siaisie sur l'écran
ent_date.pack(side='top',pady = 5)

# 4. LES BOUTTONS
btn_age = ttk. Button(
        master=frm_1,
        text = "Age",
        command = display_result
        )

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

# Afficher les bouttons sur l'écran
btn_age.pack(side='top',pady = 5)


# 5. LABEL DES RESULTATS
lbl_r = tkinter.Label(
        master = frm_2,
        text = 'LES RESULTATS APPARAISSENT ICI',
        background = 'yellow',
        fg = "#7BCCB5", 
        font = ('REM', 15)    
        )
lbl_r.pack(side='top',fill='x')

result = tkinter.StringVar()
lbl_result = tkinter.Label( 
        master = frm_2,
        textvariable = result,
        bg = "yellow", 
        fg = "#090A0C", 
        font = ('REM', 16)
        )

# Boucle infinie 
if __name__ == '__main__':
        interface.mainloop()