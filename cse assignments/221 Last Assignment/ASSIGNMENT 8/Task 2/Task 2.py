

inp82 = open('/Users/mouly/Downloads/input2_4.txt', 'r')
out82 = open('/Users/mouly/Downloads/output2_4.txt', 'w')
def frog(num):
    lst = [None] *(num+1)
    lst[0] = 1
    lst[1] = 1
    lst[2] = 2
    for elm in range(3,num+1):
        lst[elm] = lst[elm-1] + lst[elm-2]
    return lst[num]
line1 = inp82.readline()
out82.write(str(frog(int(line1))))
out82.close()


