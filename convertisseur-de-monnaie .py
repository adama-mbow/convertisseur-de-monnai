from tkinter import *
from tkinter import messagebox
machine = Tk() 
machine.title("Convertisseur de monnaie")
machine.geometry()
machine.resizable(0,0) 
machine.minsize(width=250, height=250)
machine.config(bg="#202630")
my_font = ('Arial', 16, 'bold')


#EN-TÊTE DE LA MACHINE
Mylabel=Label(machine, text="Convertisseur de monnaie", pady=20,fg='orange', bg="#202630", font=my_font)
Mylabel.pack()

#LABEL
Mylabel1=Label(machine, text="Montant à convertir :",fg='white', bg="#202630", font=('Times', 13, 'bold'))
Mylabel1.pack()

#BARRE DE CALCUL
entry1 = Entry(machine, width=18, font=('Times', 12))
entry1.pack()


#FONCTION DU BOUTON1
def euro_to_dollard():
    d = 0.92   # 0.92 dollard
    # 1 euro équivaut à 0.92 dollard
    euro = float(entry1.get())

    if euro == float(entry1.get()):
        resultat1 = euro/d
        Label(machine, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None


#FONCTION DU BOUTON2
def dollard_to_euro():
    d = 0.92
    dollard = float(entry1.get())


    if dollard == float(entry1.get()):
        resultat1 = dollard*d
        Label(machine, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None

def clear_one():
    val = entry1.get()
    entry1.delete(len(val)-1,"end")

def clear_f():
    entry1.delete(0,"end")


#FONCTION DU BOUTON3 historique

#BOUTON QUI PERMET DE CONVERTIR LES EUROS EN DIRHAMS
bouton1 = Button(machine , text = "Euro → dollard", bg = "orange" , fg = "white", height=1, width=15, command=euro_to_dollard)
bouton1.pack()

#BOUTON QUI PERMET DE CONVERTIR LES DIRHAMS EN EUROS
bouton2 = Button(machine , text = "Dollard → Euro", bg = "orange" , fg = "white", height=1, width=15, command=dollard_to_euro)
bouton2.pack()

#bouton effacer
clear = Button(machine,text="effacer",command=clear_one)
clear.pack()

#LABEL "RESULTAT"
Mylabel2=Label(machine, text="Résultat :", font=('Times', 13, 'bold'), pady=10,fg='white', bg="#202630")
Mylabel2.pack()



machine.mainloop()