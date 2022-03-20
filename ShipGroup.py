from Ship import *

iGlobalShipGroupCounter = 0

class cShipGroup:
	def __init__(self):
		self.iUniqueID = iGlobalShipGroupCounter
		iGlobalShipGroupCounter += 1
		self.vShips = list()

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

