


import time


elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column:
    def __init__(self,_id,_amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.status = "Online"
        self.elevatorList = [1,2,3]
        self.callButtonList = [1,2,3,4,5,6]

        # self.createCallButtons(_amountOfFloors)
        # self.createElevators(_amountOfFloors,_amountOfElevators)

    def __str__(self):
        return f"Column id: {self.ID} Column status {self.status} Column elevator list {self.elevatorList[0]}, {self.elevatorList[-1]}  Column call button list {self.callButtonList[0]}, {self.callButtonList[-1]}"
        


class Elevator:
    def __init__(self, _id, _amountOfFloors):
            self.ID = _id
            self.status = "idle"
            self.currentFloor = 1
            self.direction = "down"
            self.door = Door(_id,"closed")
            self.floorRequestButtonList = [2,4]
            self.floorRequestList = [7,2,10]
            self.createFloorRequestButtons(_amountOfFloors)
           
    def createFloorRequestButtons(self,_amountOfFloors):
        buttonFloor = 1
        floorRequestButtonID = 1
        for floor in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(floorRequestButtonID,buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor += 1
            floorRequestButtonID += 1


    def requestFloor(self,floor):
        self.floorRequestList.append(floor)  
        self.move()
        self.operateDoors()  

    def move(self):
        numberOfRequest = len(self.floorRequestList)
        while numberOfRequest > 0:
            destination = self.floorRequestList[0]
            self.status = "moving"
            if self.currentFloor < destination:
               self.direction = "up"
               self.sortFloorList()
               while self.currentFloor < destination:
                self.currentFloor += 1
                self.screenDisplay = self.currentFloor

            elif self.currentFloor > destination:
                self.status = "down"
                self.sortFloorList()
                while self.currentFloor > destination:
                    self.currentFloor -= 1
                    self.screenDisplay = self.currentFloor
                

            self.status = "stopped"
            self.floorRequestList.pop(0)
            numberOfRequest -= 1


        self.status = "idle"
                    

            

    def sortFloorList(self):
         if self.direction == "up":
            self.floorRequestList.sort()
         else:
            self.floorRequestList.sort(reverse= True)
            
    def operateDoors(self):
        print("wait 5 seconds")
        time.sleep(5)



    def __str__(self):
        return f"Elevator id :{self.ID} Elevator status: {self.status} Elevator current floor: {self.currentFloor} Elevator direction: {self.direction} Request button list: {str(self.floorRequestButtonList[0])}Request list: {self.floorRequestList}"





class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.floor =_floor
        self.status = "OFF"
        self.direction = _direction

    def printCallButton(self):

        print("call button id,status , direction, and floor: ",self.ID, self.status, self.direction, self.floor)
        

class FloorRequestButton:
    def __init__(self,_id, _floor):
        self.ID = _id
        self.status = "OFF"
        self.floor = _floor

    def __str__(self):
        return f"id :{self.ID}, status: {self.status}, floor : {self.floor}"
        

    def printFloorRequestButton(self):
        print("Request Button id, status an floor:", self.ID, self.status, self.floor)      
         


class Door:
    def __init__(self,_id, _status):
        self.ID = _id
        self.status = _status


    def printDoor(self):
        print("Door id and status:", self.ID, self.status) 



testColumn = Column(1,10,2)
print(testColumn)


testElevator = Elevator(1, 10)
testElevator.requestFloor(8)
print(testElevator)
testCallButton = CallButton(1,10,"up")
testCallButton.printCallButton()
testRequestButton = FloorRequestButton(1,10)
testRequestButton.printFloorRequestButton()
testDoor = Door(1,"close")
testDoor.printDoor()