# LITTLE PYTHON HACKS
Python est l'un de langages les plus appris et les plus utilisés. Sa versatilité combinée à sa syntaxe lui offrent une place de choix dans n'importe quel domaine de l'IT.

L'une de meilleures façons d'apprendre n'importe quoi (surtout en informatique), c'est de s'exercer. 

Voici donc pour vous quelques petits programmes informatiques qui vous aideront à comprendre le fonctionnement de Python tout en vous amusant. Sentez-vous libres d'améliorer ces programmes et de les réutiliser comme vous voulez. Chaque programme aura un classement **DEBUTANT**, **INTERMEDIAIRE** ou **AVANCE**.

DEBUTANT
-
Les notions basiques de l'algorithmies Python y sont utilisées : variables, fonctions, listes, tuples, ...

INTERMEDIAIRE
-
Des notions un peu plus complexes y sont abordées : la Programmation Orientée Objet, les classes, ...,

AVANCE
-
Ils contiennent des cas d'application de l'algothmie et/ou font intervenir des notions étrangères à l'algorithmie : base de données, librairies extérieures, lecture des fichiers, ...

### BANNED WORDS FILTER - DEBUTANT

C'est un programme qui filtre un texte pour cacher des parties indésirées. Supposez que vous êtes en train de coder une application comme Facebook et que vous ne voulez pas que les utilisateurs écrivent de gros mots dans leurs commentaires ou dans leurs publications.

L'algorithme réside au sein du fichier [message_filter_programm.py](BannedWordsFilter/message_filter_programm.py). 

Au tout début du fichier, vous avez une liste de mots à banir. Ce sont les mots indésirés.  Ajoutez plus de mots à cette liste, si vous voulez. Essayez ensuite d'appeler la fonction *filter_user_input* avec un texte comme argument dans lequel vous incluez certains des mots présents dans la liste. Vous remarquerez que ces mots-là seront filtrés.

Pour améliorer le programme, voici quelques pistes :

_ Stoker les mots à banir dans un fichier .json ou dans un fichier .txt

_ Se servir des expressions régulières pour une recherche intégrale et performante (si vous avez un niveau avancé en Python)

### BIRTHDAY APP - INTERMEDIAIRE

Petite application conçue avec Tkinter qui calcule l'âge d'une personne ou lui dit quand sera son prochain anniversaire. 

L'algorithme réside dans le fichier [operations.py](BirthDayApp/operations.py). Le fichier [gui.py](BirthDayApp/gui.py), lui, contient une interface simpliste conçue avec Tkinter (une librairie Python permettant de concevoir des interface graphiques simples) qui vous aidera à tester l'algorithme.

Pour faire fonctionner cette interface graphique, il suffit d'ouvrir l'invite de commande dans le repertoire et d'exécuter le fichier.

    py gui.py 

Ou alors, si vous utilisez l'éditeur de texte **Sublime Text**, ouvrez le fichier et cliquez sur **Ctrl + B** et l'interface s'affichera.

Le processus de calcul (le fonctionnement de l'algorithme) peut être vu dans le fichier [test.py](BirthDayApp/test.py). 

### EQUATION RESOLVER - INTERMEDIAIRE

Le dossier ne contient qu'un seul fichier : [equations.py](EquationResolver/equations.py) qui contient tout l'agorithme. 

Deux classes sont construites dans ce fichier :

_ Une classe *EqFirstDeg* pour les équations du premier degré. Il suffit de construire un object en lui passant trois valeurs (a,b et c). L'équation sera constiuée de cette manière, avec ces valeurs :

    ax + b = c

et d'appeller la méthode *resolution* sur cet objet pour obtenir le résultat.

_ Une classe *EqSecondDeg* pour les équations du second degré. Il suffit de construire un object en lui passant quatre valeurs (a,b, c et d). L'équation sera constiuée de cette manière, avec ces valeurs :

    ax2 + bx + c = d

et d'appeler la méthode *resolution* ou la méthode *float_resolution* pour obtenir le résultat.

<p style="color:red;font-weight:bold;font-size:1.2rem;">
Attention, cependant : ne vous fiez pas à cet algorithme pour faire vos devoirs d'algèbre. Il a été fait par un amateur d'informatique pas un mathématicien agrégé.
</p>

