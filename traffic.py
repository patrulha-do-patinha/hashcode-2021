from dataclasses import dataclass

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

streets = []
for _ in range(street_count):
    [ s, e, n, l ] = input().split()
    streets.append(Street(int(s), int(e), n, int(l)))

cars = []
for i in range(car_count):
    path = input().split()[1:]
    cars.append(Car(i, path))

from collections import defaultdict
intersections = defaultdict(list)
for street in streets:
    intersections[street.end].append(street.name)

print(len(intersections))
for i, streets in intersections.items():
    print(i)
    print(len(streets))
    for street in streets:
        print(f"{street} 1")



