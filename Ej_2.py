class Mago:
    def hechizos(self):
        print("Hechizos - Mago")

class Guerrero:
    def defensa(self):
        print("Defensa - Guerrero")

class Elfo:
    def aura(self):
        print("Aura - Elfo")

class DarkLorda(Guerrero, Elfo):
    def hechizos(self):
        print("Hechizos - DarkLord")

class DarkLordb(Elfo, Guerrero):
    def hechizos(self):
        print("Hechizos - DarkLord")

a = DarkLorda()
a.defensa()   # de Guerrero
a.aura()      # de Elfo
a.hechizos() # de DarkLord

b = DarkLordb()
b.defensa()   # sigue siendo de Guerrero
b.aura()      # sigue siendo de Elfo
b.hechizos() # sigue siendo de DarkLord