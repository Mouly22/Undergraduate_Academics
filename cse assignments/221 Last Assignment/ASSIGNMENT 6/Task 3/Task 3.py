

inp62 = open('/Users/mouly/Downloads/input3_1.txt', 'r')
out62 = open('/Users/mouly/Downloads/output3_1.txt', 'w')
class dfs_run:
    def __init__(self,first):
        self.wght_lst = []
        self.store = []
        self.first = first
        
    def DFS_trav(self, adj_list, vrtx, wght):
        if vrtx in adj_list.keys():
            if vrtx == self.first:
                for val in adj_list[vrtx]:
                    self.wght_lst.append(wght)
                    self.DFS_trav(adj_list, val[0], val[1])
                    self.store.append(self.wght_lst)
                    self.wght_lst = []
            else:
                for val in adj_list[vrtx]:
                    self.wght_lst.append(wght)
                    self.DFS_trav(adj_list, val[0], val[1])
        else:
            self.wght_lst.append(wght)
            
line1 = inp62.readline().split()
dct = {}
for m in range(int(line1[1])):
    v = inp62.readline().split()
    if int(v[0]) not in dct.keys():
        dct[int(v[0])] = [(int(v[1]), int(v[2]))]
    else:
        dct[int(v[0])].append((int(v[1]), int(v[2])))

    
def minmax_wght(adj_list):
    min_wght = float('inf')
    
    for val in adj_list[1]:
        dfs = dfs_run(val[0])
        dfs.DFS_trav(adj_list, val[0], val[1])
        
        for wghts in dfs.store:
            max_wght = max(wghts)
            if max_wght < min_wght:
                min_wght = max_wght
    
    return min_wght

out62.write(str(minmax_wght(dct)))
out62.close()


# In[ ]:





# In[ ]:




