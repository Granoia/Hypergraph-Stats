from fragCount import LL_node
from parseNodes import node

def tarjan(nodes, notebook):
    s = stack()
    for v in nodes:
        if v.index == None:
            strong_connect(v,notebook, s)

def strong_connect(v, notebook, s):
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

            
            
class notebook():
    def __init__(self):
        self.index = 0
        self.entries = []
            
    def newEntry(self):
        line = []
        self.entries.append(line)
    
    def write(self, item):
        if len(self.entries) != 0:
            self.entries[-1].append(item)
        else:
            print("Notebook error. There are no entries in the notebook. Use newEntry() first.")
            return -1
            

class stack():
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
s = stack()
print(s.pop())
s.push(7)
s.push(8)
s.push(9)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
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