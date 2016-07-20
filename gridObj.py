#the grid class will store a grid that describes the number of hedges with 1, 2, and >2 nodes in their heads/tails
#later it may also store additional information

class grid():
	def __init__(self):
		self.ht_ls = self.makeGrid(3,3)
                self.posRegs = 0
                self.negRegs = 0
		#other information such as statistics about regulation may be included here
		
	def makeGrid(self,r,c):
		rows = []
		for i in range(r):		#initialize rows by appending r empty lists to the main list
			rows.append([])
		for r in rows:			#for each row append c 0's to represent the columns
			for j in range(c):
				r.append(0)
		return rows
		
	def grid_inc(self,h,t,pR=0,nR=0):	
		if h >= 3:
			h = 3
		if t >= 3:
			t = 3						#because the entries in the grid are going to be 1, 2, >2
		self.ht_ls[h-1][t-1] += 1		#ht_ls will be the list of lists that contains all the numbers in the grid, the -1 is because [0,0] is actually the 1 head 1 tail box

                if pR == 1:
                        self.posRegs += 1
                if nR == 1:
                        self.negRegs += 1

                        
	def square_report(self, h, t, percentage=False):
                if percentage == True:
                        total_hedges = self.grid_total()
                        p_of_total = (self.ht_ls[h-1][t-1] / float(total_hedges))*100
                        return p_of_total
                else:
                        return self.ht_ls[h-1][t-1]


        def grid_total(self):
                total = 0
                for row in self.ht_ls:
                        for item in row:
                                total += item
                return total
        
	def render_grid(self, p=False):				#renders a string representation of the grid in the command prompt (it's not well aligned right now but it gets the point across)
		grid_str = "   t: \t 1 \t 2 \t >2 \n" + "h: \n"
		i = 1
		for row in self.ht_ls:
			string_i = str(i)
			if i == 3:
				string_i = ">2"
                        if p == False:
                                row_str = string_i + " \t " + str(self.square_report(i,1)) + " \t " + str(self.square_report(i,2)) + " \t " + str(self.square_report(i,3)) + " \n"
                        else:
                                row_str = string_i + " \t " + str("%.1f" % self.square_report(i,1,True)) + " \t " + str("%.1f" % self.square_report(i,2,True)) + " \t " + str("%.1f" % self.square_report(i,3,True)) + " \n"
			grid_str = grid_str + row_str
			i += 1

                grid_str += "\n"
                grid_str += "Positively Regulated Hedges: " + str(self.posRegs) + " (" + str("%.1f" % (100 * self.posRegs / float(self.grid_total()))) + "%) \n"
                grid_str += "Negatively Regulated Hedges: " + str(self.negRegs) + " (" +  str("%.1f" % (100 * self.negRegs / float(self.grid_total()))) + "%) \n"
                grid_str += "\n" + "TOTAL HEDGES: " + str(self.grid_total())
		print(grid_str)





#random testing stuff below
g = grid()
for i in range(50):
	g.grid_inc(1,1)

for i in range(500):
	g.grid_inc(2,1)
	g.grid_inc(5,2)

g.render_grid()
