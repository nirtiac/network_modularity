#!/usr/bin/env python

import igraph as ig
import argparse
import sys
from itertools import izip

def main():
    print "here"
    parser = create_parser()
    args = parser.parse_args()
    process_args(args)
    print "processed"

def process_args(args, out=sys.stdout):
    file_path = args.file_path
    is_directed = args.directed
    methods =[]
    silence = args.silence
    
    if args.infomap:
        methods.append("infomap")
    if args.multilevel:
        methods.append("multilevel")
    if args.labelpropagation:
        methods.append("label_propagation")
    
    try:
        g = get_graph(file_path, is_directed)
    except:
        sys.exit("Could not read graph file. Please ensure proper format")
        
    if len(methods) < 1: #if they didn't specify run all of them
        methods = ["infomap", "multilevel", "label_propagation"]

    for method in methods:
        try:
            modularity, vc = modularity_score(method, g)
            if args.outputcommunities:
                print_communities(modularity, vc, g, method, silence, out)
            else:
                out.write(str(modularity) + "\n")
        except:
            out.write("ERR" + "\n") #because a single method could fail, for some reason.
    
def create_parser():    
    parser = argparse.ArgumentParser(description="Given an edge list, returns modularity as calculated by infomap, multilevel and label propogation algorithms. Or, specifiy a single option")
    parser.add_argument("file_path", help="CSV edge list. One line per edge, include weights in third column if using -d option")
    parser.add_argument("-i", "--infomap", help="calculate modularity using the infomap method of Rosvall and Bergstrom", action="store_true")
    parser.add_argument("-m", "--multilevel", help="calculate modularity using the multilevel algorithm of Blondel et al.", action="store_true")
    parser.add_argument("-l", "--labelpropagation", help="calculate modularity using the label propagation method of Raghavan et al.", action="store_true")
    parser.add_argument("-d", "--directed", help="if directed graph", action="store_true")
    parser.add_argument("-o", "--outputcommunities", help="for each node output label and community, separated by a tab", action="store_true")
    parser.add_argument("-s", "--silence", help="don't print modularity score after outputcommunities. Will do nothing without -o argument", action="store_true")
    
    return parser

def print_communities(modularity, vc, g, method, silence, out2):
    membership = vc.membership
    for n,m in izip(g.vs["name"], membership):
        out2.write( n + "," + str(m) + "\n")

    if not silence:
        out2.write("method" + ": " + method + ", " + "modularity score: " + str(modularity) + "\n")

def modularity_score(method, g):
    if "infomap" in method:
        vc = g.community_infomap()
    if "multilevel" in method:
        vc = g.community_multilevel()
    if "label_propagation" in method:
        vc = g.community_label_propagation()

    return g.modularity(vc), vc

def get_graph(file_path, is_directed):         
    G = ig.Graph.Read_Ncol(file_path, directed=is_directed)
    return G

if __name__ == "__main__":
    main()
