# !/usr/bin/env julia
#
# Prior to running, ensure all packages have been added. For
# LightGraphs, ensure that LightGraphs master has been added
# since we're using the new shortest paths syntax and a new
# core_number algorithm.
using BenchmarkTools
using LightGraphs, LightGraphs.Experimental.ShortestPaths
using GraphIO
using SortingAlgorithms: RadixSort
f = ARGS[1]
n = parse(Int, ARGS[2])

println("loadgraph")
# we use @time here because we only want a single sample, and we want
# to keep the result. 
@time g = squash(loadgraph(f, GraphIO.EdgeList.EdgeListFormat()))
println("loaded $g")
println("\n")

println("shortest paths")
show(stdout, MIME"text/plain"(), @benchmark b = shortest_paths($g, 1, BFS(RadixSort)) samples = n seconds = 300)
println("\n")

println("pagerank")
show(stdout, MIME"text/plain"(), @benchmark pagerank($g, 0.85, 10000000, 1e-3) samples = n seconds = 300)
println("\n")

println("core_number")
show(stdout, MIME"text/plain"(), @benchmark core_number($g) samples = n seconds = 300)
println("\n")

println("scc")
show(stdout, MIME"text/plain"(), @benchmark strongly_connected_components($g) samples = n seconds = 300)
println("\n")
