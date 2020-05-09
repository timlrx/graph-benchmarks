from graph_tool.all import *
from benchmark import benchmark
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

openmp_set_num_threads(16)

print(f"Profiling dataset {filename}")
print(f"using {openmp_get_num_threads()} threads")

print("Profiling loading")
print("=================")
print()

benchmark(
    '''load_graph_from_csv(filename, directed=True, csv_options={'delimiter': '\t', 'quotechar': '"'})''', globals=globals(), n=n)
g = load_graph_from_csv(filename, directed=True, csv_options={
                        'delimiter': '\t', 'quotechar': '"'})

print("Profiling 2-hops")
print("================")
print()

benchmark(
    "shortest_distance(g, g.vertex(0), max_dist=2)", globals=globals(), n=n)

print("Profiling shortest path")
print("=======================")
print()

benchmark("shortest_distance(g, g.vertex(0))", globals=globals(), n=n)

print("Profiling PageRank")
print("==================")
print()

benchmark('pagerank(g, damping=0.85, epsilon=1e-3, max_iter=10000000)',
          globals=globals(), n=n)

print("Profiling k-core")
print("================")
print()

benchmark('kcore_decomposition(g)', globals=globals(), n=n)

print("Profiling strongly connected components")
print("=======================================")
print()

benchmark('label_components(g, vprop=None, directed=None, attractors=False)',
          globals=globals(), n=n)
