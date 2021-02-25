from dataclasses import dataclass
from collections import defaultdict
from functools import reduce
import math, sys

@dataclass
class Street:
    start: int
    end: int
    name: str
    time: int

@dataclass
class Car:
    i: int
    path: list

[ duration, intersections_count, street_count, car_count, bonus ] = [ int(x) for x in input().split() ]

streets = dict()
for _ in range(street_count):
    [ s, e, n, l ] = input().split()
    streets[n] = (Street(int(s), int(e), n, int(l)))

cars = []
for i in range(car_count):
    path = input().split()[1:]
    cars.append(Car(i, path))

result = bonus * car_count
for car in cars:
    time = 0
    for street in path:
        time += streets[street].time
    result += duration - time
print(result, file=sys.stderr)
