from igraph import *
graph =load('karate.GraphML')
graph.vs["label"] = graph.vs["name"]
mylayout = graph.layout("kk")
plot(graph, 'graph4.pdf', layout = mylayout)
while len(graph.clusters()) < 4:
    ebs = graph.edge_betweenness()
    max_eb = max(ebs)
    max_idx = max(xrange(len(ebs)), key = ebs.__getitem__) 
    graph.delete_edges(max_idx)
layout = graph.layout("kk")
plot(graph, 'finalgraph4.pdf' , layout = layout)