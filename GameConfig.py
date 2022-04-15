import json
from Planet import *
from Player import *

class cGameState:

	def __init__(self):
		self.iNumPlayers = 2
		self.vPlanets = list()
		self.vPlayers = list()
		for i in range(self.iNumPlayers):
			self.vPlayers.append(cPlayer())

	def CreateFromConfig(self, strFilename):
		dictCfg = dict()
		with open(strFilename) as json_data_file:
			dictCfg = json.load(json_data_file)
		self.iNumPlayers = dictCfg["NumPlayers"]
		for PlanetDict in dictCfg["Planets"]:
			Planet = cPlanet(self.iNumPlayers)
			Planet.FromDict(PlanetDict)
			self.vPlanets.append(Planet)

	def WriteGameConfigFile(self, strFilename):
		outputDict = dict()
		outputDict["NumPlayers"] = self.iNumPlayers
		outputDict["Planets"] = list()
		for Planet in self.vPlanets:
			outputDict["Planets"].append(Planet.ToDict())
		with open(strFilename, 'w') as outfile:
			json.dump(outputDict, outfile, indent=4)

	def GetNumPlayers(self):
		return self.iNumPlayers

	def SetNumPlayers(self, iNumPlayers):
		self.iNumPlayers = iNumPlayers

	def __str__(self):
		print("Game State:")
		print("Num Players:", self.iNumPlayers)
		for Planet in self.vPlanets:
			print(Planet)
			
	def WriteExampleConfigTest():
		localGameState = cGameState()
		localGameState.vPlanets.append(cPlanet(localGameState.GetNumPlayers()))
		localGameState.vPlanets.append(cPlanet(localGameState.GetNumPlayers()))
		localGameState.WriteGameConfigFile("ExampleGameConfig.json")

	def SimulateTick(self):
		for Player in self.vPlayers:
			Player.CollectResources()

		for Player in self.vPlayers:
			Player.BuildShips()

		for Player in self.vPlayers:
			Player.GroupShips()

		for Player in self.vPlayers:
			Player.MoveShips()

		for Player in self.vPlayers:
			Player.CalculateCurrentAttack()

		for Player in self.vPlayers:
			Player.DiscoverTargets()

		for Player in self.vPlayers:
			Player.SelectTargets()

		for Player in self.vPlayers:
			Player.AttackTargets()

		for Player in self.vPlayers:
			Player.CleanUpBattle()

		for Player in self.vPlayers:
			Player.UpgradePlanets()
