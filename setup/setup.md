# Setup and Installation Guide

Configuration based on an Ubuntu 16.04 Google Compute VM. To bootstrap the setup, one can set up a virtual machine on Google Cloud Platform using `startup.sh` as a startup script. To install a specific package, follow the instructions below.

Where possible, most of the installations were done using conda / pip. As of 2020, all the Python packages tested supports Python 3.

Due to the different requirements of each package, we create seperate virtual environments for each installation.

### Install Miniconda and Julia (for LightGraphs)

Follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04) guide but use miniconda instead of an anaconda installer. The installer can be found [here](https://docs.conda.io/en/latest/miniconda.html)

Similarly download the latest release from [Julia's website](https://julialang.org/download/)

### Installing graph-tool

```
conda create --name graphtool
conda activate graphtool
conda install -y -c conda-forge graph-tool
```

### Installing igraph

```
conda create --name igraph
conda activate igraph
conda install -y -c conda-forge python-igraph
```

### Installing networkx

```
conda create --name networkx
conda activate networkx
conda install -y -c anaconda networkx
```

### Installing networkit

Install Clang++ (note: have to install 3.7 / 3.8) and cmake

```
sudo apt install clang-3.8
sudo apt install cmake
```

Install networkit

```
pip install ipython
conda create --name networkit
conda activate networkit
conda install -y -c conda-forge networkit ipython
```

### Installing SNAP

```
conda create --name snap
conda activate snap
pip install snap-stanford
```

### Installing LightGraphs

```
julia -e 'using Pkg; Pkg.add.("LightGraphs")'
```
