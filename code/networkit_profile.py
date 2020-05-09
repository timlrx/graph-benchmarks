import networkit as nk
from benchmark import benchmark
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

nk.engineering.setNumberOfThreads(16)

if ("pokec" in filename):
    nodeid = 1
else:
    nodeid = 0

print(f"Profiling dataset {filename}")
print(f"using {nk.getCurrentNumberOfThreads()} threads")

print("Profiling loading")
print("=================")
print()

benchmark("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True, directed =True).read(filename)", globals=globals(), n=n)
g = nk.graphio.EdgeListReader(
    separator="\t", firstNode=nodeid, continuous=True, directed=True).read(filename)

print("Profiling shortest path")
print("=======================")
print()

benchmark("nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)",
          globals=globals(), n=n)

print("Profiling PageRank")
print("==================")
print()

benchmark("nk.centrality.PageRank(g, damp=0.85, tol=1e-3).run().scores()",
          globals=globals(), n=n)

print("Profiling k-core")
print("================")
print()

benchmark("nk.centrality.CoreDecomposition(g).run().scores()",
          globals=globals(), n=n)

print("Profiling strongly connected components")
print("=======================================")
print()

benchmark("nk.components.StronglyConnectedComponents(g).run().getPartition().getVector()",
          globals=globals(), n=n)
