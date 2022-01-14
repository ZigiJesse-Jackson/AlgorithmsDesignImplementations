import numpy as np
from typing import List, Tuple, Generic, TypeVar, MutableSequence

T = TypeVar('T')


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


class UndirectedNode(Generic[T]):

    def __init__(self, value: T):
        self._data = value
        self._connections = []
        self._degrees = len(self._connections)
        self._marked = False
        self._order = 0

    def get_data(self) -> T:
        return self._data

    def get_edges(self) -> List[T]:
        return self._connections

    def is_marked(self) -> bool:
        return self._marked

    def mark_node(self):
        self._marked = True

    def get_degree(self):
        return self._degrees

    def set_order(self, pos: int):
        self._order = pos

    def get_order(self):
        return self._order

    def set_connections(self, connections: List[T]):
        self._connections = connections

    def get_connections(self):
        return self._connections

    def __eq__(self, other):
        return self._data == other._data

    def __str__(self):
        return f'{self._data}'

    def __hash__(self):
        return hash(self._data)


class UndirectedEdge(Generic[T]):

    def __init__(self, arr: UndirectedNode, dest: UndirectedNode):
        self.arr = arr
        self.dest = dest

    def set_arr(self, arr: UndirectedNode):
        self.arr = arr

    def set_dest(self, dest: UndirectedNode):
        self.dest = dest

    def __eq__(self, other):
        return self.arr == other.arr and self.dest == other.dest

    def __str__(self):
        return f'({self.arr}) -> ({self.dest})'

    def __hash__(self):
        return hash(self.arr) ^ hash(self.dest)


class UndirectedGraphNode:

    def __init__(self, nodes: List[UndirectedNode]):
        self.undirected_nodes = nodes

    def __eq__(self, other):
        return self.undirected_nodes == other.undirected_nodes


def depth_first_search(node: UndirectedNode, count: int = 0):
    node.mark_node()
    node.set_order(count)
    for i in node.get_connections():
        if not i.is_marked():
            count+=1
            depth_first_search(i, count)


"""
Function to create a list of random integers

args:
    size(int): size of list to be created

returns: 
    list of random integers
"""


def list_generator(size):
    return np.random.randint(low=1, high=1001, size=size)  # Generate uniform random numbers
    # from 1 to 1000


"""
Function to generate Point objects

args:
    length(int, optional): number of points to create

returns:
    list of Point objects

"""


def points_generator(length: int = 100) -> List[Point]:
    x_val = list_generator(length)
    y_val = list_generator(length)
    points = []
    for i in range(0, length):
        points.append(Point(x_val[i], y_val[i]))
    return points

"""
Function to generate an UndirectedGraphNode objected with each nodes _connections initialized

args:
    length(int): number of nodes to be created for UndirectedGraphNode 

returns:
    an UndirectedGraphNode object 
"""


def points_graph_generator(length: int = 100) -> UndirectedGraphNode:
    points = points_generator(length)
    nodes = []

    for i in points:
        nodes.append(UndirectedNode(i))

    for i in nodes:
        begin = np.random.randint(low=0, high=length / 2)
        end = np.random.randint(low=length / 2, high=length)
        # print(begin, end=', ' + str(end) +'\n')
        i.set_connections(nodes[begin:end])  # slicing nodes array to create a edges for each node

    return UndirectedGraphNode(nodes)


"""
Function to generate cartesian product of two lists of points

args:
    X(Point): a list of Point objects
    Y(Point): a list of Point objects


returns:
    list of Point objects which is the cartesian product of X and Y 

"""


def cartesian_product(X: List[Point], Y: List[Point]) -> List[Tuple[Point, Point]]:
    xLen = len(X)
    yLen = len(Y)
    cart_prod = []

    if (xLen or yLen) == 0:
        raise UserWarning("An empty list of Point objects given")

    for i in range(0, xLen):
        for j in range(0, yLen):
            element = (X[i], Y[j])
            cart_prod.append(element)
    return cart_prod


"""
Function to check which side a point falls given a line

args:
    line(tuple[Point]): a tuple of two Point objects to represent a line
    point(Point): a Point object

returns:
    int: 1 if point falls on right side, -1 if point falls on left side, 0 if point falls on line

"""


def side_line(line: Tuple[Point], point: Point) -> int:
    a = line[1].y - line[0].y
    b = line[0].x - line[1].x

    c = (line[0].x * line[1].y) - (line[0].y * line[1].x)

    if (a * point.x) + (b * point.y) > c:
        return 1  # on the right
    elif (a * point.x) + (b * point.y) < c:
        return -1  # on the left
    return 0
