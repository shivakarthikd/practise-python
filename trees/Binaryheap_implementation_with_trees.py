class BinaryHeap:
    def __init__(self):
        self.heap=[0]
        self.size=0

    def __percolate(self,i):

        while i//2:
            if self.heap[i]<self.heap[i//2]:
                temp=self.heap[i]
                self.heap[i]=self.heap[i//2]
                self.heap[i//2]=temp
            i=i//2

    def insert(self,key):
        self.heap.append(key)
        self.size=self.size+1
        self.__percolate(self.size)

    def __percDown(self,i):
        if i*2 +1 < self.size:
            return i*2
        else:
            while i < self.size:
                t=self.heap[i]
                self.heap[i]=self.heap[i*2]
                self.heap[i*2]=t
                i=i*2



    def deleteMin(self):
        temp=self.heap[1]
        self.heap[1]=self.heap[self.size]
        self.size=self.size-1
        self.heap.pop()
        self.__percDown(1)
        return temp


r=BinaryHeap()
r.insert(4)
r.insert(10)
r.insert(12)
r.insert(5)
r.insert(8)
print(r.heap)

r.deleteMin()
print(r.heap)

/