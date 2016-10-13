import igraph as ig
import argparse
import sys

def main():

    parser = argparse.ArgumentParser(description="Given an edge list, returns modularity as calculated by infomap, multilevel and label propogation algorithms. Or, specifiy a single option")
    parser.add_argument("file_path", help="CSV edge list. One line per edge, include weights in third column if using -d option")
    parser.add_argument("-i", "--infomap", help="calculate modularity using the infomap method of Rosvall and Bergstrom", action="store_true")
    parser.add_argument("-m", "--multilevel", help="calculate modularity using the multilevel algorithm of Blondel et al.", action="store_true")
    parser.add_argument("-l", "--labelpropagation", help="calculate modularity using the label propagation method of Raghavan et al.", action="store_true")
    parser.add_argument("-d", "--directed", help="if directed graph", action="store_true")
    args = parser.parse_args()
    file_path = args.file_path
    is_directed = args.d
    methods =[]

    if args.i:
        methods.append("infomap")
    if args.m:
        methods.append("multilevel")
    if args.l:
        methods.append("label_propagation")
    
    try:
        g = get_graph(file_path, is_directed)
    except:
        sys.exit("Could not read graph file. Please ensure proper format")
        
    if not methods: #if they didn't specify run all of them
        methods = ["infomap", "multilevel", "label_propagation"]
    for method in methods:
        try:
            modularity = modularity_score(method, g)
            print modularity,
        except:
            print "ERR" #because a single method could fail, for some reason.
        finally:
            print #just a newline

def modularity_score(method, g):
    if "infomap" in method:
        vc = g.community_infomap()
    if "multilevel" in method:
        vc = g.community_multilevel()
    if "labelpropagation" in method:
        vc = g.community_label_propagation()

    return g.modularity(vc)

def get_graph(file_path, is_directed):
    G = ig.Read_Ncol(file_path, directed=is_directed)
    return G
