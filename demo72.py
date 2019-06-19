import functools
import graphviz as gv

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g5 = graph()
g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            pass
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            pass
        else:
            graph.edge(*e)
    return graph


import itertools

nodes1 = list('ABCD')
nodes2 = list('EFGH')
edges1 = [e for e in itertools.combinations(nodes1, 2)]
g3 = add_nodes(g3, nodes1)
g3 = add_edges(g3, edges1)
g5 = add_nodes(g3, nodes2)
g3.render('graph\\demo67_g3')
