from dataclasses import dataclass
import sys

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

@dataclass
class Intersection:
    counts: dict
    def count(self, street):
        if street not in self.counts:
            self.counts[street] = 1
        else:
            self.counts[street] += 1

intersections = dict()
for car in cars:
    for street in car.path:
        end = streets[street].end
        if end not in intersections:
            intersections[end] = Intersection(dict())
        intersections[end].count(street)

from math import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x

# print(len(intersections))
# for i, intersection in intersections.items():
#     print(i)
#     print(len(intersection.counts.items()))
#     street_names = list(intersection.counts.keys())
#     street_values = [ streets[k].time for k in street_names ]
#     this_gcd = find_gcd(street_values)
#     street_values = [ v/this_gcd for v in street_values ]
#     biggest_time = max(street_values)
#     for i in range(len(street_names)):
#         print(f"{street_names[i]} {int(max(biggest_time//street_values[i], 1))}")

# print(len(intersections))
# for i, intersection in intersections.items():
#     print(i)
#     print(len(intersection.counts.items()))
#     this_gcd = find_gcd(intersection.counts.values())
#     for (street, n) in intersection.counts.items():
#         print(f"{street} {n//this_gcd}")

print(len(intersections.items()))
for i, intersection in intersections.items():
    print(i)
    print(len(intersection.counts.items()))
    streets = sorted(intersection.counts.keys(), key=lambda x: intersection.counts[x])
    for (i, street) in enumerate(streets):
        print(f"{street} {i+1}")



