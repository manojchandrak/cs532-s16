from igraph import *
#loads a graphML file
graph =load('karate.GraphML')
#labels a graph with name
graph.vs["label"] = graph.vs["name"]
#assigning a layout to the graph
mylayout = graph.layout("kk")
#Array of colors
color_dict = {1: "blue", 2: "pink"}
#plotting the original graph before seperation 
plot(graph, 'graphkk.pdf', layout = mylayout, vertex_color = [color_dict[faction] for faction  in graph.vs["Faction"]])
print 'Removed Edges \n '
#looping until you get two clusters 
while len(graph.clusters()) < 2 :
	#edge betweenness 
    ebs = graph.edge_betweenness()
    max_eb = max(ebs)
    #finding the index of edge which has maximum edge betweenness
    indexEdgeMaxBtwness = max(xrange(len(ebs)), key = ebs.__getitem__)
    #deleting the edges with maximum edge betweenness
    graph.delete_edges(indexEdgeMaxBtwness)
    print indexEdgeMaxBtwness
#assigning another layout to the final graph
layout = graph.layout("kk")
#plotting the final graph
plot(graph, 'finalgraph.pdf' , layout = layout)