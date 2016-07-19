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
		... #whatever else i want to count about the hedges can also be included here
		g.grid_inc|(curr_heads, curr_tails, ...)
		
	

	
class hedge():
	def __init__(self,head,tail,posReg,negReg,ID):
		self.head = head
		self.tail = tail
		self.posReg = posReg
		self.negReg = negReg
		self.ID = ID
		#each of these will be lists of nodes(by which i mean strings describing nodes from the hypergraph) except for ID which will just be a string presumably


class grid():
	def __init__(self):
		self.ht_ls = self.makeGrid(3,3)
		#other information such as statistics about regulation may be included here
		
	def makeGrid(r,c):
		rows = []
		for i in range(r):		#initialize rows by appending r empty lists to the main list
			rows.append([])
		for r in rows:			#for each row append c 0's to represent the columns
			for j in range(c):
				r.append(0)
		return rows
		
	def grid_inc(self,h,t):		#this will be a method of the grid class
		self.ht_ls[h][t] += 1		#ht_ls will be the list of lists that contains all the numbers in the grid

		
		
"""	
still to do:
	viewer for grid class
"""