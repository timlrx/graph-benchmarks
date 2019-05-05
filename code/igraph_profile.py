from igraph import *
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

print("Profiling loading")
print("=================")
print()

cProfile.run(f'''for i in range({n}): g = Graph.Read(f"../data/{file}", format="edges")''')

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