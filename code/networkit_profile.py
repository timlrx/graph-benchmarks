from networkit import *
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

engineering.setNumberOfThreads(16)
print(f"Profiling dataset {file}")

print("Profiling loading")
print("=================")
print()

cProfile.run(f'''for i in range({n}): g = readGraph(f"../data/{file}", Format.SNAP)''')

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
