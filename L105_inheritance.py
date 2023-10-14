class Vehicle:  # ยานพาหนะ
    license_code = ""
    serial_code = ""
    face = ""
    def turn_on_air(self):
        print("Turn on : Air")

class Car(Vehicle):
    def carHello(self):
        print("Car's Hello !!")
class Pick_up(Vehicle):
    def pickupHello(self):
        print("Pick Up's Hello !!")
class Van(Vehicle):
    def vanHello(self):
        print("Van's Hello !!")
class Estate_car(Vehicle):
    def estatecarHello(self):
        print("Estate Car's Hello !!")

car1 = Car()
car1.turn_on_air()
car1.carHello()
print()
pick_up1 = Pick_up()
pick_up1.turn_on_air()
pick_up1.pickupHello()
print()
van1 = Van()
van1.turn_on_air()
van1.vanHello()
print()
estate_car1 = Estate_car()
estate_car1.turn_on_air()
estate_car1.estatecarHello()


