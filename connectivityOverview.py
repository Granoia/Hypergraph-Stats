"""
connectivity overview

part 1: parse & make node objects -> populate adjacency with edges
"""

FILENAME = "/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hypernodes.txt"


def parse_nodes(filename):      #extracts information from the list of hypernodes and puts them into node objects. Right now it only actually uses the names of the nodes.
	node_ls = []
	with open(filename, 'r') as file:
		file.readline()
		for line in file.readlines():
			curr_ls = line.split("\t")
			node_ls.append(node(curr_ls[0]))
	node_ls.sort(key = lambda n: n.name, reverse = True)
	return node_ls

class node():                    #node objects for the graph G. they know who they are adjacent to and whether they are in a fragment
	def __init__(self, name):
		self.name = name
		self.entrances = None
		self.exits = None
		self.adj_nodes = None
		distance = -1
		parent = None
		in_frag = None
	

def populate_nodes(node_ls, hedge_ls):     #attaches the node objects together using a list of hedges (which can be obtained using a function in parseCount.py). In doing so converts the hypergraph back to a standard graph.
	for hedge in hedge_ls:
		for t in hedge.tails:
			t_node = binary_search_names(node_ls, t)
			if t_node == None:
				print("Error! node: " + t + " not found in node_ls!")
			else:
				for h in hedge.heads:
					h_node = binary_search_names(node_ls, h)
					if h_node == None:
						print("Error! node: " + h + " not found in node_ls!")
					else:
						t_node.exits.append(h_node)
						t_node.adj_nodes.append(h_node)
						d_node.entrances.append(t_node)
						d_node.adj_nodes.append(t_node)

				
def binary_search_names(ls, target, start=0, end=None):
	if end == None:
		end = len(ls)

	mid = floor((end+start)/2)
	if ls[mid].name == target:
		return ls[mid]
	elif start == end:
		return None
	elif ls[mid].name < target:
		return binary_search(ls, , mid+1, end)
	elif ls[mid].name > target:
		return binary_search(ls, target, start, mid)




"""
part 2: probe connectivity of the graph using BFS, determine how many connected subgraphs are in the graph
"""

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
			self.tail.next = new_item
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