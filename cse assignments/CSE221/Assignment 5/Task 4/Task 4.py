
#Task 4
inp5 = open('/Users/mouly/Downloads/input4_5.txt', 'r')
out5 = open('/Users/mouly/Downloads/output4_5.txt', 'w')
linee = inp5.readline()
linee = linee.split()
vrtxs = int(linee[0])
edges = int(linee[1])
class cycle_finding:
    def __init__(self, num, edges_num):
        self.vrtx = num
        self.edges = edges_num
        self.dfsgraph = {}
        self.dfslst = []
        self.flag = True
        self.storelst = []
        
    def Edge_creating(self, val1, val2):
        if val1 not in self.dfsgraph:
            self.dfsgraph[val1] = []
        if val2 not in self.dfsgraph:
            self.dfsgraph[val2] = []
        self.dfsgraph[val1].append(val2)
               
    def dfs_cycle_travs(self, start):
        self.dfslst.append(start)
       
        for m in self.dfsgraph[start]:
            if m not in self.dfslst:
                self.dfs_cycle_travs(m)
            else:
                if m in self.dfsgraph.keys():
                    store_val = self.dfsgraph[m]
                    if start in store_val:
                        self.flag = False
                        

                    else:
                        for elms in range(len(store_val)):
                            if store_val[elms] in self.dfsgraph.keys():
                                if start in self.dfsgraph[(store_val[elms])]:
                                    self.flag = False
                                    
    def cycle_print(self):
        
        if self.flag == False:
            out5.write("YES")
        else:
            out5.write("NO")
                   
                
cycle = cycle_finding(vrtxs, edges)
for q in range(int(linee[1])):
    lines = inp5.readline()
    elwms = lines.split()
    cycle.Edge_creating(int(elwms[0]), int(elwms[1]))
#print(dfs.dfsgraph)
for j in cycle.dfsgraph.keys():
    cycle.dfs_cycle_travs(j)
    break
cycle.cycle_print()
out5.close()





