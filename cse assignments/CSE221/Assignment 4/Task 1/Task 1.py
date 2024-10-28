


def readFile():
    # reading file from as input
    # change the file name according to yours
    f = open("graph.txt", "r")
    f2 = open('graph_output.txt', 'w')
    
    # first line of input contains the number of vertices in the graph
    n = f.readline()
    # strip() gets rid of the new line
    # try printing n without strip()
    # print(n.strip())
    n = n.strip()
    # print(type(n))
    # n is of type string. we need to convert it to int
    n=int(n)
    # print(type(n))
    
    # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    # print(c)
    
    buildGraphUsingDictionary(c,f, prnt= f2)
    
    buildGraphUsingListofLists(c,f, prnt= f2)



# we want to build an adjacency list like the following
# A -> B,C 
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}

def buildGraphUsingDictionary(c,f,prnt): 
    # creating a dictionary
    graph = {}
    
    # the following lines of the file contain the connections
    # creating a directed graph (a,b means a is connected to b)
    
    counter = 0
    while (counter<c):
        line = f.readline() # reading each line
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        
        # we first search if the value inside variable a exists in the dictionary or not
        if(a in graph):
            # if yes, then append() the value in b to a
            graph[a].append(b)
        else:
            # create a new list in graph with a as the key and b as the value
            graph[a] = [b]
        # print(a)
        # print(b)
        counter+=1    
    
    printGraph(graph, None, prnt)
       
    
# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
#  1 -> 2,4
#  2 -> 4
#  3 -> 1,4
#  4 -> 2
# notice this method takes both the graphs as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph
def printGraph(graph,listGraph, prnt):  
    if listGraph == None:
        for m, n in graph.items():
            v = ''
            for val in n:
                v = v +', ' +val
            v = v[1:]   
            prnt.write(f'{m} -> {v}\n')

    else:
        for p in range(len(listGraph)):
            work = ''
            for a in listGraph[p]:
                work = work + ', '+ str(a)
            work = work[1:]
            prnt.write(f'{p+1} ->{work}\n')


# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c,f, prnt):
    f = open('graph.txt', 'r')
    listGraph = [] # do not change the name of the variable
    count = 0
    tmp_lst =[]
    n_lst = []
    line1 = f.readline()
    line2 = f.readline()
    listGraph = []
    for m in range(c):
        line= f.readline() # reading each line
        store = line.strip()
        val1 = int(store[0])
        if val1 not in tmp_lst:
            tmp_lst.append(int(store[0]))
        v = sorted(tmp_lst)
        n_lst.append(store.split(','))

    for j in v:
        store2 = []
        for i in n_lst:
            if int(i[0]) == j:
                store2.append(int(i[1]))
        listGraph.append(store2)

    printGraph(None,listGraph, prnt)

# ======================Program starts here.========================

# read file using the readFile() method
readFile()


# In[ ]:




