
f1 = open("20101539_Umme Abira Azmary_CSE422_11_Assignment01_Summer2024_InputFile.txt", "r")
f2 = open("output.txt", "w")
import heapq

class MinimumPQueue:
    def __init__(self):
        self.varcount = 0
        self.priorty_list = []


    def nodepush(self, tobject, priorty_value):
        heapq.heappush(self.priorty_list, (priorty_value,self.varcount  , tobject))
        self.varcount += 1


    def nodepop(self):
        temp_lst =  heapq.heappop(self.priorty_list)
        return temp_lst[-1]

    def is_empty(self):
        temp_lst = self.priorty_list

        if len(temp_lst) == 0:
            return True
        else:
            return False


class Node:
    def __init__(self,name,pcost,hcost,pnode):
        self.name = name
        self.pcost = pcost
        self.hcost = hcost
        self.pnode = pnode
        self.total_cost = hcost+ pcost

pq = MinimumPQueue()
heurestic = {}
path_costs = {}
expired_parents = {}

for line in f1:
    line = line.split()
    main_node = line[0]
    heurestic[main_node] = int(line[1])

    path_costs[main_node] = []
    for selm in range(2,len(line),2):
        #print(line[selm],line[selm+1])
        path_costs[main_node].append([line[selm], int(line[selm+1])])

    #f2.write(line)

starting_node = input("Enter starting node: ")

ending_node = input("Enter destination node: ")


total_path_costs = 0

final_node = None

node1 = Node(starting_node,0,heurestic[starting_node],None)
pq.nodepush(node1,node1.total_cost)



while pq.is_empty() == False:
    node1 = pq.nodepop()
    # print(node1.name)
    noneflag = node1.pnode is None
    if node1.name == ending_node:
        final_node = node1
        break
    if node1.name not in expired_parents.keys():
        if node1.pnode:
            expired_parents[node1.name] = [node1.pnode.name]
    else:
        if node1.pnode:
            if node1.pnode.name in expired_parents[node1.name]:
                continue
            else:
                expired_parents[node1.name].append(node1.pnode.name)


    for elm in path_costs[node1.name]:
        if noneflag or node1.pnode.name != elm[0]:
            pcost = node1.pcost + elm[1]
            new_node = Node(elm[0],pcost,heurestic[elm[0]],node1)
            pq.nodepush(new_node,new_node.total_cost)

#print(heurestic)
#print(path_costs)


temp_node = final_node
flst = []
while temp_node is not None:
    flst.append(temp_node.name)
    temp_node = temp_node.pnode

flst = flst[::-1]

if len(flst) >0:
    # print(flst)
    wordlst = ""

    for selm in flst:
        wordlst += selm + " -> "
    wordlst = wordlst.rstrip("-> ")
    print(f"Path: {wordlst}")
    print(f"Total distance: {final_node.pcost} km")
else:
    print("NO PATH FOUND")

f1.close()
f2.close()

