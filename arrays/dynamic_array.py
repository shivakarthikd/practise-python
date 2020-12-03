import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n=0
        self.capacity=1
        self.Aarr= self.create_Array(self.capacity)

    def __len__(self):
        return self.n
    def __getitem__(self, k):
        if not 0<=k<self.n:
            return IndexError('K is out of bounds!')
        return self.Aarr[k]
    def append(self,ele):
        if self.capacity==self.n:
            self._resize(2*self.capacity)
        self.Aarr[self.n]=ele
        self.n += 1
    def _resize(self,new_cap):
        B=self.create_Array(new_cap)
        for k in range (self.n):
            B[k]=self.Aarr[k]
        self.Aarr=B
        self.capacity=new_cap
    def create_Array(self,new_cap):
        return (new_cap*ctypes.py_object)()



arrobj= DynamicArray()
arrobj.append(3)
arrobj.append(5)
arrobj.append(1)
arrobj.append(8)
print(arrobj[0])
print(len(arrobj))
