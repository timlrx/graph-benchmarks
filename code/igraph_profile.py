from igraph import *
from benchmark import benchmark
import sys

filename = sys.argv[1]
n = sys.argv[2]

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

benchmark("Graph.Read(filename, format='edges')", globals=globals(), n=n)
g = Graph.Read(filename, format='edges')

print("Profiling shortest path")
print("=======================")
print()

benchmark("g.shortest_paths([g.vs[0]])", globals=globals(), n=n)

print("Profiling PageRank")
print("==================")
print()

benchmark("g.pagerank(damping=0.85, eps=1e-3)", globals=globals(), n=n)

print("Profiling k-core")
print("================")
print()

benchmark("g.coreness(mode='all')", globals=globals(), n=n)

print("Profiling strongly connected components")
print("=======================================")
print()

benchmark("g.components(mode=STRONG)", globals=globals(), n=n)
