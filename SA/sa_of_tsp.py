import random as rd
import copy
class Location:
    def __init__(self, name, x, y):
        self.name = name
        self.loc = (x, y)

    def distance_between(self, location2):
        assert isinstance(location2, Location)
        return ((self.loc[0] - location2.loc[0]) ** 2 + (self.loc[1] - location2.loc[1]) ** 2) ** (1 / 2)

class Route:
    def __init__(self, path):
        self.path = path
        self.distance = self._set_distance()
        self.age = 0
    def _set_distance(self):
        d = 0
        for i in range(len(self.path)-1):
            d += self.path[i].distance_between(self.path[i+1])
        d += self.path[-1].distance_between(self.path[0]) 
        return d
    def _rand_change(self):
        length = len(self.path)
        loc1 = rd.randint(0,length-1)
        loc2 = rd.randint(0,length-1)
        self.path[loc1] , self.path[loc2] = self.path[loc2], self.path[loc1]
        return self._set_distance()

class SimulatedAnnealing:
    def __init__(self, locs, level, maxTempature, minTempature):
        self.locs = locs
        self.level = level
        self.maxTempature = maxTempature
        self.minTempature = minTempature

    def _init_route(self):
        newlocs = copy.deepcopy(self.locs)
        rd.shuffle(newlocs)
        newRoute = Route(newlocs)
        self.route = newRoute
        return newRoute
    

def create_locations():
    locations = []
    xs = []
    ys = []
    cities = []
    f = open("tsp_test")
    try:
        while True:
            s = f.readline().split()
            xs.append(int(s[1]))
            ys.append(int(s[2]))
            cities.append(str(s[0]))
    except:
        f.close()
    for x, y, name in zip(xs, ys, cities):
        locations.append(Location(name, x, y))
    return locations, xs, ys, cities
