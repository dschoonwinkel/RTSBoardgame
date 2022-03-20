import json
from Planet import *

class cGameConfig:

	def __init__(self):
		self.iNumPlayers = 2
		self.vPlanets = list()

	def CreateFromGameConfig(self, strFilename):
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

	def ToString(self):
		print("Game Config:")
		print("Num Players:", self.iNumPlayers)
		for Planet in self.vPlanets:
			print(Planet.ToString())
			
	def WriteExampleConfigTest():
		localGameConfig = cGameConfig()
		localGameConfig.vPlanets.append(cPlanet(localGameConfig.GetNumPlayers()))
		localGameConfig.vPlanets.append(cPlanet(localGameConfig.GetNumPlayers()))
		localGameConfig.WriteGameConfigFile("ExampleGameConfig.json")