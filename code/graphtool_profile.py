from graph_tool.all import *
import cProfile
import sys

n = sys.argv[1]
filename = sys.argv[2]

if (filename=="amazon"):
    file="amazon0302.txt"
elif (filename=="google"):
    file="web-Google.txt"
elif (filename=="pokec"):
    file="soc-pokec-relationships.txt"
else:
    file="email-Enron.txt"

print(f"Profiling dataset {file}")

openmp_set_num_threads(16)

print("Profiling loading")
print("=================")
print()

cProfile.run(f'''for i in range({n}): g = load_graph_from_csv('../data/{file}', directed=False, csv_options={{'delimiter': '\t', 'quotechar': '"'}})''')

print("Profiling 2-hops")
print("================")
print()

cProfile.run(f"for i in range({n}): shortest_distance(g, g.vertex(0), max_dist=2)", sort="cumulative")

print("Profiling shortest path")
print("=======================")
print()

cProfile.run(f"for i in range({n}): shortest_distance(g, g.vertex(0))", sort="cumulative")

print("Profiling PageRank")
print("==================")
print()

cProfile.run(f"for i in range({n}): pagerank(g, damping=0.85, epsilon=1e-3, max_iter=10000000)", sort="cumulative")

print("Profiling k-core")
print("================")
print()

cProfile.run(f"for i in range({n}): kcore_decomposition(g)", sort="cumulative")

print("Profiling strongly connected components")
print("=======================================")
print()

cProfile.run(f"for i in range({n}): label_components(g, vprop=None, directed=None, attractors=False)", sort="cumulative")