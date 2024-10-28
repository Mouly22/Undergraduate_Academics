
inp1 = open('input1(i).txt', 'r')
out1 = open('output1(i).txt', 'w')
  
# low –> Starting index, high –> Ending index */
def quickSort(arr, low, high):
    if (low < high): # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1) # Before pi
        quickSort(arr, pi + 1, high) # After pi


# This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot
def partition(arr, low, high):

    pivot = arr[high] # pivot (Element to be placed at right position)
    i =low - 1 # Index of smaller element and indicates the right position of pivot found so far

    for j in range (low, high):

        if arr[j] < pivot:
            i=i+1 # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]


    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return(i + 1)

arr = []
line1 = inp1.readline()
n1 = line1.split()
for i in n1:
    arr.append(int(i))
quickSort(arr, 0, 7)
out1.write(str(arr))

