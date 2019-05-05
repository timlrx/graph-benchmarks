# Benchmark of popular graph / network packages

A comparison of 5 different packages:
- graph-tool
- igraph
- networkit
- networkx
- snap

Benchmark was run using Google Compute n1-standard-16 instance (16vCPU Haswell 2.3GHz, 60 GB memory).

Setup and installation instructions can be found in `setup.md`.

Datasets are downloaded from https://snap.stanford.edu/data/ and is stored in the data folder. Amazon refers to [amazon0302](https://snap.stanford.edu/data/amazon0302.html), google to [web-Google](https://snap.stanford.edu/data/web-Google.html) and pokec to [soc-Pokec](https://snap.stanford.edu/data/soc-Pokec.html). Comments (if any) were removed from the datasets prior to loading.

Benchmark codes are located in the code folder. To replicate the analysis run `bash run_profiler.sh`. To replicate one of the benchmarks e.g. igraph on the amazon dataset just run `python igraph_profile.py 100 amazon` where the first argument is the number of repetitions and the second argument is the dataset.

Results are stored in the output folder.
