import tkinter as tk
from functools import partial
from pygame import mixer

def on_enter(dugme, boja,  *e):
    dugme.config( bg = boja, fg = "black")

def on_leave(dugme, boja, *e):
    dugme.config(bg = "black", fg = boja)

def zvuk():
    mixer.init()
    dugmeZvuk = mixer.Sound("Car_Door_Close-SoundBible.com-1695076524.mp3")
    dugmeZvuk.set_volume(0.1)
    dugmeZvuk.play()

class Dugme:

    def __init__(self, main, x, y, visina, duzina, tekst, komanda, boja, velicinaFonta):
        self.boja = boja
        self.frame = tk.Frame(master = main, bg = self.boja, height = visina, width = duzina)
        self.frame.place(relx = x, rely = y, anchor = "center")
        self.dugme = tk.Button(master = self.frame, bg = "black", fg = self.boja, activebackground = "black", text = tekst,
                               font = ("Berlin Sans FB Demi", velicinaFonta), bd = 0, command = lambda :[zvuk(), komanda()])
        self.dugme.place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.85, anchor = "center")
        self.dugme.bind("<Enter>", partial(on_enter, self.dugme, self.boja))
        self.dugme.bind("<Leave>", partial(on_leave, self.dugme, self.boja))

    def menjanjeBoje(self, novaBoja):
        self.boja = novaBoja
        self.frame.config(bg = self.boja)
        self.dugme.config(fg = self.boja)
        self.dugme.bind("<Enter>", partial(on_enter, self.dugme, self.boja))
        self.dugme.bind("<Leave>", partial(on_leave, self.dugme, self.boja))

class Labela:

    def __init__(self, main,  tekst, x, y, boja, font):
        self.labela = tk.Label(master = main, text = tekst, fg = boja, bg = "black", font = ("Berlin Sans FB Demi", font), anchor = "center")
        self.labela.place(relx = x, rely = y, anchor = "center")

