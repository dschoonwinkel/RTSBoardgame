from GameConfig import *
from Player import *
from Planet import *
from Ship import *
from ShipGroup import *
import time
import random

def main():
	print("Starting RTS Boardgame Monte Carlo Simulation")
	random.seed()	# Uses system time to seed randomizer
	localGameState = cGameState()
	localGameState.CreateFromConfig("GameConfig.json")
	for Planet in localGameState.vPlanets:
		print(Planet.ToString())

	try:
		while (True):
			print("Tick")
			time.sleep(30)
	except KeyboardInterrupt:
		print("Stopping Main loop")

if __name__ == '__main__':
	main()