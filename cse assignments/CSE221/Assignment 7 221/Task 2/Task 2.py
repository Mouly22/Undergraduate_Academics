
from queue import PriorityQueue
inp221 = open('/Users/mouly/Downloads/input2_1.txt', 'r')
out221 = open('/Users/mouly/Downloads/output2_1.txt', 'w')
number = inp221.readline().split()
task_no = number[0]
person = number[1]
store = []
for i in range(int(task_no)):
    v = inp221.readline().split()
    store.append((int(v[1]), int(v[0])))

que = PriorityQueue()
for m in range(len(store)):
    que.put(store[m])

f_elm = que.get()
p_lst = [0]*int(person)
p_lst[0] = f_elm[0]

counter = 1
st = ''+ str(f_elm[1]) +' '+ str(f_elm[0])+ '\n'

for n in range(len(store)-1):
    v = que.get()
    s_count = 0
  
    for i in p_lst:
        if v[1] >= i:
            if (s_count+1) < int(person):
                if p_lst[s_count+1]> p_lst[s_count] and p_lst[s_count+1] != 0 and p_lst[s_count+1] <= v[1]:
                    counter+= 1
                    f_elm = v
                    p_lst[s_count+1] = f_elm[0]
                    st += f'{f_elm[1]} {f_elm[0]}\n'
                    break
            counter+= 1
            f_elm = v
            p_lst[s_count] = f_elm[0]
            st += f'{f_elm[1]} {f_elm[0]}\n'
            break
        s_count += 1

out221.write(str(counter))
out221.close()

