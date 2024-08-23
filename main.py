import tkinter as tk
import time
import random

import pygame

import ulaz
from zmija import Zmija, pravljanjeKvadrata
import os
import sys
from pygame import mixer

def trcanje(zmija):
    prozor.bind("<Left>", zmija.levo)
    prozor.bind("<Right>", zmija.desno)
    prozor.bind("<Up>", zmija.gore)
    prozor.bind("<Down>", zmija.dole)
    prozor.bind("<Escape>", zmija.stani)
    prozor.bind("<Escape>", pauza, add="+")
    hrana = pravljanjeKvadrata(random.choice(xLista[1:-1]), random.choice(yLista[:-1]), platno)
    mixer.init()
    try:
        mixer.music.load("535331_Stay-Inside-Me.mp3")
        mixer.music.set_volume(0.01)
        mixer.music.play(-1)
    except pygame.error:
        pass

    while True:
        bul = zmija.pomeranje(hrana)
        try:
            if bul[0] == True:
                while True:
                    platno.delete(hrana)
                    koordinate = bul[-1]
                    hrana = pravljanjeKvadrata(random.choice(xLista[1:-1]), random.choice(yLista[:-1]), platno)
                    if platno.coords(hrana) not in koordinate:
                        #jedenje = mixer.Sound("maro-jump-sound-effect_1.mp3")
                        #jedenje.play()
                        break
            elif bul[0] == False and zmija.stanje == False:
                break
        except TypeError:
            pass
        prozor.update()
        time.sleep(ulaz.br)
    mixer.music.stop()
    pauza()

def nastavi():
    for element in skupObjekata:
        if isinstance(element, ulaz.Dugme):
            element.frame.place_forget()
            element.dugme.place_forget()
        else:
            element.labela.place_forget()
        del element

    skupObjekata.clear()

def retry():
    global zmija, platno
    zmija.izlaz()
    platno.delete("all")
    zmija = Zmija(platno, xLista, yLista)
    nastavi()
    trcanje(zmija)

def ponovi():
    os.execv(sys.executable, ["python"] + sys.argv)

def izadji():
    global zmija
    zmija.izlaz()
    sys.exit()

def pauza(*args):
    labelPauza = ulaz.Labela(main = prozor, tekst = "Pauza" if zmija.stanje else "Izgubio si", x = 0.5, y = 0.13, font = 60, boja = ulaz.boja)
    labelScore = ulaz.Labela(main = prozor, tekst = "Poeni: " + str(len(zmija.telo) * 100), x = 0.5, y = 0.22, font=40, boja = ulaz.boja)
    dugmeNastavi = ulaz.Dugme(prozor, 0.5, 0.34, 100, 200, "Nastavi", nastavi, ulaz.boja, 25)
    dugmePonovi = ulaz.Dugme(prozor, 0.5, 0.48, 100, 200, "Iz pocetka", retry, ulaz.boja, 25)
    dugmeMeni = ulaz.Dugme(prozor, 0.5, 0.62, 100, 200, "Pocetna", ponovi, ulaz.boja, 25)
    dugmeIzadji = ulaz.Dugme(prozor, 0.5, 0.76, 100, 200, "Izadji", izadji, ulaz.boja, 25)

    skupObjekata.update({dugmeMeni, dugmeNastavi, dugmePonovi, dugmeIzadji, labelPauza, labelScore})

skupObjekata = set()
xLista = [i for i in range(0, 1921, 30)]
yLista = [i for i in range(0, 1081, 30)]

prozor = tk.Tk()

platno = tk.Canvas(master = prozor, height = 1080, width = 1920, bg = "black")
platno.pack()
zmija = Zmija(platno, xLista, yLista)

prozor.attributes("-fullscreen", True)
prozor.after(1, lambda: prozor.focus_force())

trcanje(zmija)

prozor.mainloop()






