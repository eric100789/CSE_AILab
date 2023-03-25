import random as rd
import copy
from matplotlib import pyplot as plt

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
    def next_gen(self):
        self.age += 1
        return self

class GeneticAlgo:
    def __init__(self, locs, level=10, populations=100, variant=3, mutate_percent=0.01, elite_save_percent=0.1):
        self.locs = locs
        self.level = level
        self.variant = variant
        self.populations = populations
        self.mutates = int(populations * mutate_percent)
        self.elite = int(populations * elite_save_percent)

    def _find_path(self):
        locs_copy = copy.deepcopy(self.locs)
        rd.shuffle(locs_copy)
        return Route(locs_copy)

    def _init_routes(self):
        routes = []
        for _ in range(self.populations):
            routes.append(self._find_path())
        return routes

    def _get_next_route(self, routes):
        routes.sort(key=lambda x: x.distance, reverse=False)
        elites = routes[:self.elite]
        crossovers = self._crossover(elites)
        crossovers.extend(elites)
        next_routes = crossovers
        next_routes = [*map(lambda this: this.next_gen() , next_routes)]
        return next_routes

    def _crossover(self, elites):
        normal_breeds = []
        mutate_breeds = []
        elites = [*filter(lambda this: this.age <= 5, elites)]
        elites_num = len(elites)

        while elites_num < self.populations - self.mutates:
            elites_num += 1
            father, mother = rd.choices(elites[:4], k=2)
            father = copy.deepcopy(father.path)
            mother = copy.deepcopy(mother.path)
            father_start = rd.randint(0,len(father)-1)
            father_chrom = []
            for i in range(self.variant):
                picked = father[(i+father_start)%len(father)]
                father_chrom.append(picked)
                for j in range(len(mother)):
                    if(mother[j].name == picked.name):
                        del mother[j]
                        break
            mother_start = rd.randint(0,len(mother))
            for i,j in enumerate(father_chrom):
                mother.insert(mother_start+i,j)
            cross_normal = Route(mother)
            normal_breeds.append(cross_normal)

            gene1, gene2 = rd.sample(range(len(mother)), 2)
            m = copy.deepcopy(mother)
            m[gene1], m[gene2] = m[gene2], m[gene1]
            cross_mutate = Route(m)
            mutate_breeds.append(cross_mutate)
        return normal_breeds + rd.choices(mutate_breeds, k=self.mutates)

    def evolution(self):
        routes = self._init_routes()
        for _ in range(self.level):
            routes = self._get_next_route(routes)
        routes.sort(key=lambda x: x.distance)
        return routes[0].path, routes[0].distance

def create_locations():
    locations = []
    xs = []
    ys = []
    cities = []
    f = open("GA/tsp_test")
    try:
        while True:
            s = f.readline().split()
            xs.append(int(s[1]))
            ys.append(int(s[2]))
            cities.append(str(s[0]))
    except:
        f.close()
        pass
    for x, y, name in zip(xs, ys, cities):
        locations.append(Location(name, x, y))
    return locations, xs, ys, cities

if __name__ == '__main__':
    RUN_TIMES = 10
    my_locs, xs, ys, cities = create_locations()
    for _ in range(RUN_TIMES):
        my_algo = GeneticAlgo(my_locs, level=200, populations=150, variant=2, mutate_percent=0.01, elite_save_percent=0.15)
        best_route, best_route_length = my_algo.evolution()
        best_route.append(best_route[0])
        print([loc.name for loc in best_route], best_route_length)
        print([(loc.loc[0], loc.loc[1]) for loc in best_route], best_route_length)
        fig, ax = plt.subplots()
        ax.plot([loc.loc[0] for loc in best_route], [loc.loc[1] for loc in best_route], 'red', linestyle='-', marker='')
        ax.scatter(xs, ys)
        for i, txt in enumerate(cities):
            ax.annotate(txt, (xs[i], ys[i]))
        with open("GA/result.txt","a") as f:
            f.write(str(best_route_length)+"\n")
    plt.show()