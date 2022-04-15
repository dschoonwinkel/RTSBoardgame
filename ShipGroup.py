from Ship import *
import uuid

class cShipGroup:
	def __init__(self, OwnerUUID, CurrentPlanet):
		self.UUID = uuid.uuid4()
		self.vShips = list()
		self.OwnerUUID = OwnerUUID
		self.CurrentPlanet = CurrentPlanet
		CurrentPlanet.AddShipGroupToPlanet(self)

	def AddShipToGroup(self, Ship):
		self.vShips.append(Ship)

	def RemoveShipFromGroup(self, strShipType):
		for Ship in self.vShips:
			if Ship.strShipType == strShipType:
				self.vShips.remove(Ship)
				break

	def TransferShipsToOtherGroup(self, OtherShipGroup):
		for Ship in self.vShips:
			OtherShipGroup.AddShipToGroup(Ship)

		self.vShips.clear()

	def __str__(self):
		strOutput = "Ship group UUID: %s\n" % str(self.UUID)
		strOutput += "Owner UUID %s\n" % str(self.OwnerUUID)
		for Ship in self.vShips:
			strOutput += str(Ship) + "\n"
		return strOutput

	def CalculateCurrentAttack(self):
		self.iTotalAttack = 0
		for Ship in self.vShips:
			self.iTotalAttack += Ship.CalculateAttack()

	def GetSize(self):
		return len(self.vShips)

	def AtSamePlanet(self, OtherShipGroup):
		if self.CurrentPlanet == OtherShipGroup.CurrentPlanet:
			return True
		else:
			return False


