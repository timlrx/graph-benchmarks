# Setup and Installation Guide

Configuration based on an Ubuntu 16.04 Google Compute VM.

Most of the installations are done using conda / pip since that makes package control simpler. The only exception is SNAP which has its own installation files. It also requires python 2 to run and does not have an official python 3 version.

Networkit has external dependencies on Clang++ and cmake which has to be additionally installed on top of the python package.

Due to the different requirements of each package, it is better to create a separate virtual environment for each installation.

### Install Miniconda

Follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04) guide but use miniconda instead of an anaconda installer. The installer can be found [here](https://docs.conda.io/en/latest/miniconda.html)

### Installing graph-tool

Setup new environment for the installation
```
conda create --name graphtool
conda activate graphtool
```

Install graph-tool
```
conda config --add channels conda-forge --add channels ostrokach-forge --add channels pkgw-forge
conda install -y -c pkgw-forge gtk3
conda install -y -c conda-forge pygobject
conda install -y -c conda-forge matplotlib
conda install -y -c ostrokach-forge graph-tool
conda install -y graphviz
conda install -y python-graphviz
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
conda create --name networkit
conda activate networkit
conda install -y pip
pip install networkit
```

### Installing SNAP (only runs on python 2)

```
conda create --name snap python=2.7
wget https://snap.stanford.edu/snappy/release/snap-4.1.0-4.1-centos6.5-x64-py2.6.tar.gz
tar zxvf snap-4.1.0-4.1-centos6.5-x64-py2.6.tar.gz
cd snap-4.1.0-4.1-centos6.5-x64-py2.6
sudo python setup.py install
```
