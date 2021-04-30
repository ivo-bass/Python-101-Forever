"""
We are implementing a smart GPS software.

We are taking a long trip from Sofia to Bourgas and we know the distance between the two cities.
It is a positive integer and we mark it as distance.

We know how much our car can ride with a full tank of gas.
It is a positive integer in kilometers. We mark it as tank_size.

We have a list of gas stations. We know the distance between Sofia and the current gas station.
 stations = [50, 80, 110, 180, 220, 290] Notice, the list is sorted!

By using this information we will implement a function that returns the shortest list of gas stations
 that we have to visit in order to travel from Sofia to Bourgas. We allways start with a full tank_size!
"""

from unittest import TestCase, main


class Car:
    def __init__(self, tank_size: int):
        self.tank_size = tank_size


class Trip:
    def __init__(self, distance: int, stations: list):
        self.distance = distance
        self.stations = stations
        self.current_index = 0
        self.distance_left = self.distance
        self.stops = []

    @property
    def previous_station(self):
        if self.current_index == 0:
            return 0
        return self.stations[self.current_index - 1]

    @property
    def current_station(self):
        return self.stations[self.current_index]

    @property
    def next_station(self):
        if self.current_index + 1 == len(self.stations):
            return self.distance
        return self.stations[self.current_index + 1]

    def stop_at_gas_station(self):
        self.distance_left = self.distance - self.current_station
        self.stops.append(self.current_station)

    def driving_simulation(self, car: Car):
        while self.distance_left > car.tank_size and self.current_index < len(self.stations):
            if self.next_station - self.previous_station >= car.tank_size:
                self.stop_at_gas_station()
            self.current_index += 1


def gas_stations(distance: int, tank_size: int, stations: list):
    car = Car(tank_size)
    trip = Trip(distance, stations)
    trip.driving_simulation(car)
    return trip.stops


class TestGasStations(TestCase):

    def test_1(self):
        expected = [80, 140, 220, 290]
        result = gas_stations(1000, 90, [40, 50, 80, 140, 180, 220, 290])
        self.assertListEqual(expected, result)

    def test_2(self):
        expected = [70, 140, 210, 280, 350]
        result = gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
        self.assertListEqual(expected, result)

    def test_3(self):
        expected = []
        result = gas_stations(50, 100, [10, 50, 100, 200])
        self.assertListEqual(expected, result)

    # Todo:

    # def test_4(self):
    #     expected = [50]
    #     result = gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150])
    #     self.assertListEqual(expected, result)
    #
    # def test_5(self):
    #     expected = [10]
    #     result = gas_stations(100, 50, [10, 90])
    #     self.assertListEqual(expected, result)


if __name__ == '__main__':
    main()
