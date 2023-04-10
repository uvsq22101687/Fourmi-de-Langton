import tkinter as tk

# Constantes
WIDTH = 500
HEIGHT = 500
TAILLE_CELLULE = 10
ROWS = HEIGHT // TAILLE_CELLULE
COLS = WIDTH // TAILLE_CELLULE
BLACK = "black"
WHITE = "white"

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
   print(previous_steps)
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