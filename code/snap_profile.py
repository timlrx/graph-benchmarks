import snap
from benchmark import benchmark
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

benchmark("snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)",
          globals=globals(), n=n)
g = snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)

print("Profiling 2-hops")
print("================")
print()

NodeVec = snap.TIntV()
benchmark("snap.GetNodesAtHop(g, 0, 2, NodeVec, True)", globals=globals(), n=n)

print("Profiling shortest path")
print("=======================")
print()

NIdToDistH = snap.TIntH()
benchmark("snap.GetShortPath(g, 0, NIdToDistH, True)", globals=globals(), n=n)

print("Profiling PageRank")
print("==================")
print()

PRankH = snap.TIntFltH()
benchmark("snap.GetPageRank(g, PRankH, 0.85, 1e-3, 10000000)",
          globals=globals(), n=n)

print("Profiling k-core")
print("================")
print()

CoreIDSzV = snap.TIntPrV()
benchmark("snap.GetKCoreNodes(g, CoreIDSzV)", globals=globals(), n=n)

print("Profiling strongly connected components")
print("=======================================")
print()

Components = snap.TCnComV()
benchmark("snap.GetSccs(g, Components)", globals=globals(), n=n)
