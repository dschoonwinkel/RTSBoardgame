class cPlanet:
	def __init__(self, iNumPlayers):
		self.ListOfShipGroups = list()
		self.iPlanetHealth = 24;
		self.dictPlayerHits = dict()
		for iPlayerNumber in range(iNumPlayers):
			self.dictPlayerHits[iPlayerNumber] = 0
		self.iResourcesPerTick = 2
		self.iPlanetGravity = 3
		self.iPlanetUpgrades = 0

	def ToString(self):
		strDescription = ""
		strDescription += "Planet:\n"
		strDescription += "Planet Health: %d\n" % self.iPlanetHealth
		strDescription += "Resources Per Tick: %d\n" % self.iResourcesPerTick
		strDescription += "Planet Gravity: %d\n" % self.iPlanetGravity
		strDescription += "Planet Upgrades: %d\n" % self.iPlanetUpgrades 