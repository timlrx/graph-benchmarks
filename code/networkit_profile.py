from networkit import *
from benchmark import benchmark
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

engineering.setNumberOfThreads(16)
print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

benchmark("readGraph(filename, Format.SNAP)", globals=globals(), n=n)
g = readGraph(filename, Format.SNAP)

print("Profiling shortest path")
print("=======================")
print()

benchmark("distance.BFS(g, 0, storePaths=False).run()", globals=globals(), n=n)

print("Profiling PageRank")
print("==================")
print()

benchmark("centrality.PageRank(g, damp=0.85, tol=1e-3).run()",
          globals=globals(), n=n)

print("Profiling k-core")
print("================")
print()

benchmark("centrality.CoreDecomposition(g).run()", globals=globals(), n=n)

print("Profiling strongly connected components")
print("=======================================")
print()

benchmark("components.StronglyConnectedComponents(g).run()",
          globals=globals(), n=n)
