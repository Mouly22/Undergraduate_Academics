
import heapq
import time
import math
import matplotlib.pyplot as plt
import numpy as np

class patient_system:
  def __init__(self): 
    self.lst = []
    
  def enque(self, vals): 
      heapq.heappush(self.lst, vals)
      

  def see_doctor(self):
      return heapq.heappop(self.lst)


  def printQueue(self):
    print(self.lst)

v = patient_system()
v.printQueue()


#(a)
def bubbleSort(arr):
        n = len(arr)
        flag = False
        for i in range(len(arr)):
            
            if flag:
                break 
            for j in range(0, len(arr) - i - 1):


                if int(arr[j].split()[-1]) >= int(arr[j + 1].split()[-1]):

                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                else:
                    flag = True
                    break
        
#(b)
def enque_new(name,list1):
    name,priority = name.split()
    list1.insert(0,f"{name} {priority}")
    bubbleSort(list1)
def see_doctor2(list1):
    name = list1.pop(0)
    return name
def print_queue(list1):
    for item in list1:
        print(list1)




#(c)
out4 = open('input3.txt',"r")
line1 = out4.readlines()
arr1 = []
arr2 = []
for p in line1:
    p = p.rstrip("\n")
    if p == "see doctor":
        arr2.append("delete")
    else:
        arr1.append(p)
        arr2.append("add")


arr = []
obj1 =patient_system()
obj2 = bubbleSort(arr)

no1 = [i for i in range(len(arr2)+1)]
no2 = [0 for i in range(len(arr2)+1)]
no3 = [0 for i in range(len(arr2)+1)]
store = 0
for q in range(len(arr2)):
    i1 = arr2[q]
    val = None
    if i1 =="add":
        temp = arr1[store]

        store += 1

        start = time.time()
        
        obj1.enque((int(temp.split()[-1]),temp)) 
        no2[q+1]= time.time()-start
        start = time.time()
        enque_new(temp,arr) 
        no3[q+1]= time.time()-start
    else:
        
        

        start = time.time()

        obj1.see_doctor() 

        no2[q+1]= time.time()-start
        start = time.time()
        see_doctor2(arr) 

        no3[q+1]= time.time()-start        

plt.plot(no1, no2, 'r')
plt.plot(no1, no3, 'b')
plt.xlabel('n-th position')
plt.ylabel('time')
plt.title('Comparing Time Complexity!')
plt.show()

