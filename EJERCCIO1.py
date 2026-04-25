import random

class Equipo:
    def __init__(self, nombre):
        self.Nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0
equipo1 = Equipo("Equipo A")
equipo2 = Equipo("Equipo B")
def Puntos():
    return random.randint(10, 28)
def PuntosExtras():
    return random.randint(0, 6)
def RegistraSet(nro):
    if nro == 1:
        equipo1.setGanados = equipo1.setGanados + 1
        if equipo1.setGanados == 3:
            equipo1.partidosGanados = equipo1.partidosGanados + 1
            equipo2.partidosPerdidos = equipo2.partidosPerdidos + 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            return 1 
    elif nro == 2:
        equipo2.setGanados = equipo2.setGanados + 1
        if equipo2.setGanados == 3:
            equipo2.partidosGanados = equipo2.partidosGanados + 1
            equipo1.partidosPerdidos = equipo1.partidosPerdidos + 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            return 1
    return 0

def JugarPartido():
    termino = 0
    while termino == 0:
        p1 = Puntos()
        p2 = Puntos()
        while p1 < 25 and p2 < 25:
            p1 = p1 + PuntosExtras()
            p2 = p2 + PuntosExtras()
        if p1 == p2:
            while p1 == p2:
                p1 = p1 + PuntosExtras()
                p2 = p2 + PuntosExtras()
        if p1 > p2:
            termino = RegistraSet(1)
        else:
            termino = RegistraSet(2)

def ResultadoTorneo():
    print("Nombre del equipo: " + equipo1.Nombre)
    print("Ganados: " + str(equipo1.partidosGanados))
    print("Perdidos: " + str(equipo1.partidosPerdidos))
    print("--------------------")
    print("Nombre del equipo: " + equipo2.Nombre)
    print("Ganados: " + str(equipo2.partidosGanados))
    print("Perdidos: " + str(equipo2.partidosPerdidos))

entrada = input("¿Cuantos partidos juegan?: ")
n = int(entrada)

for i in range(n):
    JugarPartido()

ResultadoTorneo()