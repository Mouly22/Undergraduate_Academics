
#Task 6:
inp7 = open('/Users/mouly/Downloads/input6_5.txt', 'r')
out7 = open('/Users/mouly/Downloads/output6_5.txt', 'w')
line = inp7.readline()
line = line.split()
vrtx1 = int(line[0])
edge1 = int(line[1])


class Diamond_hunting:
    max_counter = 0
    def __init__(self, rw_count, col_count):
        self.vrtx = rw_count
        self.edges = col_count
        self.dfslst = []
        self.counter = 0
        

    def DFS_TRAVS(self,lst,row,column):
        if row < self.vrtx and column < self.edges and row >=0 and column >= 0:

            if lst[row][column]  in [".","D"]:
                self.dfslst.append([row,column])
                if lst[row][column] == "D":
                    self.counter += 1
                if [row-1,column] not in self.dfslst:
                    self.DFS_TRAVS(lst,row-1,column)
                if [row+1,column] not in self.dfslst:
                    self.DFS_TRAVS(lst,row+1,column)
                if [row,column-1] not in self.dfslst:
                    self.DFS_TRAVS(lst,row,column-1)
                if [row,column+1] not in self.dfslst:
                    self.DFS_TRAVS(lst,row,column+1)   
            else:
                pass
        if Diamond_hunting.max_counter < self.counter:
            Diamond_hunting.max_counter = self.counter

                
dfs = Diamond_hunting(vrtx1, edge1)

store_lst = []
for p in range(int(line[0])):
    lines = inp7.readline().rstrip("\n")
    store_lst.append(lines)


max_counter = 0
for ver in range(vrtx1):
    for ed in range(edge1):
        obj = Diamond_hunting(vrtx1,edge1)
        obj.DFS_TRAVS(store_lst,ver,ed)
out7.write(str(Diamond_hunting.max_counter))
out7.close()







