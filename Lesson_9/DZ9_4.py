class Car:
    name = ""
    color = ""
    speed = 35
    is_police = False

    def go(self):
        return "car on the go!"

    def turn(self, direction):
        return f"car turned {direction}"

    def stop(self):
        return "car stopped!"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, name, color, speed):
        self.speed = speed
        self.name = name
        self.color = color

    def show_speed(self):
        if self.speed > 60:
            return "Speed is over the limit!"
        else:
            return self.speed


class WorkCar(Car):
    def __init__(self, name, color, speed):
        self.speed = speed
        self.name = name
        self.color = color

    def show_speed(self):
        if self.speed > 40:
            return "Speed is over the limit!"
        else:
            return self.speed


class PoliceCar(Car):
    is_police = True
    color = "black n white"

    def __init__(self, name, speed):
        self.speed = speed
        self.name = name


class SportCar(Car):
    def __init__(self, name, color, speed):
        self.speed = speed
        self.name = name
        self.color = color


car_1 = TownCar(speed=78, color="blue", name="jayzet-900")
car_2 = PoliceCar(speed=78, name="lk-565")
car_3 = SportCar(speed=1000, color="yellow", name="bugatti")
car_4 = WorkCar(speed=46, color="red", name="MAN Truck")


print(car_1.show_speed())
print(car_1.go())
print(car_1.turn("right"))
print(car_1.stop())
