#อะไรที่เหมือนกันให้แยกออกมาสร้างเป็น class ใหม่
#อะไรที่แตกต่างกันแยกออกไปใส่ เฉพาะ class นั้นๆ

class Vehicle:
    LicenseCode = ""
    SeriesCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On Air")


class Car(Vehicle):
    def sayHello(self):
        print("Hello world")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = EstateCar()
estatecar1.turnOnAirConditioner()



