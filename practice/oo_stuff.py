
elevators = ["0", "1", "2"]


Elevator0Button = ["off", "up", "off", "down", "off", "up", "off", "down", "off", "off"]
Elevator1Button = ["off", "off", "up", "up", "up", "down", "off", "up", "off", "off"]
Elevator2Button = ["off", "off", "down", "down", "down", "down", "off", "off", "off", "off"]  

class Elevator:
  def __init__(self, name, CurFloor, Direction, Destination):
        self.name = "name"
        self.CurFloor = 0         # last floor reached
        self.Direction = "idle"   # up/down/idle
        self.Destination = 0      # next floor in current directiona

Elevator0 = Elevator("0", 0, "idle", 0)
Elevator1 = Elevator("0", 0, "idle", 0)
Elevator2 = Elevator("0", 0, "idle", 0)

ActiveFloorsUpElev0 = [i for i, s in enumerate(Elevator0Button) if 'up' in s]
ActiveFloorsDnElev0 = [i for i, s in enumerate(Elevator0Button) if 'down' in s]
ActiveFloorsUpElev1 = [i for i, s in enumerate(Elevator1Button) if 'up' in s]
ActiveFloorsDnElev1 = [i for i, s in enumerate(Elevator1Button) if 'down' in s]
ActiveFloorsUpElev2 = [i for i, s in enumerate(Elevator2Button) if 'up' in s]
ActiveFloorsDnElev2 = [i for i, s in enumerate(Elevator2Button) if 'down' in s]


print(ActiveFloorsUpElev0)
print(ActiveFloorsDnElev0)
print(ActiveFloorsUpElev1)
print(ActiveFloorsDnElev1)
print(ActiveFloorsUpElev2)
print(ActiveFloorsDnElev2)
