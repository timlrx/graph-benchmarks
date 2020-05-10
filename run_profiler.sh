#!/bin/bash
# Takes in 4 arguments: code path, data input, number of runs, output path
# Example:
#   run_profiler.sh "code/graphtool_profile.py" "data/email-Enron.txt" 10 "output/test_results.txt"

CODE=$1
INPUT=$2
N=$3
OUTPUT=$4

eval "$(conda shell.bash hook)" # https://stackoverflow.com/questions/34534513/calling-conda-source-activate-from-bash-script

if [[ $CODE == *"graphtool"* ]]; then
    conda activate graphtool
    echo profiling graphtool on $2...
    python $CODE $INPUT $N > $OUTPUT
elif [[ $CODE == *"snap"* ]]; then
    conda activate snap
    echo profiling snap on $2...
    python $CODE $INPUT $N > $OUTPUT
elif [[ $CODE == *"igraph"* ]]; then
    conda activate igraph
    echo profiling igraph on $2...
    python $CODE $INPUT $N > $OUTPUT
elif [[ $CODE == *"networkit"* ]]; then
    conda activate networkit
    echo profiling networkit on $2...
    python $CODE $INPUT $N > $OUTPUT
elif [[ $CODE == *"networkx"* ]]; then
    conda activate networkx
    echo profiling networkx on $2...
    python $CODE $INPUT $N > $OUTPUT
elif [[ $CODE == *"lightgraphs"* ]]; then
    echo profiling lightgraphs on $2...
    JULIA_NUM_THREADS=16 julia --depwarn=no $CODE $INPUT $N > $OUTPUT
else
    echo "Unknown code"
fi