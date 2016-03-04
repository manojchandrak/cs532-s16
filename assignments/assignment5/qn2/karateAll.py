from igraph import *
graph =load('karate.GraphML')
graph.vs["label"] = graph.vs["name"]
mylayout = graph.layout("kk")
plot(graph, 'graph1.pdf', layout = mylayout)
print 'Index of removed Edges for forming 3 clusters  \n '
while len(graph.clusters()) < 3 :
    edgeBtw = graph.edge_betweenness()
    maxEdgeBtw = max(edgeBtw)
    indexEdgeMaxBtwness = max(xrange(len(edgeBtw)), key = edgeBtw.__getitem__)
    print indexEdgeMaxBtwness 
    graph.delete_edges(indexEdgeMaxBtwness)
    
layout = graph.layout("kk")
plot(graph, 'finalgraph3.pdf' , layout = layout)
print 'Index of removed Edges for forming 4 clusters  \n '
while len(graph.clusters()) < 4:
    edgeBtw = graph.edge_betweenness()
    maxEdgeBtw = max(edgeBtw)
    indexEdgeMaxBtwness = max(xrange(len(edgeBtw)), key = edgeBtw.__getitem__)
    print indexEdgeMaxBtwness 
    graph.delete_edges(indexEdgeMaxBtwness)
    
layout = graph.layout("kk")
plot(graph, 'finalgraph4.pdf' , layout = layout)
print 'Index of removed Edges for forming 5 clusters  \n '
while len(graph.clusters()) < 5:
    edgeBtw = graph.edge_betweenness()
    maxEdgeBtw = max(edgeBtw)
    indexEdgeMaxBtwness = max(xrange(len(edgeBtw)), key = edgeBtw.__getitem__)
    print indexEdgeMaxBtwness 
    graph.delete_edges(indexEdgeMaxBtwness)
layout = graph.layout("kk")
plot(graph, 'finalgraph5.pdf' , layout = layout)