class GroundVehicle(object):
    def move(self):
        print("Ground movement")


class FlyingVehicle(object):
    def move(self):
        print("Flying movement")


class Car(GroundVehicle):
    pass


class Airplane(FlyingVehicle, GroundVehicle):
    pass

# c = Car()
# c.move()

a = Airplane()
a.move()