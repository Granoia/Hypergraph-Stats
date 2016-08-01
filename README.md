# Hypergraph-Stats
A small project with the purpose of obtaining and cataloging statistics from biological interactomes that have been converted into hypergraphs.


use the runfile (python3 runStats.py) on one of the bioinf computers to get statistics about a reactome's connectivity and about what sorts of hyperedges it contains.

The comments of the runfile give a good summary of what they do, but I'll list the contents here:

block 0: initialization

block 1: hedge stats grid

block 2: weakly connected components of the whole reactome

block 3: strongly connected components of the biggest fragment in the reactome
