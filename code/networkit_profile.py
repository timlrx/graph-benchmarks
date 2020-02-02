from networkit import *
import cProfile
import sys

filename = sys.argv[1]
n = sys.argv[2]

engineering.setNumberOfThreads(16)
print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

cProfile.run(f'''for i in range({n}): g = readGraph(filename, Format.SNAP)''')

print("Profiling shortest path")
print("=======================")
print()

cProfile.run(f"for i in range({n}): distance.BFS(g, 0).run()", sort="cumulative")

print("Profiling PageRank")
print("==================")
print()

cProfile.run(f"for i in range({n}): centrality.PageRank(g, damp=0.85, tol=1e-3).run()", sort="cumulative")

print("Profiling k-core")
print("================")
print()

cProfile.run(f"for i in range({n}): centrality.CoreDecomposition(g).run()", sort="cumulative")

print("Profiling strongly connected components")
print("=======================================")
print()

cProfile.run(f"for i in range({n}): components.StronglyConnectedComponents(g).run()", sort="cumulative")
