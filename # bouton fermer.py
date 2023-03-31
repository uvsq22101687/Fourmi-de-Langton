# bouton fermer la fênetre  
import tkinter as tk 
racine = tk.Tk()
bouton_fermer = tk.Button(racine, text= "FERMER", command=racine.quit)
bouton_fermer.pack()
racine.mainloop()