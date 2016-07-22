import parseCount


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



hedges = parseCount.parse_hedges("/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hyperedges.txt")

nodes = parse_nodes(FILENAME)