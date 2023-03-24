import random as rd
from matplotlib import pyplot as plt
import os
import copy
from math import exp
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
    def _set_distance(self):
        d = 0
        for i in range(len(self.path)-1):
            d += self.path[i].distance_between(self.path[i+1])
        d += self.path[-1].distance_between(self.path[0])
        self.distance = d 
        return d
    def _two_change(self):
        length = len(self.path)
        loc1 = rd.randint(0,length-1)
        loc2 = rd.randint(0,length-1)
        self.path[loc1] , self.path[loc2] = self.path[loc2], self.path[loc1]
        return self._set_distance()
    def _half_change(self):
        length = len(self.path)
        loc = rd.randint(0,length-1)
        self.path = self.path[loc:]+self.path[0:loc]
        return self._set_distance()

class SimulatedAnnealing:
    def __init__(self, locs, level, maxTempature, minTempature, coolnum=0.95):
        self.locs = locs
        self.level = level
        self.coolnum = coolnum
        self.maxTempature = maxTempature
        self.minTempature = minTempature

    def _init_route(self):
        newlocs = copy.deepcopy(self.locs)
        rd.shuffle(newlocs)
        newRoute = Route(newlocs)
        self.route = newRoute
        return newRoute
    
    def annealing(self):
        t = self.maxTempature
        rt = self.coolnum
        last_route = self._init_route()

        while (t>self.minTempature) :
            for _ in range(self.level):
                new_route = copy.deepcopy(last_route)
                new_route._two_change()
                diff = new_route.distance - last_route.distance

                if(diff<=0):
                    last_route = new_route
                    
                else:
                    r = rd.uniform(0,1)
                    if(r <= exp(-diff/t)):
                        last_route = new_route
            t *= rt

        self.path = last_route
        return self.route.path, self.route.distance
    

def create_locations():
    locations = []
    xs = []
    ys = []
    cities = []
    f = open("SA/tsp_test")
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

if __name__ == '__main__':
    my_locs, xs, ys, cities = create_locations()
    my_algo = SimulatedAnnealing(my_locs, 40, 500, 0.1, 0.98)
    best_route, best_route_length = my_algo.annealing()
    best_route.append(best_route[0])
    print([loc.name for loc in best_route], best_route_length)
    print([(loc.loc[0], loc.loc[1]) for loc in best_route], best_route_length)
    fig, ax = plt.subplots()
    ax.plot([loc.loc[0] for loc in best_route], [loc.loc[1] for loc in best_route], 'red', linestyle='-', marker='')
    ax.scatter(xs, ys)
    for i, txt in enumerate(cities):
        ax.annotate(txt, (xs[i], ys[i]))
    plt.show()
