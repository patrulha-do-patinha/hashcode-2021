from dataclasses import dataclass, field
from collections import defaultdict
import math, sys, functools
gcd = lambda l: functools.reduce(math.gcd, l)

# data storage
cars = []
streets = dict()
intersections = defaultdict(lambda: Intersection())
schedules = []



# type definitions
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

    def path_total_time(self):
        count = 0
        for p in self.path:
            count += streets[p].time
        return count

@dataclass
class Intersection:
    cars_per_inbound: defaultdict = field(default_factory = lambda: defaultdict(int))



# output type definitions
@dataclass
class Schedule:
    intersection: int
    schedule: list



# data load from input
[ duration, intersections_count, street_count, car_count, bonus ] = [ int(x) for x in input().split() ]

for _ in range(street_count):
    [ s, e, n, l ] = input().split()
    streets[n] = (Street(int(s), int(e), n, int(l)))

for i in range(car_count):
    path = input().split()[1:]
    cars.append(Car(i, path))



# pre processing
# sorted_cars = sorted(cars, key=lambda c: c.path_total_time())
# cars = sorted_cars[:math.floor(len(sorted_cars)*0.65)]

for car in cars:
    for street in car.path:
        end = streets[street].end
        intersections[end].cars_per_inbound[street] += 1
        start = streets[street].start
        intersections[start].cars_per_inbound[street] += 1



# processing
for i, intersection in intersections.items():
    schedule = []
    streets = sorted(intersection.cars_per_inbound.keys(), key=lambda x: intersection.cars_per_inbound[x])
    for (i, street) in enumerate(streets):
        schedule.append((street, int(i + 1)))
    schedules.append(Schedule(i, schedule))


# print(len(intersections))
# for i, intersection in intersections.items():
#     print(i)
#     print(len(intersection.counts.items()))
#     street_names = list(intersection.counts.keys())
#     street_values = [ streets[k].time for k in street_names ]
#     this_gcd = gcd(street_values)
#     street_values = [ v/this_gcd for v in street_values ]
#     biggest_time = max(street_values)
#     for i in range(len(street_names)):
#         print(f"{street_names[i]} {int(max(biggest_time//street_values[i], 1))}")

# first_streets = defaultdict(int)
# for car in cars:
#     first_streets[car.path[0]] += 1

# print(len(intersections))
# for i, intersection in intersections.items():
#     print(i)
#     print(len(intersection.counts.items()))
#     this_gcd = gcd(intersection.counts.values())
#     street_names = list(intersection.counts.keys())
#     street_names = sorted(street_names, key=lambda x: first_streets[x], reverse=True)
#     for street in street_names:
#         print(f"{street} {int(intersection.counts[street]/this_gcd)}")





# output
print(len(schedules))
for schedule in schedules:
    print(schedule.intersection)
    print(len(schedule.schedule))
    for (street, time) in schedule.schedule:
        print(f"{street} {time}")

