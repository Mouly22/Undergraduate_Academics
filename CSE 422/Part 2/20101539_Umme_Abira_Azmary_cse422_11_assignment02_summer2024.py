f1 = open('20101539_Umme Abira Azmary_CSE422_11_Assignment02_Summer2024_InputFile.txt', 'r')
import random
line1 = f1.readline().split()
v1 = []
v2 = []
for p in line1[0]:
  v1.append(int(p))
for q in line1[1]:
  v2.append(int(q))
v = []
v.append(v1)
v.append(v2)

def DMutate(c_lst):
    mutateChild = []
    l1 = []
    l2 = []
    l3 = []
    indx1 = random.randint(2,3)
    indx2 = random.randint(6,7)
    for x in c_lst:
   
      f1first = x[0:indx1]
      l1.append(f1first)

 
      f1middle = x[indx1:indx2]
      l2.append(f1middle)

      f1rest = x[indx2::]
      l3.append(f1rest)

    chromo1 = l1[0]+l2[1]+l3[0]
    mutateChild.append(chromo1)
    chromo2 = l1[1] + l2[0] + l3[1]
    mutateChild.append(chromo2)

    return mutateChild

output = DMutate(v)

finaloutputstring = ""
for big in output:
    for i in big:
        finaloutputstring += str(i)
    finaloutputstring += " "

print(finaloutputstring)
   
   