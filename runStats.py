#runfile for hypergraph-stats
#this file contains blocks of code that you can comment/uncomment to recieve whichever statistics you'd like

#contents:
#block 0: initialization
#block 1: hedge stats grid
#block 2: weakly connected components of the reactome
#block 3: strongly connected components of the biggest fragment in the reactome 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Block 0: initialization
#DO NOT COMMENT THIS BLOCK OUT. IT IS NECESSARY FOR THE FUNCTIONALITY OF THE OTHER BLOCKS
#general purpose stuff: imports code from the other files, parses the hedges and nodes into objects
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from parseCount import *
from gridObj import *
from parseNodes import *
from fragCount import *
from tarjan import *


HEDGE_FILENAME = "/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hyperedges.txt"       #change these filepaths if you want to run the code on a different data set
HNODE_FILENAME = "/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hypernodes.txt"

hedges = parse_hedges(HEDGE_FILENAME)
nodes = parse_nodes(HNODE_FILENAME)

BLOCK1 = False
BLOCK2 = False
BLOCK3 = False


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#END BLOCK 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Block 1: hedge stats grid
#makes a grid that shows how many nodes are in the head and tail of each hedge in the hypergraph
#also shows the total number of hedges in the reactome, and how many are under positive / negative regulation
#
#by default, two grids (one with numbers and one with percentages) will be printed to console and saved in output.txt. If you would like to change where it writes to, just modify the string argument of g.output_grid() below
#
#for both render_grid and output_grid, the boolean variable is set to False by default, and gives the stats as percentages when True.
#for further details, see gridObj.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
BLOCK1 = True

g = grid()

count_hedges(hedges, g)

#the following four lines print the grid to console. Comment them out if you just want the data in a file

print()
print()
print("##############")
print("BLOCK 1 OUTPUT")
print("##############")
print()
g.render_grid() 
print()
print()
g.render_grid(True)
print()
print()


#the following two lines save the grid to a file.
#g.output_grid("output.txt")
#g.output_grid("output.txt",True)
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#END BLOCK 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Block 2: weakly connected components of the entire reactome
#uses BFS to compile the weakly connected components of the reactome into fragment objects -- notably, this means converting the hypergraph to a standard graph
#
#IMPORTANT NOTE: the boolean value in populate_nodes() determines whether regulator connectivity is included. That is, if the value is True, positive and negative regulators for each hedge will be included as 
# incoming nodes for the outputs of each pathway. If False, they will not be connected.
#
#frags: a list containing each fragment object
#frag_sizes: a list containing the number of nodes in each fragment object
#not_t_frags: a list of the sizes of each frag that has more than one node
#
#for additional details, see parseNodes.py and fragCount.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
BLOCK2 = True                          #this variable is purely for the runfile. it keeps track of whether this block has been run. Don't worry about it.



populate_nodes(nodes, hedges, False)   #the boolean determines whether regulator connectivity is included. False means it's not, True means it is.

frags = find_frags(nodes)
frags.sort(key = lambda n: n.size)
frag_sizes = get_frag_sizes(frags)
frag_sizes.sort()
non_t_frags = get_frag_sizes(frags,2)
non_t_frags.sort()


nodes_in = (frags[-1].size)
total_nodes = (len(nodes))
percent_of_nodes = "%.1f" % (100 * (nodes_in / float(total_nodes)))

hedges_in = (len(frags[-1].find_hedges()))
total_hedges = (len(hedges))
percent_of_hedges = "%.1f" % (100 * (hedges_in / float(total_hedges)))

print()
print()
print("##############")
print("BLOCK 2 OUTPUT")
print("##############")
print()

print("Total fragments: " + str(len(frags)))
print("max frag size is " + str(frag_sizes[-1]))
print("The following is a list of fragment sizes with greater than 1 node:")
print(non_t_frags)
print()
print("The biggest frag has " + str(nodes_in) + " nodes out of " + str(total_nodes) + " total nodes in file (" + str(percent_of_nodes) + "%)." )
print("The biggest frag has " + str(hedges_in) + " hedges out of " + str(total_hedges) + " total hedges in file (" + str(percent_of_hedges) + "%)." )
print()
print()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#END BLOCK 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Block 3: strongly connected components of the biggest fragment in the reactome
#uses tarjan's algorithm to find the strongly connected components of the big frag -- notably, this also looks at the graph as a standard graph
#
#see tarjan.py for additional details
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
BLOCK3 = True




#only worry about this if statement if you're running Block 3 but not Block 2.
#the boolean value in populate_nodes() determines whether regulator connectivity is included. False means it's not, True means it is. ONLY TAKES EFFECT IF YOU HAVENT RUN BLOCK 2
if BLOCK2 == False:
    populate_nodes(nodes, hedges, False)
    frags = find_frags(nodes)
    frags.sort(key = lambda n: n.size)

big_frag_nodes = frags[-1].node_ls    
notebook = notebook() #object for bookkeeping and data storage for tarjan's
tarjan(big_frag_nodes, notebook) #the data is stored in the notebook object once this line has been executed

important_c = notebook.extractImportantComponents()
size_dist = notebook.getSizeDistribution()
num_connected_nodes = notebook.countImportantNodes()

percent_connected_nodes = "%.1f" % (100 * (num_connected_nodes / float(len(big_frag_nodes))))

print()
print()
print("##############")
print("BLOCK 3 OUTPUT")
print("##############")
print()

print("There are " + str(num_connected_nodes) + " nodes in strongly connected components of the big frag out of " + str(len(big_frag_nodes)) + " total nodes in the big frag (" + str(percent_connected_nodes) + "%).")
print("There are " + str(len(important_c)) + " strongly connected components with greater than 1 node in the big fragment.")
print("The following is a list of the sizes of the strongly connected components in the big fragment:")
print(size_dist)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#END BLOCK 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





