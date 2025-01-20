

### EQUATION RESOLVER - INTERMEDIAIRE

Le dossier ne contient qu'un seul fichier : [equations.py](EquationResolver/equations.py) qui contient tout l'agorithme. 

Deux classes sont construites dans ce fichier :

_ Une classe *EqFirstDeg* pour les équations du premier degré. Il suffit de construire un object en lui passant trois valeurs (a,b et c). L'équation sera constiuée de cette manière, avec ces valeurs :

    ax + b = c

et d'appeller la méthode *resolution* sur cet objet pour obtenir le résultat.

_ Une classe *EqSecondDeg* pour les équations du second degré. Il suffit de construire un object en lui passant quatre valeurs (a,b, c et d). L'équation sera constiuée de cette manière, avec ces valeurs :

    ax2 + bx + c = d

et d'appeler la méthode *resolution* ou la méthode *float_resolution* pour obtenir le résultat.
