

inp321 = open('/Users/mouly/Downloads/input3_2.txt', 'r')
out321 = open('/Users/mouly/Downloads/output3_2.txt', 'w')
inp = inp321.readline().split()
total = int(inp[1])    
par = {}
count = {}
dct = {}
lst = []
for i in range(total):
    inps = inp321.readline().split()
    lst.append((int(inps[0]), int(inps[1])))  
c_0 = -1    
for m in range(len(lst)): 
   
    if lst[m][0] not in dct.keys() and lst[m][1] not in dct.keys():
        par[c_0+1] = c_0+1
        count[c_0+1] = 2
        dct[lst[m][0]] = c_0+1
        dct[lst[m][1]] = c_0+1
        c_0 += 1
        out321.write(str(count[par[dct[lst[m][0]]]]))
        out321.write('\n')
           
    elif lst[m][0] in dct.keys() and lst[m][1] not in dct.keys():
        count[dct[lst[m][0]]] += 1
        dct[lst[m][1]] = dct[lst[m][0]]
        out321.write(str(count[par[dct[lst[m][0]]]]))
        out321.write('\n')
        
    elif lst[m][0] not in dct.keys() and lst[m][1] in dct.keys():
        count[dct[lst[m][1]]] += 1
        dct[lst[m][0]] = dct[lst[m][1]]
        out321.write(str(count[par[dct[lst[m][0]]]]))
        out321.write('\n')
        
    elif par[dct[lst[m][0]]] == par[dct[lst[m][1]]]:
        pass
        out321.write(str(count[par[dct[lst[m][0]]]]))
        out321.write('\n')
    
    else: 
        count[dct[lst[m][0]]] += count[dct[lst[m][1]]]
        par[dct[lst[m][1]]] = dct[lst[m][0]] 
        out321.write(str(count[par[dct[lst[m][0]]]]))
        out321.write('\n')
out321.close()






# In[ ]:




