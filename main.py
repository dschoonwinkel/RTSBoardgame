from GameConfig import *
from Player import *
from Planet import *
from Ship import *
from ShipGroup import *

def main():
	print("Starting RTS Boardgame Monte Carlo Simulation")
	localGameConfig = cGameConfig()
	localGameConfig.CreateFromConfig("GameConfig.json")
	for Planet in localGameConfig.vPlanets:
		print(Planet.ToString())

if __name__ == '__main__':
	main()