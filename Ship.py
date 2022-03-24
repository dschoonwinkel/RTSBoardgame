import random

class cShip:
	def __init__(self):
		self.strShipType = "Fighter"
		self.iDiceType = 4
		self.iHealth = 4
	
	iCost = 4

	def ToString(self):
		strOutput = ""
		strOutput += self.strShipType + "\n"
		strOutput += "Dice Type: D%d\n" % self.iDiceType
		strOutput += "Health: %d\n" % self.iHealth
		strOutput += "Cost: %d\n" % self.iCost 

	def CalculateAttack(self):
		return random.randint(1,self.iDiceType)
