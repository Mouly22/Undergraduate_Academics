inp3 = open('input2_2.txt', 'r')
out3 = open('output2_2.txt', 'w')
val1 = []
line1 = inp3.readline()
line2 = inp3.readline()
line3 = inp3.readline()
line4 = inp3.readline()
n1 = line2.split()
n2 = line4.split()
for i in range(int(line1)):
    val = int(n1[i])
    val1.append(val)
for j in range(int(line3)):
    elms = int(n2[j])
    val1.append(elms)
s = sorted(val1)
for m in s:
    out3.write(f'{str(m)} ')

inp3.close()
out3.close()




