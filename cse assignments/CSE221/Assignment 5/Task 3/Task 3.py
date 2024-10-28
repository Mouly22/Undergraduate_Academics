
#Task 3
inp4 = open('/Users/mouly/Downloads/input3_1.txt', 'r')
out4 = open('/Users/mouly/Downloads/output3_1.txt', 'w')
line = inp4.readline()
line = line.split()
vrtx1 = int(line[0])
edge1 = int(line[1])
class DFS:
    def __init__(self, num, edges_num):
        self.vrtx = num
        self.edges = edges_num
        self.dfsgraph = {}
        self.dfslst = []
        
    def Edge_create(self, val1, val2):
        if val1 not in self.dfsgraph:
            self.dfsgraph[val1] = []
        if val2 not in self.dfsgraph:
            self.dfsgraph[val2] = []
        self.dfsgraph[val1].append(val2)
        self.dfsgraph[val2].append(val1)
        
                
    def DFS_TRAVS(self, start):   
        self.dfslst.append(start)
        for m in self.dfsgraph[start]:
            if m not in self.dfslst:
                self.DFS_TRAVS(m)
                
dfs = DFS(vrtx1, edge1)
for p in range(int(line[1])):
    lines = inp4.readline()
    elms = lines.split()
    dfs.Edge_create(int(elms[0]), int(elms[1]))

for j in dfs.dfsgraph.keys():
    dfs.DFS_TRAVS(j)
    break

saving = ''
for q in dfs.dfslst:
    saving += str(q) + ' '
out4.write(saving)
out4.close()


# In[ ]:





# In[ ]:




