#parse --> count --> compile & report


def parse_hedges(file):
	hedges = [] 		#list of hedge objects
	for line in file:
		h_ls = tab break line
		tails = ; break h_ls[0]
		heads = ; break h_ls[1]
		...
		hedges_ls.append(hedge(tails,heads,...)
	return hedges


def count_hedges(hedges, g):		#g is a grid object
	for h in hedges:
		curr_heads = len(h.head_ls)
		curr_tails = len(h.tail_ls)
		#whatever else i want to count about the hedges can also be included here
		g.grid_inc(curr_heads, curr_tails)
		
	

	
class hedge():
	def __init__(self,head,tail,posReg,negReg,ID):
		self.head = head
		self.tail = tail
		self.posReg = posReg
		self.negReg = negReg
		self.ID = ID
		#each of these will be lists of nodes(by which i mean strings describing nodes from the hypergraph) except for ID which will just be a string presumably


		
#the grid class has been moved to its own file and will no longer be updated here, for the updated version look at grid-class.py
"""
class grid():
	def __init__(self):
		self.ht_ls = self.makeGrid(3,3)
		#other information such as statistics about regulation may be included here
		
	def makeGrid(self,r,c):
		rows = []
		for i in range(r):		#initialize rows by appending r empty lists to the main list
			rows.append([])
		for r in rows:			#for each row append c 0's to represent the columns
			for j in range(c):
				r.append(0)
		return rows
		
	def grid_inc(self,h,t):	
		if h >= 3:
			h = 3
		if t >= 3:
			t = 3						#because the entries in the grid are going to be 1, 2, >2
		self.ht_ls[h-1][t-1] += 1		#ht_ls will be the list of lists that contains all the numbers in the grid, the -1 is because [0,0] is actually the 1 head 1 tail box

	def square_report(self, h, t):
		return self.ht_ls[h-1][t-1]
	
	def render_grid(self):
		grid_str = "   h:   1   2   >2   \n" + "t: \n"
		i = 1
		for row in self.ht_ls:
			row_str = str(i) + "       " + str(self.square_report(i,1) + "   " + str(self.square_report(i,2)) + "   " + str(self.square_report(i,3)) + " \n"
			grid_str += row_str
			i += 1
		print(grid_str)
"""		
		
"""	
still to do:
	make sure the hedge class works
	manually create some dummy hedges and make sure count_hedges works
	better alignment for grid class renderer, but this is more of a detail to work out if I've got nothing else to do
	connectedness (look up metrics of connectedness, think about how to convert the hypergraph into a regular graph for connectedness testing purposes)
	
"""