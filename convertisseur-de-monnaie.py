from tkinter import *
import requests

echange = Tk()
echange.title("monnaie")
echange.geometry()
echange.resizable(0,0) 
echange.minsize(width=250, height=250)

saisis = Entry(echange, width=18, font=("Times", 12))
saisis.pack()

# echange euro en dollard
def  euro_dollard():
    euros = 0.92
    A = float(saisis.get())
    #A = int(A)

    if A ==float(saisis.get()):
        echange = A/euros
       
        Label(echange, text="$", font=("Times", 12)).pack(padx=5)
    else:
        return None


# echange dollard en euro
def  dollard_euro():
    dollard = 0.92
    A = float(saisis.get())


    if A == float(saisis.get()):
        return A * dollard
        Label(echange, text="€", font=("Times", 12)).grid(padx=5)
    else:
        return None

def number(selected):
    saisis.insert("end",str(selected))

def clear_one():
    val = saisis.get()
    saisis.delete(len(val)-1,"end")

def clear_f():
    saisis.delete(0,"end")


# les boutons
convertir = Button(echange, text="Dollard → Euro", command= (euro_dollard))
convertir.pack()
convertir = Button(echange, text="Euro → Dollard", command= (dollard_euro))
convertir.pack()
clear = Button(echange,text="effacer",command=clear_one)
clear.pack()

euro_dollard()
dollard_euro()
echange.mainloop()
  