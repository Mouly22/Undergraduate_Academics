

inp1 = open('/Users/mouly/Downloads/input1a_2.txt', 'r')
out1 = open('/Users/mouly/Downloads/output1a_2.txt', 'w')
line1 = inp1.readline()
line1 = line1.split()
store = int(line1[0])
lst1 = [0]*(store+1)
lst2 = [0]*(store+1)

for x in range(len(lst2)):
    lst2[x] = lst1.copy()

for i in range(int(line1[1])):
    lines = inp1.readline()
    elem = lines.split()
    
    lst2[int(elem[0])][int(elem[1])] = int(elem[2])

val = ''
for p in lst2:
    for q in p:
    
        val += str(q)+' '
    val += '\n'
out1.write(val)


inp1.close()
out1.close()






