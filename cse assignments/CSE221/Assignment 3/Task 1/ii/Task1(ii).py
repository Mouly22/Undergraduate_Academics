
inp2 = open('input1(ii).txt', 'r')
out2 = open('output1(ii).txt', 'w')

def findk(arr, low, high, val):

    if val >= 0 and val <= high - low + 1:    #defining the bound of the val
        pi = partition(arr, low, high)        
        if pi - low == val - 1:
            return arr[pi]
        elif pi - low > val - 1:                #checking left side
            return findk(arr, low, pi-1, val)
        return findk(arr, pi+1, high, val-pi+low - 1)    #checking right side
    else:
        print('value of this index is not found')




def partition(arr, low, high):
    pivot = arr[high] # pivot (Element to be placed at right position)
    i =low - 1 # Index of smaller element and indicates the right position of pivot found so far

    for j in range (low, high):
        if arr[j] < pivot:
            i = i+1 # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i+1]
    return(i + 1)



arr = []
line1 = inp2.readline()
line2 = inp2.readline()
n2 = line1.split()
n4 = line2.split()
for p in n2:
    arr.append(int(p))
for q in n4:
    store = findk(arr, 0, len(arr)-1, int(q))
    out2.write(f'{str(store)}\n')

