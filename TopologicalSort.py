from utility import points_graph_generator, depth_first_search

graph = points_graph_generator()


node = graph.undirected_nodes[0]
depth_first_search(node, 0)
print(node.is_marked())
for i in node.get_connections():
    print(i.is_marked())
    print(i.get_order())
