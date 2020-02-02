from igraph import *
import cProfile
import sys

filename = sys.argv[1]
n = sys.argv[2]

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

cProfile.run(f'''for i in range({n}): g = Graph.Read(filename, format="edges")''')

print("Profiling shortest path")
print("=======================")
print()

cProfile.run(f"for i in range({n}): g.shortest_paths([g.vs[0]])", sort="cumulative")

print("Profiling PageRank")
print("==================")
print()

cProfile.run(f"for i in range({n}): g.pagerank(damping=0.85, eps=1e-3)", sort="cumulative")

print("Profiling k-core")
print("================")
print()

cProfile.run(f"for i in range({n}): g.coreness(mode='all')", sort="cumulative")

print("Profiling strongly connected components")
print("=======================================")
print()

cProfile.run(f"for i in range({n}): g.components(mode=STRONG)", sort="cumulative")