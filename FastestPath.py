import sys
from utility import MatrixGraph

"""
Function to read file in format 
    N M D
    X Y V L
    X Y V L
    ...
    X Y V L
    
    where N is number of cities, M is number of roads, D is destination city for
    computation of fastest path to D
    L is the lenth of the road in km from city X to city L with speed limit V km/h

args:
    filename(str): file name as string


returns: a list containing a matrix graph from file content, a dict of speed limits
            from file content, and the destination city (an integer)

"""


def read_file_to_Graph(filename: str) -> list:
    # opening file
    with open(filename) as file:
        # reading first line to read in number of cities,
        # roads and destination city for djikstra's algorithm
        first_line = file.readline().split()

        # creating graph to be returned
        graph = MatrixGraph(int(first_line[0]))
        # getting destination city to compute fastest path
        dest_city = first_line[2]
        # speed limits in file to be returned
        speed_limits = dict()

        # remaining content in file is of format <X, Y, V, L> where
        # X is the source city, Y is the destination city
        # V is the speed limit on the road connecting said cities in km/h
        # L is the length of the road in km
        paths = file.readlines()
        for path in paths:
            path = path.split(' ')
            path = [int(i) for i in path]
            src, dest, speed_lmt, dist = path[0], path[1], path[2], path[3]
            # putting in graph the distance value from src to dest
            graph.put(src, dest, dist)
            # creating key to hold speed limit of road from src to dest
            pos = (src, dest)
            # storing speed limit in dictionary
            speed_limits[pos] = speed_lmt
        return [graph, speed_limits, dest_city]


"""
Function 

args:
    filename(str): file name as string


returns: a list containing a matrix graph from file content, a dict of speed limits
            from file content, and the destination city (an integer)

"""


def find_shortest_paths(graph: MatrixGraph, speed_limits: dict, dest: int):
    # Initialization phase
    # contains set of cities with least cost already computed
    set_cities = {0}

    # path to dest
    path_to_dest = [0]

    # starting speed is 70km/h
    curr_speed = 70
    # the distance covered from city 0 to Distance_to[x] as (road distance / curr_speed)
    Distance_to = dict()

    for city in range(graph.matrix_size):
        # city is source city 0
        if city == 0:
            Distance_to[0] = 0
        # neighbouring cities to source city 0
        elif graph.get(0, city) != sys.maxsize:
            # if there is no speed limit, divide length of road by curr_speed
            # else divide by speed limit on that road
            Distance_to[city] = graph.get(0, city) / curr_speed if \
                speed_limits[(0, city)] == 0 \
                else graph.get(0, city) / speed_limits[(0, city)]
        # cities not neighbouring source city 0
        else:
            Distance_to[city] = sys.maxsize

    # Computation phase

    # speed_limits = dict(sorted(speed_limits.items(), key=lambda item: item[1]))

    while graph.matrix_size > len(set_cities):
        # get next city with min cost not yet in set
        curr_min = get_min_not_in_set(Distance_to, set_cities)
        # add said city to set
        set_cities.add(curr_min)
        # get said city's neighbours
        curr_min_neighbours = get_neighbours(curr_min, graph)
        # for each neighbour to city not in set, compute whether
        # we can reduce its current cost
        for neighbour in curr_min_neighbours:
            if neighbour not in set_cities:
                # if speed_limit on road from curr_min to neighbour is 0, the speed limit currently on
                curr_speed = curr_speed if speed_limits[(curr_min, neighbour)] == 0 else speed_limits[
                    (curr_min, neighbour)]
                # computing whether a lesser cost can be assigned to neighbor
                Distance_to[neighbour] = min(Distance_to[neighbour],
                                             (Distance_to[curr_min] +
                                              (graph.get(curr_min, neighbour) / curr_speed)))
                # for the purpose of tracing path to destination city
                # if neighbour to curr_min city is dest city, curr_min city is added to paths
                # because it is a path that will be traversed to get the least cost path to dest city
                # this is because the least cost path to dest city has not yet been computed i.e. dest
                # city has not yet been added to set_cities with already computed least costs
                if neighbour == int(dest):
                    path_to_dest.append(curr_min)
    path_to_dest.append(int(dest))
    return path_to_dest


"""
Function to get neighbours of a vertex in MatrixGraph in utility.py

args:
    src(int): vertex to find neighbours of
    graph(MatrixGraph): MatrixGraph to perform neighbor search for src


returns: a list containing the neighbours of vertex src

"""


def get_neighbours(src: int, graph: MatrixGraph):
    if src > graph.matrix_size:
        raise UserWarning("vertex out of bounds")
    neighbours = []
    for dest in range(graph.matrix_size):
        if graph.get(src, dest) != sys.maxsize:
            neighbours.append(dest)
    return neighbours


"""
Function to get key with minimum value in a set

args:
    costs(dict): should contain the cost values of items in set
    tree_set(set): should contain the keys of the costs dictionary


returns: key with the minimum value in tree_set

"""


def get_min_not_in_set(costs: dict, tree_set: set):
    min = sys.maxsize
    key: int
    for i in costs.keys():
        if i not in tree_set and costs[i] < min:
            min = costs[i]
            key = i
    return key
