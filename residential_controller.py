elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1


class Elevator:
    def __init__(self, _id):
           self.ID = _id
           self.status = "idle"
           self.currentFloor = 1
           self.direction = None
          # self.door = Door(_id,"closed")
           self.floorRequestButtonList = []
           self.floorRequestList = []
          # createFloorRequestButtons(_amountOfFloors)

        

    def __str__(self):
        return f"Elevator id :{self.ID} Elevator status: {self.status} Elevator current floor: {self.currentFloor} Elevator direction: {self.direction} Request button list: {self.floorRequestButtonList}Request list: {self.floorRequestList}"



testElevator = Elevator(1)
print(testElevator)