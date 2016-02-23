#! /usr/bin/python3

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

class indhold(Enum):
	mad = 1
	bo = 2


class Bo:
	def __init__(self, holdNavn, myreType):
		self.holdNavn = holdNavn
		self.myreType = myreType
		self.antalMad = 1 # hvor meget mad har vi i boet: 1 mad -> 1 myer (kan laves om...)

	def __str__(self):
		return("B:"+self.holdNavn)

	def update(self):
		self.lavNyMyrer()

	def lavNyMyrer(self):
		global kort
		global nKolonner, nRaekker
		for i in range(self.antalMad):
			# Opretter lige myre en tilfaeldigt sted - det maa vi aendre senere
			for i in range(10):
				nyMyer = self.myreType(self.holdNavn)
				bo1X = randint(1, nKolonner-2)
				bo1Y = randint(1, nRaekker-2)
				if(kort[bo1Y][bo1X] == None):
					kort[bo1Y][bo1X] = nyMyer
					break
		self.mad = 0

class Myre:
	def __init__(self, holdNavn):
		self.harMad = False
		self.holdNavn = holdNavn

	def __str__(self):
		return("M:"+self.holdNavn)

	def reagere(self, input):
		return None


#############################################################################
# Det er det her kode brugen skal rette i

#############################################################################
class SimpelMyre(Myre):
	def __init__(self, holdNavn):
		self.harMad = False
		self.holdNavn = holdNavn

	def __str__(self):
		return("M:"+self.holdNavn)

	def update(self, input):
		return None


class Mad:
	def __init__(self):
		pass


# Opret verden
nRaekker = 10
nKolonner = 15
kort = []
for i in range(nRaekker):
	raekke = []
	for j in range(nKolonner):
		raekke.append(None)
	kort.append(raekke)

# Pladser Bo Hold 1
bo1X = randint(1, nKolonner-2)
bo1Y = randint(1, nRaekker-2) 
startBo1 = Bo("Sort", SimpelMyre)
kort[bo1Y][bo1X] = startBo1

# Pladser Bo Hold 2
bo1X = randint(1, nKolonner-2)
bo1Y = randint(1, nRaekker-2) 
startBo2 = Bo("Brun", SimpelMyre)
kort[bo1Y][bo1X] = startBo2

# Simulering
nRunter = 10
for i in range(nRunter):
	startBo1.update()
	startBo2.update()

for row in kort:
	for cell in row:
		if(hasattr(cell,"reagere")):
			myre_omgivelser = None
			cell.reagere(myre_omgivelser)

# Udskriv resultat
def printKort():
	out = ""
	for row in kort:
		for cell in row:
			out += str(cell)+" "
		out += "\n"
	print(out)

printKort()

