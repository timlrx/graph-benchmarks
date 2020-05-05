#! /bin/bash
sudo su -

apt-get update

# Basic packages
apt-get install -y \
    curl \
    python3-pip \
    software-properties-common \
    clang-3.8 \
    cmake \
    libgtk-3-0 

### Install Miniconda
cd /opt

wget -nv 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh' -O conda.sh \
    && bash conda.sh -b -p /opt/conda \
    && rm conda.sh \
    && sudo ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh

### Install Julia 
wget -nv https://julialang-s3.julialang.org/bin/linux/x64/1.4/julia-1.4.1-linux-x86_64.tar.gz -O julia.tar.gz \
    && tar -xvzf julia.tar.gz \
    && echo 'PATH=$PATH:/opt/julia-1.4.1/bin' >> /etc/profile

source /etc/profile
conda activate

### Install LightGraphs
julia -e 'using Pkg; Pkg.add.("LightGraphs")'

### Install Igraph
conda create --name igraph
conda activate igraph
conda install -y -c conda-forge python-igraph

### Install Networkx
conda create --name networkx
conda activate networkx
conda install -y -c anaconda networkx

### Install Graph-tool
conda create --name graphtool
conda activate graphtool
conda install -y -c conda-forge graph-tool

### Install Networkit
pip install ipython
conda create --name networkit
conda activate networkit
conda install -y -c conda-forge networkit ipython

### Install Snap
conda create --name snap python=3.7
conda activate snap
pip install snap-stanford
