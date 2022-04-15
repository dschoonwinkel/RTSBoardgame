import uuid

class cPlanet:
	def __init__(self, iNumPlayers, strName=""):
		# Constant variables
		self.strName = strName
		self.iPlanetHealth = 24
		self.iResourcesPerTick = 2
		self.iPlanetGravity = 3
		self.UUID = uuid.uuid4()
		# Dynamic variables
		self.iPlanetUpgrades = 0
		self.vShipGroups = list()
		self.dictPlayerHits = dict()
		for iPlayerNumber in range(iNumPlayers):
			self.dictPlayerHits[iPlayerNumber] = 0

	def AddShipGroupToPlanet(self, ShipGroup):
		self.vShipGroups.append(ShipGroup)

	def RemoveShipGroupFromPlanet(self, ShipGroup):
		self.vShipGroups.remove(ShipGroup)

	def __str__(self):
		strDescription = ""
		strDescription += "Planet %s:\n" % self.strName 
		strDescription += "Planet Health: %d\n" % self.iPlanetHealth
		strDescription += "Resources Per Tick: %d\n" % self.iResourcesPerTick
		strDescription += "Planet Gravity: %d\n" % self.iPlanetGravity
		strDescription += "Planet Upgrades: %d\n" % self.iPlanetUpgrades
		strDescription += "Ship Groups at Planet: %d\n" % len(self.vShipGroups)
		for key in self.dictPlayerHits.keys():
			strDescription += "Player %d Hits: %d\n" % (key, self.dictPlayerHits[key])
		strDescription += "UUID: %s\n" % str(self.UUID)

		return strDescription

	def ToDict(self):
		outDict = dict()
		outDict["PlanetName"] = self.strName
		outDict["PlanetHealth"] = self.iPlanetHealth
		outDict["ResourcePerTick"] = self.iResourcesPerTick
		outDict["PlanetGravity"] = self.iPlanetGravity
		return outDict

	def FromDict(self, inDict):
		self.strName = inDict["PlanetName"]
		self.iPlanetHealth = inDict["PlanetHealth"]
		self.iResourcesPerTick = inDict["ResourcePerTick"]
		self.iPlanetGravity = inDict["PlanetGravity"]