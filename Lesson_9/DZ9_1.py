import time


class TrafficLight:

    __color = ["red", "yellow", "green"]

    def running():
        print(TrafficLight.__color[0])
        time.sleep(7.0)
        print(TrafficLight.__color[1])
        time.sleep(2.0)
        print(TrafficLight.__color[2])
        time.sleep(10.0)


TrafficLight_1 = TrafficLight
TrafficLight_1.running()
