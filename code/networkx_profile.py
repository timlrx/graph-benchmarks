from networkx import *
from benchmark import benchmark
import sys

filename = sys.argv[1]
n = sys.argv[2]

if (filename == "pokec"):
    nodeid = '1'
else:
    nodeid = '0'

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

benchmark('read_edgelist(filename, delimiter="\t")', globals=globals(), n=n)
g = read_edgelist(filename, delimiter="\t")
g = g.to_directed()

print("Profiling 2-hops")
print("================")
print()

benchmark(
    f'single_source_shortest_path_length(g, "{nodeid}", cutoff=2)', globals=globals(), n=n)

print("Profiling shortest path")
print("=======================")
print()

benchmark(f'shortest_path_length(g, "{nodeid}")', globals=globals(), n=n)

print("Profiling PageRank")
print("==================")
print()

benchmark('pagerank(g, alpha=0.85, tol=1e-3, max_iter=10000000)',
          globals=globals(), n=n)

print("Profiling k-core")
print("================")
print()

benchmark('core.core_number(g)', globals=globals(), n=n)

print("Profiling strongly connected components")
print("=======================================")
print()

benchmark('[i for i in strongly_connected_components(g)]',
          globals=globals(), n=n)
