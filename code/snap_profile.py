import sys
sys.path.append('snap-4.1.0-4.1-centos6.5-x64-py2.6')
import snap
import cProfile

filename = sys.argv[1]
n = int(sys.argv[2])

print("Profiling dataset {}".format(filename))

print("Profiling loading")
print("=================")
print()

cProfile.run('''for i in range({}): g = snap.LoadEdgeListStr(snap.PNGraph, "{}", 0, 1)'''.format(n, filename))

print("Profiling 2-hops")
print("================")
print()

NodeVec = snap.TIntV()
cProfile.run("for i in range({}): snap.GetNodesAtHop(g, 0, 2, NodeVec, True)".format(n), sort="cumulative")

print("Profiling shortest path")
print("=======================")
print()

NIdToDistH = snap.TIntH()
cProfile.run("for i in range({}): snap.GetShortPath(g, 0, NIdToDistH, True)".format(n), sort="cumulative")

print("Profiling PageRank")
print("==================")
print()

PRankH = snap.TIntFltH()
cProfile.run("for i in range(n): snap.GetPageRank(g, PRankH, 0.85, 1e-3, 10000000)".format(n), sort="cumulative")

print("Profiling k-core")
print("================")
print()

CoreIDSzV = snap.TIntPrV()
cProfile.run("for i in range(n): snap.GetKCoreNodes(g, CoreIDSzV)".format(n), sort="cumulative")

print("Profiling strongly connected components")
print("=======================================")
print()

Components = snap.TCnComV()
cProfile.run("for i in range(n): snap.GetSccs(g, Components)".format(n), sort="cumulative")