inp1 = open('input1_2.txt', 'r')
out1 = open('output1_2.txt', 'w')


line1 = inp1.readline()
line2 = inp1.readline()
n1 = line1.split()
n2 = line2.split()
val = 0
flag = True
for elm in range(int(n1[0])):
    if flag:
        for x in range(elm+1, int(n1[0])):
            val = int(n2[elm]) + int(n2[x])
            if val == int(n1[1]):
                out1.write(f'{str(elm+1)} {str(x+1)}')
                flag = False
                break
if flag == True:
    out1.write('IMPOSSIBLE')
inp1.close()
out1.close()






