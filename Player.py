import uuid
from Ship import *
from ShipGroup import *

class cPlayer:
	def __init__(self):
		self.vShipGroups = list()
		self.vPlanetsConquered = list()
		self.iResources = 0
		self.UUID = uuid.uuid4()

	def AddPlanet(self, Planet):
		self.vPlanetsConquered.append(Planet)

	def RemovePlanet(self, Planet):
		self.vPlanetsConquered.remove(Planet)

	def CollectResources(self):
		for Planet in self.vPlanetsConquered:
			self.iResources += Planet.iResourcesPerTick

	def BuildShips(self):
		if (self.iResources >= cShip.iCost):
			Ship = cShip()
			self.iResources -= cShip.iCost
			ShipGroup = cShipGroup(self.UUID)
			print(ShipGroup.ToString())
			ShipGroup.AddShipToGroup(Ship)
			self.vShipGroups.append(ShipGroup)
			self.vPlanetsConquered[0].AddShipGroupToPlanet(ShipGroup)

	def GroupShips(self):
		pass

	def MoveShips(self):
		pass

	def CalculateCurrentAttack(self):
		pass

	def DiscoverTargets(self):
		pass

	def SelectTargets(self):
		pass

	def AttackTargets(self):
		pass

	def CleanUpBattle(self):
		pass

	def UpgradePlanets(self):
		pass

	def ToString(self):
		strDescription = ""
		strDescription += "%d Ship Groups owned\n" % len(self.vShipGroups)
		strDescription += "%d Planets Conquered\n" % len(self.vPlanetsConquered)
		strDescription += "Current resources %d\n" % self.iResources
		strDescription += "UUID %s\n" % str(self.UUID)
		return strDescription
