#! /usr/bin/python

from random import randint
from enum import Enum

class Actions(Enum):
	nord = 1
	oest = 2
	syd  = 3
	vest = 4
	signalA = 5
	signalB = 6
	signalC = 7
	signalD = 8
	signalE = 9
	signalF = 10
	signalG = 11


class Bo:
	def __init__(self, ):
		pass

# hvordan gemmer vi hvad en myre har samlet op?
class SimpelMyre:
	def __init__(self):
		pass

	def reagere(self, input):
		return None

class Mad:
	def __init__(self):
		pass

# Opret verden
nRaekker = 5
nKolonner = 10
kort = []
for i in range(nRaekker):
	raekke = []
	for j in range(nKolonner):
		raekke.append(None)
	kort.append(raekke)

# Pladser Bo Hold 1
bo1X = randint(0, nKolonner-1)
bo1Y = randint(0, nRaekker-1) 
kort[bo1Y][bo1X] = 

# Pladser Bo Hold 2
bo1X = randint(0, nKolonner-1)
bo1Y = randint(0, nRaekker-1) 
kort[bo1Y][bo1X] = "bo1" 

# Pladser Bo Hold 2


# Simulering

# Udskriv resultat

print kort
