#!/usr/bin/env julia
# Execute this with the JULIA_NUM_THREADS environment variable set to
# the number of threads on the machine.
#
# Prior to running, ensure all packages have been added. For
# LightGraphs, ensure that LightGraphs master has been added
# since we're using the new shortest paths syntax and a new
# core_number algorithm.
using BenchmarkTools
using LightGraphs, LightGraphs.ShortestPaths, LightGraphs.Centrality
using LightGraphs.Traversals: BreadthFirst, ThreadedBreadthFirst, distances
using LightGraphs.ShortestPaths: shortest_paths, BFS, ThreadedBFS
using LightGraphs.Centrality: centrality, PageRank, ThreadedPageRank
using LightGraphs.Degeneracy: core_number, KabirMadduri
using LightGraphs.Connectivity: connected_components, Kosaraju

using GraphIO
using SortingAlgorithms: RadixSort
f = ARGS[1]
n = parse(Int, ARGS[2])

println("using $(Base.Threads.nthreads()) threads")

println("loadgraph")
# we use @time here because we only want a single sample, and we want
# to keep the result. 
@time g = squash(loadgraph(f, GraphIO.EdgeList.EdgeListFormat()))
println("loaded $g")
println("\n")

println("shortest paths: with path data")
show(stdout, MIME"text/plain"(), @benchmark b = shortest_paths($g, 1, BFS(RadixSort)) samples = n seconds = 300)
println("\n")

println("shortest paths: threaded, with path data")
show(stdout, MIME"text/plain"(), @benchmark b = shortest_paths($g, 1, ThreadedBFS()) samples = n seconds = 300)
println("\n")

println("shortest paths: distances only")
show(stdout, MIME"text/plain"(), @benchmark b = distances($g, 1, BreadthFirst(sort_alg=RadixSort)) samples = n seconds = 300)
println("\n")

println("shortest paths: threaded, distances only")
show(stdout, MIME"text/plain"(), @benchmark b = distances($g, 1, ThreadedBreadthFirst()) samples = n seconds = 300)
println("\n")

println("pagerank")
show(stdout, MIME"text/plain"(), @benchmark centrality($g, PageRank(0.85, 10000000, 1e-3)) samples = n seconds = 300)
println("\n")

# note: this might not be as performant because BLAS is inherently multi-threaded.
println("pagerank: threaded")
show(stdout, MIME"text/plain"(), @benchmark centrality($g, ThreadedPageRank(0.85, 10000000, 1e-3)) samples = n seconds = 300)
println("\n")

println("core_number")
show(stdout, MIME"text/plain"(), @benchmark core_number($g) samples = n seconds = 300)
println("\n")

println("core_number: threaded")
show(stdout, MIME"text/plain"(), @benchmark core_number($g, KabirMadduri()) samples = n seconds = 300)
println("\n")

println("scc: Tarjan")
show(stdout, MIME"text/plain"(), @benchmark connected_components($g) samples = n seconds = 300)
println("\n")
