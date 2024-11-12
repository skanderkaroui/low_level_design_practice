class Vehicule:
    def __init__(self, id, color):
        self.id = id
        self.color = color

    def honk(self):
        print("Biiiiiiiiiiiiiiiiiiiiip")

class Car(Vehicule):
    def __init__(self, id, color, speed):
        super().__init__(id, color)
        self.speed = speed

    def accelerate(self, acceleration):
        speed += acceleration
    

BUGATTI = Car('1234','violet', 10)

#the bugatti clearly inherits the honk since it's a car
BUGATTI.honk()
