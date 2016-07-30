import parseCount



def parse_nodes(filename):      #extracts information from the list of hypernodes and puts them into node objects. Right now it only actually uses the names of the nodes.
    node_ls = []
    with open(filename, 'r') as file:
        file.readline()
        for line in file.readlines():
            curr_ls = line.split("\t")
            node_ls.append(node(curr_ls[0]))
    node_ls.sort(key = lambda n: n.name)
    return node_ls

class node():                    #node objects for the graph G. they know who they are adjacent to and whether they are in a fragment
    def __init__(self, name):
        self.name = name
        self.entrances = []
        self.exits = []
        self.pRegulates = []
        self.pRegulatedBy = []
        self.nRegulates = []
        self.nRegulatedBy = []
        self.adj_nodes = []
        self.hedges = []
        self.distance = -1
        self.parent = None
        self.in_frag = None
        self.index = None
        self.lowlink = None    #index and lowlink are for Tarjan's algorithm, implemented in tarjan.py
    

def populate_help(node_ls, hedge_ls,curr_hedge, part):       #helper function for populate_nodes()
    if part == "tail_ls":
        lookup = curr_hedge.tail_ls
    elif part == "posReg":
        lookup = curr_hedge.posReg
    elif part == "negReg":
        lookup = curr_hedge.negReg
    
    for item in lookup:
        if item != "None":
            tail_node = binary_search_names(node_ls, item)
            if tail_node == None:
                print("Error in first step of populate_help! Failed to look up " + item)
            else:    
                for h in curr_hedge.head_ls:
                    if h != "None":
                        head_node = binary_search_names(node_ls, h)
                        if head_node == None:
                            print("Error in second step of populate_help! Failed to look up " + h)
                        tail_node.hedges.append(curr_hedge)
                        head_node.hedges.append(curr_hedge)
                        
                        tail_node.adj_nodes.append(head_node)
                        head_node.adj_nodes.append(tail_node)
                        

                        if part == "tail_ls":
                            tail_node.exits.append(head_node)
                            head_node.entrances.append(tail_node)
                        elif part == "posReg":
                            tail_node.pRegulates.append(head_node)
                            head_node.pRegulatedBy.append(tail_node)
                        elif part == "negReg":
                            tail_node.nRegulates.append(head_node)
                            head_node.nRegulatedBy.append(tail_node)
        
def populate_nodes(node_ls, hedge_ls, regulators = False):     #attaches the node objects together using a list of hedges (which can be obtained using a function in parseCount.py). In doing so converts the hypergraph back to a standard graph.
    for hedge in hedge_ls:
        populate_help(node_ls, hedge_ls, hedge, "tail_ls")
        if regulators == True:
            populate_help(node_ls, hedge_ls, hedge, "posReg")
            populate_help(node_ls, hedge_ls, hedge, "negReg")


def binary_search_names(ls, target, start=0, end=None):        #binary searches a list of nodes organized by name
    if end == None:
        end = len(ls)

    mid = (end+start)//2
    if ls[mid].name == target:
        return ls[mid]
    elif start == end:
        return None
    elif ls[mid].name < target:
        return binary_search_names(ls, target, mid+1, end)
    elif ls[mid].name > target:
        return binary_search_names(ls, target, start, mid)



