

#Task 1(B)
inp2 = open('/Users/mouly/Downloads/input1b_1.txt', 'r')
out2 = open('/Users/mouly/Downloads/output1b_1.txt', 'w')
line1 = inp2.readline()
line1 = line1.split()
stor1 = int(line1[0])
stor2 = int(line1[1])

class Node:
    def __init__(self, vrtx, wght):
        self.vrtx = vrtx
        self.wght = wght

class Graph:
    def __init__(self, num, edge_num):
        self.V = int(num)
        self.E = int(edge_num)
        self.lst = []
        self.dct = {}
        for i in range(self.V+ 1):
            self.lst.append(i)        
    
    def edges_w_weight(self, strt, end, wght):
        for i in range(self.V + 1):
            self.lst.append(i)
            
        for vals in self.lst:
            if vals not in self.dct:
                self.dct[vals] = []         
        val = Node(end, wght)
        self.dct[strt].append(val)
        
    def g_print(self):
        for m, n in self.dct.items():
            out2.write(f"{str(m)} : ")
            for elem in n:
                out2.write(f"({elem.vrtx}, {elem.wght}) ")
            out2.write("\n")  
        
graph = Graph(stor1, stor2)           
for i in range(int(line1[1])):
    lines = inp2.readline()
    elem = lines.split()
    graph.edges_w_weight(int(elem[0]), int(elem[1]), int(elem[2]))
graph.g_print()
out2.close()


# In[ ]:







