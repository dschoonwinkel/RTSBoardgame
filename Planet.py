class cPlanet:
	def __init__(self, iNumPlayers):
		# Constant variables
		self.iPlanetHealth = 24;
		self.iResourcesPerTick = 2
		self.iPlanetGravity = 3
		# Dynamic variables
		self.iPlanetUpgrades = 0
		self.vShipGroups = list()
		self.dictPlayerHits = dict()
		for iPlayerNumber in range(iNumPlayers):
			self.dictPlayerHits[iPlayerNumber] = 0

	def ToString(self):
		strDescription = ""
		strDescription += "Planet:\n"
		strDescription += "Planet Health: %d\n" % self.iPlanetHealth
		strDescription += "Resources Per Tick: %d\n" % self.iResourcesPerTick
		strDescription += "Planet Gravity: %d\n" % self.iPlanetGravity
		strDescription += "Planet Upgrades: %d\n" % self.iPlanetUpgrades
		strDescription += "Ship Groups at Planet: %d\n" % len(self.vShipGroups)
		for key in self.dictPlayerHits.keys():
			strDescription += "Player %d Hits: %d\n" % (key, self.dictPlayerHits[key])

		return strDescription

	def ToDict(self):
		outDict = dict()
		outDict["PlanetHealth"] = self.iPlanetHealth
		outDict["ResourcePerTick"] = self.iResourcesPerTick
		outDict["PlanetGravity"] = self.iPlanetGravity
		return outDict

	def FromDict(self, inDict):
		self.iPlanetHealth = inDict["PlanetHealth"]
		self.iResourcesPerTick = inDict["ResourcePerTick"]
		self.iPlanetGravity = inDict["PlanetGravity"]