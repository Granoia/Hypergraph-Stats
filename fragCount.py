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