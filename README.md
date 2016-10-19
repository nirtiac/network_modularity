### network_modularity [![Build Status](https://travis-ci.org/nirtiac/network_modularity.svg?branch=master)](https://travis-ci.org/nirtiac/network_modularity)

This package provides quick access to the modularity scores returned by the infomap, multilevel and label-propagation community detection methods as implemented in [iGraph](http://igraph.org/python/)

### Installation
* make install

Note that the python-igraph dependency may conflict with an different older igraph package since changed to jgraph. If this occurs consider uninstalling igraph and reinstalling as jgraph.

### Usage

#### Command Line

See full options available : `nm --help`

```sh
usage: network_modularity [-h] [-i] [-m] [-l] [-d] file_path

Given an edge list, returns modularity as calculated by infomap, multilevel
and label propogation algorithms. Or, specifiy a single option

positional arguments:
  file_path             CSV edge list. One line per edge, include weights in
                        third column if using -d option

optional arguments:
  -h, --help            show this help message and exit
  -i, --infomap         calculate modularity using the infomap method of
                        Rosvall and Bergstrom
  -m, --multilevel      calculate modularity using the multilevel algorithm of
                        Blondel et al.
  -l, --labelpropagation
                        calculate modularity using the label propagation
                        method of Raghavan et al.
  -d, --directed        if directed graph
```

### Tests
* pip install -r requirements.txt
* make test

###
