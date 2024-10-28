inp_fle = open('input2_3.txt', 'r')
out_fle = open('output2_3.txt', 'w')
line1 = inp_fle.readline()
line2 = inp_fle.readline()
line3 = inp_fle.readline()
line4 = inp_fle.readline()

l1 = line2.split()
lst1 = []
lst2 = []
for m in l1:
    lst1.append(int(m))
l2 = line4.split()
for n in l2:
    lst2.append(int(n))

pointer1 = 0
pointer2 = 0
n_lst = []
checker1 = True
checker2 = True
while True:
    if lst1[pointer1] > lst2[pointer2]:
        n_lst.append(lst2[pointer2])
        pointer2 += 1 
    else:
        n_lst.append(lst1[pointer1])
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

for k in n_lst:
    out_fle.write(f'{str(k)} ')
inp_fle.close()
out_fle.close()





