# Fourmi-de-Langton
BI TD 4 GROUPE 1
Gladys, Ines, Mariam et Ludivine
Liens du https://github.com/uvsq22101687/Fourmi-de-Langton.git

La Fourmi de Langton est un automate cellulaire composé d'une grille à deux dimensions et d'une fourmi. La grille est composé de cases pouvant être blanches ou noires. Au départ, toutes les cases de la grilles sont blanches. Elle a également la proriété d'une tore: si la foumi sort à gauche, elle réapparaît à droite, si elle sort en haut, elle réapparaît en bas. 
Les deux règles de cet automates sont : 
Si la fourmi est sur une case noire, elle tourne de 90° vers la gauche, change la couleur de la case en blanc et avance d'une case. 
Si la fourmi est sur une case blanche, elle tourne de 90° vers la droite, change la couleur de la case en noir et avance d'une case.

On retrouve sur l'interface 5 boutons : 
- le bouton Play : permet de faire dérouler les étapes tant qu'il est actif
- le bouton Pause : permet de mettre en pause le déroulement des étapes en appuyant dessus une première fois et permet de relancer le déroulement des étapes en appuyant dessus une seconde fois. 
- le bouton Next : permet de passer 1 étape à la fois
- le bouton Cancel : permet de revenir en arrière d'une étape. Pour utiliser ce bouton après le bouton Play, il faut d'abord appuyer sur le bouton pause puis sur le bouton Cancel. 
- le bouton accelerer et ralentir: permet de changer la vitesse de passage des étapes

En appuyant sur la touche 's', vous pouvez enregistrer votre instance sous forme de fichier json à l'endroit souhaité après lui avoir donné un nom.
Pour l'ouvrir il suffit d'appuyer sur la touche 'o', et lorsque que la fenêtre apparait vous pouvez entrer le nom de votre fichier pour l'ouvrir. 
Pour continuer le jeu après l'ouverture de l'instance, il faut appuyer sur Play et le jeu reprendra là où il a été arrêté. 







Sources utilisées :
https://github.com/Moremar/langton_ant/blob/master/langton_ant.py (pour la partie sur les directions que peut prendre la fourmi)
http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html (pour la partie sur la rotation de la fourmi) 
https://www.youtube.com/watch?v=6A2LkRaY2Mc
https://www.youtube.com/watch?v=Tr2Uq_pD6p0
https://vincent.developpez.com/cours-tutoriels/python/tkinter/apprendre-creer-interface-graphique-tkinter-python-3/#LVII-A-6
( pour la partie sur la vitesse de la fourmi)

NB:manque de motivation et de participation de la part d'Inès

