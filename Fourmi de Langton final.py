import tkinter as tk
import json
from tkinter import filedialog#importe le module de tkinter

# Constantes
WIDTH = 300
HEIGHT = 300
TAILLE_CELLULE = 10
ROWS = HEIGHT // TAILLE_CELLULE
COLS = WIDTH // TAILLE_CELLULE
BLACK = "black"
WHITE = "white"
Playing = True
DELAY = 500

# Initialisation de la grille
grid = [[WHITE for _ in range(COLS)] for _ in range(ROWS)]

# Position initiale de la fourmi
fourmi_row = ROWS // 2
fourmi_col = COLS // 2
direction = "up"
previous_steps=[]

#Permet le changement de la couleur de la case en fonction de la position de la fourmi
def changement_couleur():
   global couleur, fourmi_row, fourmi_col, direction, previous_steps
   couleur = grid[fourmi_row][fourmi_col]
   #permet de récuperer la position case actuelle (pour annuler)
   previous_steps.append((fourmi_row,fourmi_col,direction,couleur))
   grid[fourmi_row][fourmi_col] = BLACK if couleur == WHITE else WHITE

def rotation_fourmi():
    global direction
    changement_couleur()
    if couleur == WHITE:
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        elif direction == "left":
            direction = "up"
    elif couleur == BLACK:
        if direction == "up":
            direction = "left"
        elif direction == "left":
            direction = "down"
        elif direction == "down":
            direction = "right"
        elif direction == "right":
            direction = "up"

    # Déplacement de la fourmi
def deplacement_fourmi():
    global fourmi_row, fourmi_col
    rotation_fourmi()
    if direction == "up":
        fourmi_row -= 1
    elif direction == "right":
        fourmi_col += 1
    elif direction == "down":
        fourmi_row += 1
    elif direction == "left":
        fourmi_col -= 1

def bouger_la_fourmi():
    global fourmi_row, fourmi_col , previous_steps
    if Playing: 
        deplacement_fourmi()
    #permet à la grille d'avoir la propriété d'un tore
    if fourmi_row >= ROWS:
        fourmi_row = 0
    elif fourmi_row < 0:
        fourmi_row = ROWS-1
    if fourmi_col >= COLS:
        fourmi_col = 0
    elif fourmi_col < 0:
        fourmi_col = COLS-1


# Création de la fenêtre Tkinter
racine = tk.Tk()
racine.title("Fourmi de Langton")
# Création du canvas
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg=WHITE)
canvas.pack()

# Fonction pour dessiner la grille
def dessiner_grille():
   for i in range(ROWS):
       for j in range(COLS):
           couleur = grid[i][j]
           x1 = j * TAILLE_CELLULE
           y1 = i * TAILLE_CELLULE
           x2 = x1 + TAILLE_CELLULE
           y2 = y1 + TAILLE_CELLULE
           canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")

# Fonction pour faire avancer la fourmi d'un pas(soit exécuter 1 étape à la fois)
def Next():
    bouger_la_fourmi()
    dessiner_grille()

# Fonction qui permet à la fourmi de se déplacer que tant que celui-ci est actif
def Play():
    global DELAY
    Next()
    racine.after(DELAY, Play)

# Fontion pour accélérer les étapes 
def accelerer():
    global DELAY
    DELAY = DELAY - 100
    if DELAY<1: # La vitesse ne peut pas être inférieur à 1 donc arriver là la fourmi ne peut aller plus vite
        DELAY =1

# Fonction pour ralentir
def ralentir():
    global DELAY
    DELAY = DELAY + 100

def Pause():
    global Playing
    Playing = not Playing

# Fonction pour revenir en arrière d'une étape
def Cancel():
    global fourmi_row, fourmi_col, direction, previous_steps
    if any(previous_steps):
        row,col,previous_dir,couleur =previous_steps.pop()
        grid[row][col] = couleur
        direction = previous_dir
        fourmi_row = row
        fourmi_col = col
    dessiner_grille()

# Fonction pour enregistrer l'état actuel du jeu dans un fichier JSON
def Sauvegarder(event):
    global donnees_fourmi
    sauvargder_fichier= filedialog.asksaveasfile(initialdir = "/",title = "Sauvegarder partie",defaultextension=".json")
    # Création d'un dictionnaire pour stocker les données de l'instance
    if sauvargder_fichier:
        donnees_fourmi= {
            "grid": grid,
            "fourmi_row": fourmi_row,
            "fourmi_col": fourmi_col,
            "direction": direction,
            }
    with open("jeu.json", "w") as fichier:# Ouverture du fichier en mode écriture
        json.dump(donnees_fourmi, fichier)# Écriture des données au format JSON


# Fonction pour charger l'état du jeu depuis un fichier JSON
def Ouvrir(event):
    global grid, fourmi_row, fourmi_col, direction
    ouvrir_instance= filedialog.askopenfilename(title='ouvrir une instance',filetypes=[("Fichier JSON",".json")])
    # Ouverture du fichier en mode lecture
    if ouvrir_instance:
        with open("jeu.json", "r") as fichier:#Ouverture fichier en mode lecture
            donnees_fourmi = json.load(fichier)# Lecture des données depuis le fichier JSON
    # Récupération des données pour mettre à jour l'instance
        grid = donnees_fourmi["grid"]
        fourmi_row = donnees_fourmi["fourmi_row"]
        fourmi_col = donnees_fourmi["fourmi_col"]
        direction = donnees_fourmi["direction"]
        dessiner_grille()

# Dessin de la grille initiale
dessiner_grille()

# Ajout des boutons
button_next = tk.Button(racine, text="Next", command=Next)
button_next.pack(side=tk.LEFT, padx=5, pady=5)
button_play = tk.Button(racine, text="Play", command=Play)
button_play.pack(side=tk.LEFT, padx=5, pady=5)
button_cancel = tk.Button(racine, text="Cancel", command=Cancel)
button_cancel.pack(side=tk.LEFT, padx=5, pady=5)
button_pause = tk.Button(racine,text ="Pause", command= Pause)
button_pause.pack(side=tk.LEFT, padx= 5, pady=5)
button_accelerer = tk.Button(racine, text="Accelerer", command = accelerer)
button_accelerer.pack(side=tk.LEFT, padx=5, pady = 5)
button_ralentir = tk.Button(racine, text="Ralentir", command = ralentir)
button_ralentir.pack(side=tk.LEFT, padx=5, pady=5)
racine.bind("<KeyPress-s>", Sauvegarder)#permet de sauvegarder en appuyant sur la touche "s" du clavier en minuscule
racine.bind("<KeyPress-o>", Ouvrir)#permet d'ouvrir le fichier en appuyant sur la touche "o" du clavier en minuscule

# lancement de la boucle principale Tkinter
racine.mainloop()
