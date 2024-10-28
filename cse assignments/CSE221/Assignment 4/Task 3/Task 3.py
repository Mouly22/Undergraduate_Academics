
inputt = open('input3_4.txt', 'r')
outputt = open('output3_4.txt', 'w')
line1 = inputt.readline()
line2 = inputt.readline()
arr = []
l1 = line2.split()

for m in l1:
  arr.append(int(m))

class Alien_height:
  def __init__(self):
    self.t_count = 0

  def merge(self, a, b):
  # Here a and b are two sorted list
  # merge function will return a sorted list after merging a and b
    lst1 = a
    lst2 = b
    pointer1 = 0
    pointer2 = 0
    n_lst = []
    checker1 = True
    checker2 = True
    temp_len = len(lst1)
    while True:
      if lst1[pointer1] > lst2[pointer2]:
        n_lst.append(lst2[pointer2])
        pointer2 += 1 
        self.t_count += temp_len
      else:
        n_lst.append(lst1[pointer1])
        temp_len -=1
        pointer1 += 1
      if pointer1 == len(lst1):
        checker1 = False
        break
      if pointer2 == len(lst2):
        checker2 = False
        break
      

    if checker1:
      n_lst += lst1[pointer1::]
    elif checker2:
      n_lst += lst2[pointer2::]
    return n_lst

  def mergeSort(self, arr):
    if len(arr) <= 1:
      return arr
    else:
      mid = len(arr)//2
      
      a1 = self.mergeSort(arr[:mid]) # the parameter
      a2 = self.mergeSort(arr[mid::]) # the parameter
 
      return self.merge(a1, a2) #the merge function 

p1 = Alien_height()
p1.mergeSort(arr)
outputt.write(f'{str(p1.t_count)}')


# In[ ]:




