def merge(a, b):
 # Here a and b are two sorted list
 # merge function will return a sorted list after merging a and b
    lst1 = a
    lst2 = b
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
        
    return n_lst

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr)//2
            a1 = mergeSort(arr[:mid]) # the parameter
            a2 = mergeSort(arr[mid::]) # the parameter
            return merge(a1, a2) #the merge function 


    store = mergeSort(arr)

    for elmes in store:
        outputt.write(f'{str(elmes)} ')





