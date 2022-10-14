

import time


elevatorID = 1
floorRequestButtonID = 1


class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.status = "Online"
        self.elevatorList = []
        self.callButtonList = []

        self.createCallButtons(_amountOfFloors)
        self.createElevators(_amountOfFloors, _amountOfElevators)

    def createCallButtons(self, _amountOfFloors):
        callButtonID = 1

        buttonFloor = 1
        for floor in range(_amountOfFloors):
            if buttonFloor < _amountOfFloors:
                callButton = CallButton(callButtonID, buttonFloor, "UP")
                self.callButtonList.append(callButton)
                callButtonID += 1
            if buttonFloor > 1:
                self.callButton = CallButton(callButtonID, buttonFloor, "Down")
                self.callButtonList.append(self.callButton)
                callButtonID += 1

            buttonFloor += 1

    def createElevators(self, _amountOfFloors, _amountOfElevators):
        global elevatorID
        for eachElevator in range(_amountOfElevators):
            elevator = Elevator(elevatorID, _amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1

    def requestElevator(self, floor, direction):
        bestElevator = self.findElevator(floor, direction)
        bestElevator.floorRequestList.append(floor)
        bestElevator.sortFloorList()
        bestElevator.move()
        bestElevator.operateDoors()
        return bestElevator

    def findElevator(self, requestedFloor, requestedDirection):

        bestElevatorInformations = {
            "bestElevator": None,
            "bestScore": 5,
            "referenceGap": 10000000,
            "currentFloor": 1,
        }

        for elevator in self.elevatorList:

            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:

                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    1, elevator, bestElevatorInformations, requestedFloor)

            elif requestedFloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction:

                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    2, elevator, bestElevatorInformations, requestedFloor)

            elif requestedFloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction:

                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    2, elevator, bestElevatorInformations, requestedFloor)

            elif elevator.status == "idle":

                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    3, elevator, bestElevatorInformations, requestedFloor)

            else:
                bestElevatorInformations = self.checkIfElevatorIsBetter(
                    4, elevator, bestElevatorInformations, requestedFloor)

        return bestElevatorInformations["bestElevator"]

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, requestedFloor):
        if scoreToCheck < bestElevatorInformations["bestScore"]:
            bestElevatorInformations["bestScore"] = scoreToCheck
            bestElevatorInformations["bestElevator"] = newElevator
            bestElevatorInformations["referenceGap"] = abs(
                newElevator.currentFloor - requestedFloor)

        elif bestElevatorInformations["bestScore"] == scoreToCheck:
            currentFloor = newElevator.currentFloor
            gap = abs(currentFloor - requestedFloor)

            if bestElevatorInformations["referenceGap"] > gap:
                bestElevatorInformations["bestElevator"] = newElevator
                bestElevatorInformations["referenceGap"] = gap

        return bestElevatorInformations

    def __str__(self):
        return f"Column id: {self.ID} Column status {self.status} Column elevator list {self.elevatorList[0]}, {self.elevatorList[-1]}  Column call button list {self.callButtonList[0]}, {self.callButtonList[-1]}"


class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = "idle"
        self.currentFloor = 1
        self.direction = "down"
        self.door = Door(_id)
        self.floorRequestButtonList = []
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors)

    def createFloorRequestButtons(self, _amountOfFloors):
        buttonFloor = 1
        floorRequestButtonID = 1
        for floor in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(
                floorRequestButtonID, buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor += 1
            floorRequestButtonID += 1

    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    def move(self):
        while len(self.floorRequestList) > 0:
            destination = self.floorRequestList[0]
            self.status = "moving"
            if self.currentFloor < destination:
                self.direction = "up"
                while self.currentFloor < destination:
                    self.currentFloor += 1
                    self.screenDisplay = self.currentFloor

            elif self.currentFloor > destination:
                self.status = "down"
                while self.currentFloor > destination:
                    self.currentFloor -= 1
                    self.screenDisplay = self.currentFloor

            self.status = "stopped"
            self.floorRequestList.pop()

        self.status = "idle"

    def sortFloorList(self):
        if self.direction == "up":
            self.floorRequestList.sort()
        else:
            self.floorRequestList.sort(reverse=True)

    def operateDoors(self):
        print("wait 5 seconds")
        time.sleep(5)

    def __str__(self):
        return f"Elevator id :{self.ID} Elevator status: {self.status} Elevator current floor: {self.currentFloor} Elevator direction: {self.direction} Request button list: {str(self.floorRequestButtonList[0])}Request list: {self.floorRequestList}"


class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.floor = _floor
        self.status = "OFF"
        self.direction = _direction

    def printCallButton(self):

        print("call button id,status , direction, and floor: ",
              self.ID, self.status, self.direction, self.floor)


class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.status = "OFF"
        self.floor = _floor

    def __str__(self):
        return f"id :{self.ID}, status: {self.status}, floor : {self.floor}"

    def printFloorRequestButton(self):
        print("Request Button id, status an floor:",
              self.ID, self.status, self.floor)


class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = "closed"

    def printDoor(self):
        print("Door id and status:", self.ID, self.status)


# testColumn = Column(1, 10, 2)
# print(testColumn)
# testColumn.findElevator(1, 3)

# testElevator = Elevator(1, 10)
# testElevator.requestFloor(8)
# print(testElevator)
# testCallButton = CallButton(1,10,"up")
# testCallButton.printCallButton()
# testRequestButton = FloorRequestButton(1,10)
# testRequestButton.printFloorRequestButton()
# testDoor = Door(1,"close")
# testDoor.printDoor()
