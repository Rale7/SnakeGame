import random
from ulaz import boja

class Zmija:

    def __init__(self, platno, xLista, yLista):
        self.xLista = xLista
        self.yLista = yLista
        self.platno = platno
        self.xKoordinata = random.choice(xLista[2:-2])
        self.yKoordinata = random.choice(yLista[2:-2])
        self.telo = [pravljanjeKvadrata(self.xKoordinata, self.yKoordinata, self.platno),
                     pravljanjeKvadrata(self.xKoordinata - 30, self.yKoordinata, self.platno),
                     pravljanjeKvadrata(self.xKoordinata - 60, self.yKoordinata, self.platno)]
        self.xPomeraj = 0
        self.yPomeraj = 0
        self.stanje = True

    def pomeranje(self, hrana):
        if self.stanje:
            if not(self.xPomeraj == 0 and self.yPomeraj == 0):
                koordinate = [self.platno.coords(self.telo[0])]
                self.platno.move(self.telo[0], self.xPomeraj, self.yPomeraj)

                if koordinate[0][0] < 0 or koordinate[0][1] < 0 or koordinate[0][2] > 1920 or koordinate[0][3] > 1080:
                    self.stanje = False
                    return False, koordinate

                for i in range(1, len(self.telo)):
                    koordinate.append(self.platno.coords(self.telo[i]))
                    self.platno.coords(self.telo[i], koordinate[i - 1])

                if koordinate[0] in koordinate[3:]:
                    self.stanje = False
                    return False, koordinate

                if self.platno.coords(hrana) == koordinate[0]:
                    self.telo.append(pravljanjeKvadrata(koordinate[-1][0], koordinate[-1][1],self.platno))
                    return True, koordinate
            else: return None, None
        else: return False, None

    def levo(self, *args):
        if self.xPomeraj != 30:
            self.xPomeraj = -30
            self.yPomeraj = 0

    def desno(self, *args):
        if self.xPomeraj != -30:
            self.xPomeraj = 30
            self.yPomeraj = 0

    def gore(self, *args):
        if self.yPomeraj != 30:
            self.xPomeraj = 0
            self.yPomeraj = -30

    def dole(self, *args):
        if self.yPomeraj != -30:
            self.xPomeraj = 0
            self.yPomeraj = 30

    def stani(self, *args):
        self.xPomeraj = 0
        self.yPomeraj = 0

    def izlaz(self):
        self.stanje = False

pravljanjeKvadrata = lambda x, y, platno: platno.create_rectangle(x, y, x + 30, y + 30, fill = boja)