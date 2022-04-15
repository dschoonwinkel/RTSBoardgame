import uuid
from Ship import *
from ShipGroup import *

class cPlayer:
    def __init__(self):
        self.vShipGroups = list()
        self.vPlanetsConquered = list()
        self.iResources = 0
        self.UUID = uuid.uuid4()

    def AddPlanet(self, Planet):
        self.vPlanetsConquered.append(Planet)

    def RemovePlanet(self, Planet):
        self.vPlanetsConquered.remove(Planet)

    def CollectResources(self):
        for Planet in self.vPlanetsConquered:
            self.iResources += Planet.iResourcesPerTick

    def BuildShips(self):
        if (self.iResources >= cShip.iCost):
            Ship = cShip()
            self.iResources -= cShip.iCost
            # Create the Ship group and assign it to the player and planet
            ShipGroup = cShipGroup(self.UUID, self.vPlanetsConquered[0])
            # print(ShipGroup)
            ShipGroup.AddShipToGroup(Ship)
            self.vShipGroups.append(ShipGroup)

    def CombineOneShipGroup(self):
        for ShipGroup1 in self.vShipGroups:
            # print("ShipGroup1:", ShipGroup1)
            for ShipGroup2 in self.vShipGroups:
                if ShipGroup1 == ShipGroup2:
                    continue
                # print("ShipGroup2", ShipGroup2)
                if ShipGroup1.AtSamePlanet(ShipGroup2):
                    # print("Same planet found")
                    ShipGroup1.TransferShipsToOtherGroup(ShipGroup2)
                    self.vShipGroups.remove(ShipGroup1)
                    return True

        # print("No more ship groups to combine")
        return False # No more ship groups to combine

    def GroupShips(self):
        StillCombining = True
        while StillCombining == True:
            StillCombining = self.CombineOneShipGroup()

    def MoveShips(self):
        pass

    def CalculateCurrentAttack(self):
        pass

    def DiscoverTargets(self):
        pass

    def SelectTargets(self):
        pass

    def AttackTargets(self):
        pass

    def CleanUpBattle(self):
        pass

    def UpgradePlanets(self):
        pass

    def CountShips(self):
        self.iNumShipsOwned = 0
        for ShipGroup in self.vShipGroups:
            self.iNumShipsOwned += ShipGroup.GetSize() 

    def __str__(self):
        strDescription = ""
        strDescription += "%d Ship Groups owned\n" % len(self.vShipGroups)
        self.CountShips()
        strDescription += "%d Ships owned\n" % (self.iNumShipsOwned)
        strDescription += "%d Planets Conquered\n" % len(self.vPlanetsConquered)
        strDescription += "Current resources %d\n" % self.iResources
        strDescription += "UUID %s\n" % str(self.UUID)
        return strDescription
