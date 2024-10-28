inp2 = open('input1_1.txt', 'r')
out2 = open('output1_1.txt', 'w')

line1 = inp2.readline()
line2 = inp2.readline()
n1 = line1.split()
n2 = line2.split()
dct = {}
count = 0
flag = True
if flag:
    for elm in range(int(n1[0])):
        vals = int(n1[1]) - int(n2[elm])
        if vals not in dct.keys():
            dct[int(n2[elm])] = count
            
        else:
            out2.write(f'{str(dct[vals]+1)} {str(count+1)}')
            
            flag = False
            break
        count += 1
if flag == True:
    out2.write('IMPOSSIBLE')





