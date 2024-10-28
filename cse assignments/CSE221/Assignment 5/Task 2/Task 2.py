
#Task 2
inp3 = open('/Users/mouly/Downloads/input2_1.txt', 'r')
out3 = open('/Users/mouly/Downloads/output2_1.txt', 'w')
line11 = inp3.readline()
line11 = line11.split()
stre1 = int(line11[0])
stre2 = int(line11[1])
class BFS:
    def __init__(self, num, edges_num):
        self.vrtx = num
        self.edges = edges_num
        self.graph = {}
        
    def Edges_create(self, val1, val2):
        if val1 not in self.graph:
            self.graph[val1] = []
        if val2 not in self.graph:
            self.graph[val2] = []
        self.graph[val1].append(val2)
           
    
    def BFS_TRAVS(self, start) :
        
        storing = [] 
        checking_visit= {}
        storing.append(start)
        lst = []
        for m in checking_visit.values():
            m = 0
        checking_visit[start] = 1
        while len(storing): 
            temp = storing.pop(0)
            lst.append(temp)   
            for valus in self.graph[temp]:   
                if valus not in checking_visit:
                    storing.append(valus) 
                    checking_visit[valus] = 1
        printing = ''
        for v in lst:
            printing += str(v) + ' '
        out3.write(printing)
            
        
bfs = BFS(stre1, stre2)           
for i in range(int(line11[1])):
    lines = inp3.readline()
    elm = lines.split()
    bfs.Edges_create(int(elm[0]), int(elm[1]))
    
for i in bfs.graph.keys():
    bfs.BFS_TRAVS(i)
    break
out3.close()


# In[ ]:





# In[ ]:




