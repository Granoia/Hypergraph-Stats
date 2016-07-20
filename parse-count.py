FILENAME = "/data/parsers/biopax-parsers/Reactome/combined-hypergraph/all-hyperedges.txt"

def parse_hedges(file):
	hedges_ls = [] 		#list of hedge objects
	with open(file, 'r') as f:
		f.readline()
		for line in f.readlines():
			h_ls = line.split("\t")
			tails = h_ls[0].split(";")
			heads = h_ls[1].split(";")
			posReg = h_ls[2].split(";")
			negReg = h_ls[3].split(";")
			ID = h_ls[4]
			pathways = h_ls[5].split(";")
			hedges_ls.append(hedge(heads,tails,posReg,negReg,ID,pathways))
	return hedges_ls


class hedge():
	def __init__(self,head,tail,posReg,negReg,ID,pathways):
		self.head_ls = head
		self.tail_ls = tail
		self.posReg = posReg
		self.negReg = negReg
		self.ID = ID
		self.pathways = pathways

hedges = parse_hedges(FILENAME)
print(len(hedges))
print(hedges[-1].ID)
