
from queue import PriorityQueue
inp121 = open('/Users/mouly/Downloads/input1_1.txt', 'r')
out121 = open('/Users/mouly/Downloads/output1_1.txt', 'w')

total = inp121.readline()
store = []
for i in range(int(total)):
    v = inp121.readline()
    val = v.split()
    #print(val)
    store.append((int(val[1]), int(val[0])))
#print(store)

que = PriorityQueue()
for m in range(len(store)):
    que.put(store[m])

f_elm = que.get()

counter = 1
st = ''+ str(f_elm[1]) +' '+ str(f_elm[0])+ '\n'
for n in range(len(store)-1):
    elm = que.get()
    #print(elm)
    if elm[1] >= f_elm[0]:
        counter += 1
        f_elm = elm
        st += f'{f_elm[1]} {f_elm[0]}\n'

out121.write(str(counter))
out121.write('\n')
out121.write(str(st))
out121.close()


# In[ ]:




