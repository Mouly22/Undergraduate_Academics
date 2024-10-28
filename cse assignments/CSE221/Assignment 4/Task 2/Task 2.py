
inputt = open('input2_1.txt', 'r')
outputt = open('output2_1.txt', 'w')
line1 = inputt.readline()
line2 = inputt.readline()
arr = []
l1 = line2.split()

for m in l1:
    arr.append(int(m))


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid]) # the parameter
        a2 = mergeSort(arr[mid::]) # the parameter
        if a1 > a2:
            return a1
        else:
            return a2


store = mergeSort(arr)
outputt.write(f'{str(store[0])} ')

