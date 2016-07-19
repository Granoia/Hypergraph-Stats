def parse_hedges(file):
	hedges = [] 		#list of hedge objects
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
	return hedges


class hedge():
	def __init__(self,head,tail,posReg,negReg,ID,pathways):
		self.head_ls = head
		self.tail_ls = tail
		self.posReg = posReg
		self.negReg = negReg
		self.ID = ID
		self.pathways = pathways