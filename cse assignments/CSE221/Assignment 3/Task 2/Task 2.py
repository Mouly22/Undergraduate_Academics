
inp3 = open('input3.txt', 'r')
out3 = open('output3.txt', 'w')
class Min_heap:
    def __init__(self, max_len):
        self.arry = [None] * max_len
        self.max_len = max_len
        self.size = 0
        self.lst = []

        
    def parent_def(self, idx):                #defining the parent range
        a = (idx - 1)//2
        return a >= 0
    
    def parent_val(self, idx):               #getting parent value
        a = (idx - 1)//2
        return self.arry[a]
    
    def leftnode_def(self, idx):
        b = 2 * idx+1
        if self.size > b:
            return b
        
    def leftnode(self, idx):
        b = 2 * idx+1
        return self.arry[b]
    
    def rightnode_def(self, idx):
        c = 2 * idx+2
        if self.size > c:
            return c
        
    def rightnode(self, idx):
        c = 2 * idx+2
        return self.arry[c]
    
    def add(self, vals):
        if self.size == self.max_len:
            print('No space')
        self.arry[self.size] = vals
        self.size += 1
        self.heapify_Up(self.size-1)
        
    
    def delete(self):
        min_val = self.arry[0]
        self.arry[0] = self.arry[self.size- 1]
        self.arry[self.size- 1] = None
        self.size -= 1
        self.sink(0)
        
        return min_val
    
    def swaping_values(self, id1, id2):
        store = self.arry[id1]
        self.arry[id1] = self.arry[id2]
        self.arry[id2] = store
    
    def heapify_Up(self, idx):
        p_idx = (idx - 1)//2
        if self.parent_def(idx) > self.arry[idx] and self.parent_val(idx) > self.arry[idx]:
            self.swaping_values(p_idx, idx)
            self.heapify_Up(p_idx)
            
    def sink(self, idx):
        l_idx = 2 * idx+ 1
        r_idx = 2 * idx + 2
        min_v = idx
        if self.leftnode_def(idx) and self.arry[min_v] > self.leftnode(idx):
            min_v = l_idx
        if self.rightnode_def(idx) and self.arry[min_v] > self.rightnode(idx):
            min_v = r_idx
            
        if min_v != idx:
            self.swaping_values(idx, min_v)
            self.sink(min_v)
            
            
    def heapSort(self): 
        for p in range(len(self.arry)):
            self.lst.append(self.delete())
        return self.lst



    def build(self):
        arr = []  
        val = Min_heap(10)
        line1 = inp3.readline()
        n2 = line1.split()

        for p in n2:
            val.add(int(p))

        while True:
            com_inp = input()
            if com_inp == 'A':
                store1 = int(input("Add new num: "))
                val.add(store1)

            elif com_inp == 'B':
                store2 = val.delete()
                out3.write(f'{str(store2)}\n')

            elif com_inp == 'S':
                arr = val.heapSort()
                for s in arr:
                    out3.write(f'{str(s)} ')

            break

va = Min_heap(10)  
va.build()
inp3.close()
out3.close()

