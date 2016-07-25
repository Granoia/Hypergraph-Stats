import parseCount


FILENAME = "/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hypernodes.txt"



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
        self.distance = -1
        self.parent = None
        self.in_frag = None
    

def populate_nodes(node_ls, hedge_ls, regulators = False):     #attaches the node objects together using a list of hedges (which can be obtained using a function in parseCount.py). In doing so converts the hypergraph back to a standard graph.
    weird_errors = 0
    for hedge in hedge_ls:
        for t in hedge.tail_ls:
            if t == None:
                print("Error! t is None for some reason")
        t_node = binary_search_names(node_ls, t)
        if t_node == None:
            #print("Error in t search! node: " + t + " not found in node_ls!")
            #print(t)
            weird_errors += 1
        else:
            for h in hedge.head_ls:
                if h == None:
                    print("Error! h is None for some reason")
                h_node = binary_search_names(node_ls, h)
                if h_node == None:
                    print("Error in h search! node: " + h + " not found in node_ls!")
                else:
                    t_node.exits.append(h_node)
                    t_node.adj_nodes.append(h_node)
                    h_node.entrances.append(t_node)
                    h_node.adj_nodes.append(t_node)
        if regulators == True:
            for p in hedge.posReg:
                p_node = binary_search_names(node_ls, p)
                if p_node == None:
                    weird_errors += 1
                else:
                    for h in hedge.head_ls:
                        h_node = binary_search_names(node_ls, h)
                        if h_node == None:
                            print("Error in pReg h search!")
                        else:
                            p_node.pRegulates.append(h_node)
                            p_node.adj_nodes.append(h_node)
                            h_node.pRegulatedBy.append(p_node)
                            h_node.adj_nodes.append(p_node)
            for n in hedge.negReg:
                n_node = binary_search_names(node_ls, n)
                if n_node == None:
                    weird_errors += 1
                else:
                    for h in hedge.head_ls
                        h_node = binary_search_names(node_ls, h)
                        if h_node == None:
                            print("Error in nReg h search!")
                        else:
                            n_node.nRegulates.append(h_node)
                            n_node.adj_nodes.append(h_node)
                            h_node.pRegulatedBy.append(n_node)
                            h_node.adj_nodes.append(n_node)
            
    print("that weird error happened " + str(weird_errors) + " times")


def binary_search_names(ls, target, start=0, end=None):
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


"""
hedges = parseCount.parse_hedges("/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hyperedges.txt")

nodes = parse_nodes(FILENAME)
populate_nodes(nodes, hedges)

print("total nodes: " + str(len(nodes)))

def count_disconnected(nodes):
    i = 0
    for n in nodes:
        if n.adj_nodes == []:
            i += 1
    return i

print("nodes with no edges: " + str(count_disconnected(nodes)))
"""


"""
test = []

test.append(node("b"))
test.append(node("d"))
test.append(node("a"))
test.append(node("c"))
test.append(node("z"))

def print_test(ls):
        str = ""
        for n in ls:
                str += n.name + " "
        print(str)
        print

print_test(test)

test.sort(key = lambda n: n.name)

print_test(test)

print(binary_search_names(test, "b").name)
"""
