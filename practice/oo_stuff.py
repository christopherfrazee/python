
elevators = ["0", "1", "2"]


elevator0Button = ["off", "on", "off", "off", "off", "off", "off", "off", "off", "off"]
elevator1Button = ["off", "off", "on", "off", "off", "off", "off", "off", "off", "off"]
elevator2Button = ["off", "off", "off", "off", "off", "off", "off", "off", "off", "off"]  

class Elevator:
  def __init__(self, name, CurFloor, Direction, Destination):
        self.name = name
        self.CurFloor = 0       # last floor reached
        self.Direction = idle   # up/down/idle
        self.Destination = 0    # next floor in current directiona


Elevator0 = Elevator("0", 0, "idle", 0)
Elevator1 = Elevator("0", 0, "idle", 0)
Elevator2 = Elevator("0", 0, "idle", 0)

indices = [i for i, FloorNumButton in enumerate(Elevator0Button) if FloorNumButton == "on"]
print(indices)
for elevator in elevators:
    print(elevator)

    

