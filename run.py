# Search methods

import search

ab = search.GPSProblem('F', 'G', search.romania) 

print "Busqueda en anchura"
print search.breadth_first_graph_search(ab).path() #Anchura

print "Busqueda en Profundidad"
print search.depth_first_graph_search(ab).path()   #Profundidad

print "Busqueda ramificacion y acotacion"
print search.ramificacion_acotacion_graph_search(ab).path() #Ramificacion y acotacion.

print "Busqueda ramificacion y acotacion con subestimacion" #Ramificacion y acotacion con subestimacion
print search.ramificacion_subestimacion_graph_search(ab).path()

#print search.depth_limited_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
