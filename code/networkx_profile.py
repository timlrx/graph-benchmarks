from networkx import *
import cProfile
import sys

filename = sys.argv[1]
n = sys.argv[2]

if (filename=="pokec"):
    nodeid = '1'
else:
    nodeid = '0'

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

cProfile.run(f'''for i in range({n}): g = read_edgelist(filename, delimiter="\t")''')
g = g.to_directed()

print("Profiling 2-hops")
print("================")
print()

cProfile.run(f"for i in range({n}): nx.single_source_shortest_path_length(g, '{nodeid}', cutoff=2)", sort="cumulative")

print("Profiling shortest path")
print("=======================")
print()

cProfile.run(f"for i in range({n}): shortest_path_length(g, '{nodeid}')", sort="cumulative")

print("Profiling PageRank")
print("==================")
print()

cProfile.run(f"for i in range({n}): pagerank(g, alpha=0.85, tol=1e-3, max_iter=10000000)", sort="cumulative")

print("Profiling k-core")
print("================")
print()

cProfile.run(f"for i in range({n}): core.core_number(g)", sort="cumulative")

print("Profiling strongly connected components")
print("=======================================")
print()

cProfile.run(f"for i in range({n}): [i for i in strongly_connected_components(g)]", sort="cumulative")