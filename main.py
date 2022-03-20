from GameConfig import *
from Player import *
from Planet import *
from Ship import *
from ShipGroup import *

def main():
	print("Starting RTS Boardgame Monte Carlo Simulation")
	localGameConfig = cGameConfig()
	localGameConfig.WriteGameConfigFile("GameConfig.json")


if __name__ == '__main__':
	main()