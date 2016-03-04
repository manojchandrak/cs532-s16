from igraph import *
graph =load('karate.GraphML')
graph.vs["label"] = graph.vs["name"]
mylayout = graph.layout("kk")
plot(graph, 'graph5.pdf', layout = mylayout)
while len(graph.clusters()) < 5:
    edgeBtw = graph.edge_betweenness()
    maxEdgeBtw = max(edgeBtw)
    indexEdgeMaxBtwness = max(xrange(len(edgeBtw)), key = edgeBtw.__getitem__) 
    graph.delete_edges(indexEdgeMaxBtwness)
layout = graph.layout("kk")
plot(graph, 'finalgraph5.pdf' , layout = layout)