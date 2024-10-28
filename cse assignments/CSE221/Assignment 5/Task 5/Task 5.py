
#Task 5:
inp6 = open('/Users/mouly/Downloads/input5_1.txt', 'r')
out6 = open('/Users/mouly/Downloads/output5_1.txt', 'w')
linnee = inp6.readline()
linnee = linnee.split()
stor1 = int(linnee[0])
stor2 = int(linnee[1])
des = int(linnee[2])

class shortest_path:
    def __init__(self, num, edges_num):
        self.vrtx = num
        self.edges = edges_num
        self.bfsgraph = {}
        self.findict = {}
        self.findict[1] = 0 

        
    def Edges_create(self, val1, val2):
        if val1 not in self.bfsgraph:
            self.bfsgraph[val1] = []
        if val2 not in self.bfsgraph:
            self.bfsgraph[val2] = []
        self.bfsgraph[val1].append(val2)
        self.bfsgraph[val2].append(val1)
             
    def BFS_TRAVS(self, start, des) : 
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
                    self.findict[valus] = self.findict[temp] + 1
                    storing.append(valus)
                    pathdict[valus] = temp
                    checking_visit[valus] = 1
                    if valus == des:
                        time = self.findict[valus]
                        
                        
        while let_val != 1:
            let_val = pathdict[let_val]
            reslst.append(let_val)
            
        reslst.reverse()
        st = ''
        for x in reslst:
            st += str(x)+ ' '
        out6.write(f'Time:{str(time)}\n')
        out6.write(f'Shortest Path: {st}')
        

bfs = shortest_path(stor1, stor2)           
for i in range(stor2):
    lines = inp6.readline()
    elm = lines.split()
    bfs.Edges_create(int(elm[0]), int(elm[1]))
for i in bfs.bfsgraph.keys():
    if i == 1:
        bfs.BFS_TRAVS(i, des)
        break
inp6.close()
out6.close()


# In[ ]:





# In[ ]:




