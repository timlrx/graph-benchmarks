# Benchmark of popular graph / network packages

A comparison of 5 different packages:

- [NetworkX](https://networkx.github.io/), v2.3, Python 3.7
- [graph-tool](https://graph-tool.skewed.de/static/doc/quickstart.html), v2.28.dev0, Python 3.7
- [Igraph](https://igraph.org/python/), v0.7.1, Python 3.7
- [NetworKit](https://networkit.github.io/), v5.0.1, Python 3.7
- [SNAP](https://snap.stanford.edu/snap/), v4.1.0, Python 2.7
- [LightGraphs](https://juliagraphs.github.io/LightGraphs.jl/latest/), v1.3.0 dev, Julia 1.3

For a more detailed description of the process and results, please refer to the following [blog post](https://www.timlrx.com/2019/05/05/benchmark-of-popular-graph-network-packages/).  
**Note**: The post has not been updated with the latest lightgraphs benchmark

## Results

The benchmark was run using Google's Compute n1-standard-16 instance (16vCPU Haswell 2.3GHz, 60 GB memory).

Each algorithm was run 100 times on the Amazon and Google dataset and 10 times on the Pokec dataset (except networkx).

The average run time is shown in the table below. Due to differences in profiling techniques and possibly code implementation, the results of the algorithms may differ. Please refer to the respective code bases for implementation details.

| dataset | algorithm            | graph-tool | igraph | networkit | networkx | snap  | lightgraphs |
| ------- | -------------------- | ---------- | ------ | --------- | -------- | ----- | ----------- |
| Amazon  | connected components | 0.09       | 0.48   | 0.21      | 5.94     | 0.40  | 0.099       |
| Amazon  | k-core number        | 0.11       | 0.33   | 0.01      | 8.62     | 0.42  | 0.43        |
| Amazon  | loading              | 5.00       | 0.79   | 3.27      | 9.96     | 1.90  | 5.34        |
| Amazon  | page rank            | 0.05       | 1.59   | 0.01      | 25.71    | 0.90  | 0.019       |
| Amazon  | shortest path        | 0.06       | 0.12   | 0.32      | 3.31     | 0.14  | 0.029       |
| Google  | connected components | 0.32       | 2.23   | 0.65      | 21.71    | 2.02  | 0.38        |
| Google  | k-core number        | 0.57       | 1.68   | 0.06      | 153.21   | 1.57  | 1.98        |
| Google  | loading              | 67.27      | 5.51   | 17.94     | 39.69    | 9.03  | 17.96       |
| Google  | page rank            | 0.76       | 5.24   | 0.12      | 106.49   | 4.16  | 0.075       |
| Google  | shortest path        | 0.20       | 0.69   | 0.98      | 12.33    | 0.30  | 0.093       |
| Pokec   | connected components | 1.35       | 17.75  | 4.69      | 108.07   | 15.28 | 1.57        |
| Pokec   | k-core number        | 5.73       | 10.87  | 0.34      | 649.81   | 8.87  | 11.11       |
| Pokec   | loading              | 119.57     | 34.53  | 157.61    | 237.72   | 59.75 | 167.19      |
| Pokec   | page rank            | 1.74       | 59.55  | 0.20      | 611.24   | 19.52 | 0.49        |
| Pokec   | shortest path        | 0.86       | 0.87   | 6.87      | 67.15    | 3.09  | 0.26        |

## Setup

Setup and installation instructions can be found in `setup.md`.

Datasets are downloaded from https://snap.stanford.edu/data/ and is stored in the data folder. Amazon refers to [amazon0302](https://snap.stanford.edu/data/amazon0302.html), google to [web-Google](https://snap.stanford.edu/data/web-Google.html) and pokec to [soc-Pokec](https://snap.stanford.edu/data/soc-Pokec.html). Comments (if any) were removed from the datasets prior to loading.

Profiling codes are located in the code folder. A particular benchmark code can be run using the helper bash script `run_profiler.sh [profiling code] [dataset path] [number of repetitions] [output path]`. For example, to replicate the igraph benchmark on the amazon dataset just run `run_profiler.sh code/igraph_profile.py data/amazon0302.txt 100 output/igraph_amazon.txt`.
