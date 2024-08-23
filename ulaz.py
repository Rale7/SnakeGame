import tkinter
import tkinter as tk
from tkinter import colorchooser
from dugme import Dugme, Labela

def promenaBoje():
    global boja
    color = colorchooser.askcolor()
    boja = color[-1]
    dugmeBoja.menjanjeBoje(boja)
    dugmeIgraj.menjanjeBoje(boja)
    skala.config(fg = boja, troughcolo = boja)

def igra():
    global boja, br
    br = brzina.get(skala.get())
    prozor2.destroy()



brzina = {key : 0.25 / key for key in range(1, 11)}
boja = "#00FF7C"
br = brzina.get(5)

prozor2 = tk.Tk()
prozor2.config(bg ="black")
prozor2.geometry("800x750")
prozor2.title("Zmice")

try:
    slika = tk.PhotoImage(False, file = "Slika_Zmije.png")
    prozor2.iconphoto(False, slika)
except tkinter.TclError: pass

dugmeIgraj = Dugme(prozor2, 0.5, 0.3, 100, 200, "Igraj", igra, boja, 40)
dugmeBoja = Dugme(prozor2, 0.5, 0.5, 100, 200, "Boja", promenaBoje, boja, 40)

skala = tk.Scale(master = prozor2, orient ="horizontal", from_ = 1, to = 10, length = 500, font = ("Berlin Sans FB Demi", 40),
                 fg = boja, troughcolo = boja, bg = "black", activebackground = "black", highlightbackground = "black")
skala.set(5)
skala.place(relx = 0.5, rely = 0.66, anchor = "center")

prozor2.mainloop()