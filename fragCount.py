import parseNodes
import parseCount
from statistics import *

def find_frags(G):           #this function will use BFS to find out how many connected subgraphs are in G (ignoring edge directionality). It will compile these into a returned list of fragment objects.
    frags=[]
    for node in G:
        if node.in_frag == None:
            frags.append(frag_BFS(G,node))
    return frags


def frag_BFS(G,root):         #G is the populated list of node objects, root is where the BFS will start. This function will do a breadth first search (ignoring edge directionality)
    frag_ls=[root]            #starting from root and compile each node reached this way into a returned fragment object.
    Q = queue()
    root.distance = 0
    Q.enqueue(root)
    while not Q.is_empty():
        curr = Q.dequeue()
        for n in curr.adj_nodes:
            if n.distance == -1:
                n.distance = curr.distance + 1
                n.parent = curr
                n.in_frag = True
                Q.enqueue(n)
                frag_ls.append(n)
    new_frag = fragment(frag_ls)
    return new_frag

class fragment():               #a fragment object catalogues a single connected subgraph in G
    def __init__(self,nodes):
        self.node_ls = nodes
        self.size = len(nodes)
    
    
    def find_node_by_name(self, target_name):
        for node in self.node_ls:
            if node.name == target_name:
                return node
        print("No node with given name in this fragment")
    
    def find_hedges(self):         #gets a list of all hedges included in a fragment
        all_hedges = []      #has duplicates
        frag_hedges = []     #will have duplicates filtered out
        for node in self.node_ls:
            all_hedges += node.hedges
        all_hedges.sort(key = lambda h: h.ID)
        i = 0
        all_len = len(all_hedges)
        if len(all_hedges) != 0:
            singleton = all_hedges[0]
            frag_hedges.append(singleton)
            while i < all_len:
                if all_hedges[i].ID != singleton.ID:
                    singleton = all_hedges[i]
                    frag_hedges.append(singleton)
                i += 1
        return frag_hedges

    def hedge_size(self):         #finds the number of hedges in the fragment
        frag_hedges = self.find_hedges()
        return len(frag_hedges)
            
        

class queue():                  #queue only for the purpose of implementing BFS
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, item):
        new_item = LL_node(item)
        if self.head == None:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.attach(new_item)
            self.tail = new_item
    
    def dequeue(self):
        if self.head == None:
            return None
        else:
            ret = self.head.val
            new_head = self.head.give_next()
            self.head.detach()
            self.head = new_head
            return ret
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

class LL_node():                 #node only for the purpose of implementing the queue class
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def detach(self):
        self.next = None
    
    def give_next(self):
        return self.next
    
    def attach(self, next_node):
        self.next = next_node


        
#these next three are just functions for looking at the data / sanity checking
def get_frag_sizes(frag_ls,min=1):
    sizes = []
    for frag in frag_ls:
        if frag.size >= min:
            sizes.append(frag.size)
    return sizes

def frag_checksum(frag_ls):
    total = 0
    for frag in frag_ls:
        total += frag.size
    return total


def hedge_checksum(frag_ls):
    total = 0
    for frag in frag_ls:
        total += frag.hedge_size()
    return total


"""    
#data gathering and various tests. This should really be in a runfile instead but I haven't gotten around to making one.
hedges = parseCount.parse_hedges("/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hyperedges.txt")
nodes = parseNodes.parse_nodes("/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hypernodes.txt")


parseNodes.populate_nodes(nodes, hedges, False)   #the boolean determines whether regulator connectivity is included. False means it's not, True means it is.

frags = find_frags(nodes)
frags.sort(key = lambda n: n.size)
frag_sizes = get_frag_sizes(frags)
frag_sizes.sort()


non_t_frags = get_frag_sizes(frags,2)
frags_atleast_3 = get_frag_sizes(frags,3)
frags_atleast_4 = get_frag_sizes(frags,4)
frags_atleast_5 = get_frag_sizes(frags,5)
frags_atleast_5.sort()

print("Total fragments: " + str(len(frags)))



print("Fragments with size > 1: " + str(len(non_t_frags)))
print("size at least 3: " + str(len(frags_atleast_3)))
print("size at least 4: " + str(len(frags_atleast_4)))
print("size at least 5: " + str(len(frags_atleast_5)))
print("max frag size is " + str(frag_sizes[-1]))

print("List of frag sizes above 5: \n" + str(frags_atleast_5))

frags[-1].find_node_by_name("None")


print()
print()

print("Big frag has " + str(frags[-1].size) + " nodes out of " + str(len(nodes)) + " total nodes in file.")
print("Big frag has " + str(len(frags[-1].find_hedges())) + " hedges out of " + str(len(hedges)) + " total hedges in file.")


print("Checksum: In all of the fragments there are " + str(frag_checksum(frags)) + " nodes. There are a total of " + str(len(nodes)) + " nodes in the file.")
print("Hedge Checksum: In all of the fragments there are " + str(hedge_checksum(frags)) + " hedges. There are a total of " + str(len(hedges)) + " hedges in the file.")
"""