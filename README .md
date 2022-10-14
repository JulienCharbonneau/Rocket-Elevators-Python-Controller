# Rocket-Elevators-Python-Controller
This project is about implementing an elevator controller . The program is based on pseudocode file given and for this version written in python. 


### Usage 
To run the script with python run the command
`python3 residential_controller.py`

To run test with pytest run the command
`pytest`

More test can be uncomment at the bottom of the file

```
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
```
### Description
This program creates a number of columns and elevators as needed and supports the needs of elevator request button and floor access request button with a system-based efficiency management  point allowing to evaluate the best choice taking into account the floor where the request was initiated versus the availability and the direction of the cage. This system thus makes it possible to efficiently sort requests and return a lift in a short time.

#### Dependencies

`Python`
`pip`
`pytest`
