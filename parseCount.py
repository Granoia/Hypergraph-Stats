from gridObj import *

def parse_hedges(file):     #extracts data out of a text file and organizes it into a list of hedge objects which is returned
    hedges_ls = []      #list of hedge objects
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


class hedge():          #simple class to organize the data in a hyperedge
    def __init__(self,head,tail,posReg,negReg,ID,pathways):
        self.head_ls = head
        self.tail_ls = tail
        self.posReg = posReg
        self.negReg = negReg
        self.ID = ID
        self.pathways = pathways

        
def count_hedges(hedges, g):        #g is a grid object. This function counts up the data for the grid object.
    for h in hedges:
        curr_heads = len(h.head_ls)
        curr_tails = len(h.tail_ls)
        if h.posReg[0] == "None":
            pR = 0
        else:
            pR = 1
        if h.negReg[0] == "None":
            nR = 0
        else:
            nR = 1
        g.grid_inc(curr_heads, curr_tails, pR, nR)