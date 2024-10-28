
from queue import PriorityQueue
inp81 = open('/Users/mouly/Downloads/input1_2.txt', 'r')
out81 = open('/Users/mouly/Downloads/output1_2.txt', 'w')
total = inp81.readline().split()
store = []
par = {}
dct = {}
for i in range(int(total[1])):
    v = inp81.readline().split()
    #print(v)
    store.append((int(v[2]), (int(v[0]), int(v[1]))))
#print(store)
lst = []
que = PriorityQueue()
for m in range(len(store)):
    que.put(store[m])
c_0 = -1
wght = 0
for n in range(len(store)):
    vals = que.get()
   
    
    
    if vals[1][0] not in dct.keys() and vals[1][1] not in dct.keys():
        par[c_0+1] = c_0+1
        dct[vals[1][0]] = c_0+1
        dct[vals[1][1]] = c_0+1
        c_0 += 1
        #print(par)
        wght += vals[0]
        
        
    elif vals[1][0] in dct.keys() and vals[1][1] not in dct.keys():
        dct[vals[1][1]] = dct[vals[1][0]]
        wght += vals[0]
        #print(dct)
        
    elif vals[1][0] not in dct.keys() and vals[1][1] in dct.keys():
        dct[vals[1][0]] = dct[vals[1][1]]
        wght += vals[0]
    else: 
        if par[dct[vals[1][0]]] == par[dct[vals[1][1]]]:
            pass

        else: 
            par[dct[vals[1][1]]] = dct[vals[1][0]]
            wght += vals[0]
out81.write(str(wght))
out81.close()


# In[ ]:





# In[ ]:




