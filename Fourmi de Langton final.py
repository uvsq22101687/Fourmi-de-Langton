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
# Fonction pour faire avancer la fourmi d'un pas
def Next():
    bouger_la_fourmi()
    dessiner_grille()

# lancement de la boucle principale Tkinter
racine.mainloop()