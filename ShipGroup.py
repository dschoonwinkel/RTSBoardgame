from Ship import *

iGlobalShipGroupCounter = 0

class cShipGroup:
	def __init__(self, iOwner):
		self.iUniqueID = iGlobalShipGroupCounter
		iGlobalShipGroupCounter += 1
		self.vShips = list()
		self.iOwner = iOwner

	def AddShipToGroup(self, Ship):
		self.vShips.append(Ship)

	def RemoveShipFromGroup(self, strShipType):
		for Ship in self.vShips:
			if Ship.strShipType == strShipType:
				self.vShips.remove(Ship)
				break

	def ToString(self):
		strOutput = ""
		for Ship in self.vShips:
			strOutput += Ship.ToString() + "\n"

	def CalculateCurrentAttack(self):
		self.iTotalAttack = 0
		for Ship in self.vShips:
			self.iTotalAttack += Ship.CalculateAttack()


