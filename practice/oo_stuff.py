
elevators = ["0", "1", "2"]


elevator0Button = ["off", "on", "off", "off", "off", "off", "off", "off", "off", "off"]
elevator1Button = ["off", "off", "on", "off", "off", "off", "off", "off", "off", "off"]
elevator2Button = ["off", "off", "off", "off", "off", "off", "off", "off", "off", "off"]  

class elevator:
    elevator.name() 
    elevator.CurFloor()    # last floor reached
    elevator.Direction()   # up/down/idle
    elevator.Destination() # next floor in current direction


indices = [i for i, FloorNumButton in enumerate(Elevator0Button) if FloorNumButton == "on"]
print(indices)
for elevator in elevators:
    print(elevator)

    

