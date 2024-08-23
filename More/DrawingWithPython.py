# coding : utf-8

from turtle import *
from colorsys import *

# Initialiser un objet tortue depuis la classe Turtle du module turtle

turtle = Turtle()

# Configurations relatives à l'écran en soi
turtle.screen.title('Simulation d\'une zone de réseau')
turtle.screen.bgcolor('#171516')

# Configurer la tortue à présent
turtle.hideturtle()
turtle.width(4)
turtle.speed(10)
h = 0.1 		# Variable contenant une valeur qui sera utilisée dans la détermination de la couleur du stylo


n = 360			# Variable contenant la valeur d'initialisation de l'angle du cercle. Cette valeur sera décrémentée chaque fois
				# que la condition un peu plus bas dans la boucle sera évaluée à True

# Si les degrés arrivent à 0, alors on arrête de dessiner
if n==0:
	turtle.penup()
	print('Fin du dessin !')

# Boucle infinie qui dessine sur l'interface
while True:
	# Créer la couleur du stylo et se servant de la valeur initiale contenue dans h
	c = hsv_to_rgb(h,1,1)

	# Mettre la couleur du stylo, celle-ci variera selon l'incrémentation opérée dans la condition un peu plus bas dans le code
	turtle.pencolor(c)

	# Créer un petit point au centre de l'interface d'où partiront les ondes
	turtle.dot(50,hsv_to_rgb(52.5,0.0630,0.9961))

	# Allez ensuite en créant des cercles qui partiront du point central défini ci-dessus
	turtle.circle(100,n,120)

	# Si la tortue revient à son point d'origine
	# changer la direction de la tortue en décrementant l'angle de 30
	# changer la couleur en incrémentat h de 0.3
	if abs(turtle.pos())<1:
		h+=0.3
		m = n-30
		turtle.right(m)


# Créer une boucle infinie qui continue d'afficher l'interface aussi longtemps qu'aucune action extérieure ne l'a interrompue

turtle.screen.mainloop()