import json
from Planet import *

class cGameConfig:

	def __init__(self):
		self.iNumPlayers = 2
		self.vPlanetList = list()

	def CreateFromGameConfig(self, strFilename):
		self.__init__()
		dictCfg = ReadGameConfigFile(strFilename)
		self.iNumPlayers = dictCfg["NumPlayers"]
		for Planet in dictCfg["Planets"]:
			self.vPlanetList = cPlanet(self.iNumPlayers)

	def ReadGameConfigFile(self, strFilename):
		with open(strFilename) as json_data_file:
			dictCfg = json.load(json_data_file)
			print(dictCfg)
			if "NumPlayers" in dictCfg:
				iNumPlayers = int(dictCfg["NumPlayers"])


			return dictCfg

	def WriteGameConfigFile(self, strFilename):
		outputDict = dict()
		outputDict["NumPlayers"] = self.iNumPlayers
		outputDict["Planets"] = list()
		for Planet in self.vPlanetList:
			outputDict["Planets"].append(Planet.toDict())
		with open(strFilename, 'w') as outfile:
			json.dump(outputDict, outfile, indent=4)

	def GetNumPlayers(self):
		return self.iNumPlayers

	def SetNumPlayers(self, iNumPlayers):
		self.iNumPlayers = iNumPlayers

	def ToString(self):
		print("Game Config:")
		print("Num Players:", self.iNumPlayers)
		for Planet in self.vPlanetList:
			
