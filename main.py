from GameConfig import *
from Player import *
from Planet import *
from Ship import *
from ShipGroup import *
import time
import random
import os

def main():
	os.system('cls')
	os.system('color 04')
	print("Starting RTS Boardgame Monte Carlo Simulation")
	print("Start up variables:\n")
	random.seed()	# Uses system time to seed randomizer
	localGameState = cGameState()
	localGameState.CreateFromConfig("GameConfig.json")
	for Planet in localGameState.vPlanets:
		print(Planet.ToString())

	for i in range(len(localGameState.vPlayers)):
		print("Player %d" % i)
		localGameState.vPlayers[i].AddPlanet(localGameState.vPlanets[i])
		print(localGameState.vPlayers[i].ToString())
	time.sleep(10)
	try:
		while (True):
			os.system("cls")
			os.system("color 02")
			print("Tick\n")
			localGameState.SimulateTick()
			for i in range(len(localGameState.vPlayers)):
				print("Player %d" % i)
				print(localGameState.vPlayers[i].ToString())
			time.sleep(5)
	except KeyboardInterrupt:
		print("Stopping Main loop")

if __name__ == '__main__':
	main()