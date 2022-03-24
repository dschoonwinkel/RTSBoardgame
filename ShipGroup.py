from Ship import *
import uuid

class cShipGroup:
	def __init__(self, OwnerUUID):
		self.UUID = uuid.uuid4()
		self.vShips = list()
		self.OwnerUUID = OwnerUUID

	def AddShipToGroup(self, Ship):
		self.vShips.append(Ship)

	def RemoveShipFromGroup(self, strShipType):
		for Ship in self.vShips:
			if Ship.strShipType == strShipType:
				self.vShips.remove(Ship)
				break

	def ToString(self):
		strOutput = "Ship group UUID: %s\n" % str(self.UUID)
		strOutput += "Owner UUID %s\n" % str(self.OwnerUUID)
		for Ship in self.vShips:
			strOutput += Ship.ToString() + "\n"
		return strOutput

	def CalculateCurrentAttack(self):
		self.iTotalAttack = 0
		for Ship in self.vShips:
			self.iTotalAttack += Ship.CalculateAttack()


