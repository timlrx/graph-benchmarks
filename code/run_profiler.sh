#!/bin/bash
# Amazon
source /home/timothy_lin/miniconda3/bin/activate graphtool
echo profiling graphtool...
python graphtool_profile.py 100 amazon > /home/timothy_lin/output/graphtool_amazon.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate snap
echo profiling snap...
python snap_profile.py 100 amazon > /home/timothy_lin/output/snap_amazon.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate igraph
echo profiling igraph...
python igraph_profile.py 100 amazon > /home/timothy_lin/output/igraph_amazon.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate networkit
echo profiling networkit...
python networkit_profile.py 100 amazon > /home/timothy_lin/output/networkit_amazon.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate networkx
echo profiling networkx...
python networkx_profile.py 10 amazon > /home/timothy_lin/output/networkx_amazon.txt
source /home/timothy_lin/miniconda3/bin/deactivate

# Google
source /home/timothy_lin/miniconda3/bin/activate graphtool
echo profiling graphtool...
python graphtool_profile.py 100 google > /home/timothy_lin/output/graphtool_google.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate snap
echo profiling snap...
python snap_profile.py 100 google > /home/timothy_lin/output/snap_google.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate igraph
echo profiling igraph...
python igraph_profile.py 100 google > /home/timothy_lin/output/igraph_google.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate networkit
echo profiling networkit...
python networkit_profile.py 100 google > /home/timothy_lin/output/networkit_google.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate networkx
echo profiling networkx...
python networkx_profile.py 10 google > /home/timothy_lin/output/networkx_google.txt
source /home/timothy_lin/miniconda3/bin/deactivate

# Pokec
source /home/timothy_lin/miniconda3/bin/activate graphtool
echo profiling graphtool...
python graphtool_profile.py 10 pokec > /home/timothy_lin/output/graphtool_pokec.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate snap
echo profiling snap...
python snap_profile.py 10 pokec > /home/timothy_lin/output/snap_pokec.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate igraph
echo profiling igraph...
python igraph_profile.py 10 pokec > /home/timothy_lin/output/igraph_pokec.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate networkit
echo profiling networkit...
python networkit_profile.py 10 pokec > /home/timothy_lin/output/networkit_pokec.txt
source /home/timothy_lin/miniconda3/bin/deactivate

source /home/timothy_lin/miniconda3/bin/activate networkx
echo profiling networkx...
python networkx_profile.py 1 pokec > /home/timothy_lin/output/networkx_pokec.txt
source /home/timothy_lin/miniconda3/bin/deactivate
