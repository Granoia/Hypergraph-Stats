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


def get_frag_sizes(frag_ls,min=1):
    sizes = []
    for frag in frag_ls:
        if frag.size >= min:
            sizes.append(frag.size)
    return sizes


hedges = parseCount.parse_hedges("/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hyperedges.txt")

nodes = parseNodes.parse_nodes("/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hypernodes.txt")
parseNodes.populate_nodes(nodes, hedges, True)

frags = find_frags(nodes)
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
