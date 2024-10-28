#Task 7:
inp8 = open('/Users/mouly/Downloads/input7_1.txt', 'r')
out8 = open('/Users/mouly/Downloads/output7_1.txt', 'w')
linnee = inp8.readline()
linnee = linnee.split()
stor1 = int(linnee[0])


class max_visit:
    def __init__(self, num):
        self.vrtx = num
        self.bfsgraph = {}
        self.findict = {}
     

        
    def Edges_create(self, val1, val2):
        if val1 not in self.bfsgraph:
            self.bfsgraph[val1] = []
        if val2 not in self.bfsgraph:
            self.bfsgraph[val2] = []
        self.bfsgraph[val1].append(val2)
        self.bfsgraph[val2].append(val1)
             
    def BFS_TRAVS(self, start, des) :
        self.findict[start] = 0
        storing = []
        reslst = []
        checking_visit= {}
        pathdict= {}
        let_val = des
        time = 0
        reslst.append(let_val)
        storing.append(start)
        checking_visit[start] = 0
        while len(storing):
            temp = storing.pop(0)
            for valus in self.bfsgraph[temp]:
                if valus not in checking_visit:
                    #print(self.findict)
                    self.findict[valus] = self.findict[temp] + 1
                    storing.append(valus)
                    pathdict[valus] = temp
                    checking_visit[valus] = 1
                    if valus == des:
                        time = self.findict[valus]
                                              
        while let_val != start:
            let_val = pathdict[let_val]
            reslst.append(let_val)
            
        reslst.reverse()
        st = ''
        for x in reslst:
            st += str(x)+ ' '
        return time
        
bfs = max_visit(stor1)
for i in range(stor1-1):
    lines = inp8.readline()
    elm = lines.split()
    bfs.Edges_create(int(elm[0]), int(elm[1]))
maxtime = 0
max_elms = None
for i in bfs.bfsgraph.keys():
    for j in bfs.bfsgraph.keys():
        if i ==j:
            pass
        else:
            time = bfs.BFS_TRAVS(i, j)
            if time > maxtime:
                maxtime = time
                max_elms = [i,j]
#print(maxtime)
#print(max_elms)
for i in max_elms:
    #print(i)
    out8.write(str(i)+" ")

      
inp8.close()
out8.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




