from fragCount import LL_node
from parseNodes import node

def tarjan(nodes, notebook):             #tarjan's algorithm, finds the strongly connected components of a directed graph
    s = stack()
    for v in nodes:
        if v.index == None:
            strong_connect(v,notebook, s)

def strong_connect(v, notebook, s):      #helper function for tarjan()
    v.index = notebook.index
    v.lowlink = notebook.index
    notebook.index += 1
    s.push(v)
    v.on_stack = True
    for w in v.exits:
        if w.index == None:
            strong_connect(w, notebook, s)
            v.lowlink = min(v.lowlink, w.lowlink)
        elif w.on_stack:
            v.lowlink = min(v.lowlink, w.index)
    if v.lowlink == v.index:
        notebook.newEntry()
        current = s.pop()
        current.on_stack = False
        notebook.write(current)
        while current != v:
            current = s.pop()
            current.on_stack = False
            notebook.write(current)

            
            
class notebook():                     #object that does some bookkeeping for tarjan() and also catalogues the data
    def __init__(self):
        self.index = 0
        self.entries = []
        self.importantComponents = None
            
    def newEntry(self):               #bookkeeping function for tarjan()
        line = []
        self.entries.append(line)
    
    def write(self, item):            #bookkeeping function for tarjan()
        if len(self.entries) != 0:
            self.entries[-1].append(item)
        else:
            print("Notebook error. There are no entries in the notebook. Use newEntry() first.")
            return -1
    
    def extractImportantComponents(self):    #returns a list of the components with more than 1 node in them, i.e. the components for which 'strongly connected' is an interesting property
        importantComponents = []
        for entry in self.entries:
            if len(entry) > 1:
                importantComponents.append(entry)
        self.importantComponents = importantComponents    #the method also updates the notebook object's importantComponents attribute, which is necessary for the following methods to run
        return importantComponents
        
    def getSizeDistribution(self):
        if self.importantComponents == None:
            print("Notebook error! getSizeDistribution() cannot run because a list of important components has not yet been catalogued. Run extractImportantComponents() first.")
            return -1
        else:
            sizes = []
            for component in self.importantComponents:
                sizes.append(len(component))
            sizes.sort()
            return sizes
    
    def countImportantNodes(self):
        if self.importantComponents == None:
            print("Notebook error! countImportantNodes() cannot run because a list of important components has not yet been catalogued. Run extractImportantComponents() first.")
            return -1
        else:
            sizes = self.getSizeDistribution()
            sum = 0
            for n in sizes:
                sum += n
            return sum


class stack():             #stack used for implementation of tarjan(), uses the LL_node class from fragCount.py
    def __init__(self):
        self.head = None
    
    def push(self, item):
        new_node = LL_node(item)
        if self.head == None:
            self.head = new_node
        else:
            new_node.attach(self.head)
            self.head = new_node
    
    def pop(self):
        popped_node = self.head
        if self.head != None:
            self.head = self.head.next
        if popped_node != None:
            popped = popped_node.val
            return popped
        else:
            return None


"""            
a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')

ls = [a,b,c,d,e,f]

a.exits.append(e)
b.exits.append(a)
e.exits.append(b)
d.exits.append(b)
f.exits.append(e)
f.exits.append(c)
c.exits.append(f)
c.exits.append(d)

n = notebook()

tarjan(ls, n)
print(n.entries)

def extract_data(notebook):
    for entry in notebook.entries:
        entry_str = ""
        for item in entry:
            entry_str += item.name
        print(entry_str)
        
extract_data(n)

"""