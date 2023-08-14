import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.a = self.make_array(self.size)
    def make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def append(self,item):
        if self.n == self.size:
            self.resize(self.size*2)
        self.a[self.n]=item
        self.n+=1
    def pop(self):
        if self.n ==0:
            return f'Empty List'
        print(self.a[self.n-1])
        self.n = self.n-1
    def clear(self):
        self.size=1
        self.n =0
    def find(self,item):
        for i in range(self.n):
            if self.a[i] == item:
                return i
        return f'Value Error-value doesnot exist'
    def resize(self,new_size):
        b = self.make_array(new_size)
        self.size = new_size
        for i in range(self.n):
            b[i]=self.a[i]
        self.a=b
    def insert(self,index,item):
        if self.n == self.size:
            self.resize(self.size*2)
        for i in range(self.n,index,-1):
            self.a[i]=self.a[i-1]
        self.a[index]=item
        self.n+=1
    def remove(self,item):
        pos=self.find(item)
        if type(pos)== int:
            self.__delitem__(pos)
        else:
            return pos
    def __len__(self):
        return self.n
    def __str__(self):
        res =''
        for i in range(self.n):
            res=res+str(self.a[i])+','
        return '['+ res[:-1]+']'
    def __delitem__(self,pos):
        if 0<=pos<self.n:
            for i in range(pos,self.n-1):
                self.a[i]=self.a[i+1]
            self.n=self.n-1
        else:
            return f'Index Number is not correct'
    def __getitem__(self,index):
        if 0<=index<=self.n:
            return self.a[index]
        else:
            return f'Index Out of Range'
    def sort(self, reverse=False):
        for i in range(0, self.n):
            for j in range(i + 1, self.n):
                if reverse:
                    if self.a[i] <= self.a[j]:
                        self.a[j], self.a[i] = self.a[i], self.a[j]
                else:
                    if self.a[i]>= self.a[j]:
                         self.a[i],self.a[j] =self.a[j],self.a[i]
                     
        return self.a
    def min(self):
        if self.n ==0:
            return f'Empty String'
        mini = self.a[0]
        for i in range(self.n):
            if self.a[i] <= mini:
                mini = self.a[i]
        return mini
    def max(self):
        if self.n == 0:
            return f'Empty List'
        maxi = self.a[i]
        for i in range(self.n):
            if self.a[i]>=maxi:
                maxi = self.a[i]
        return maxi
    
    def sums(self):
        sumss=0
        for i in range(self.n):
            sumss+=self.a[i]
        return sumss
    def extend(self,lists):
        for i in lists:
            self.append(i)
    def convert_index(self,index):
        if - self.n <=index<=self.n:
            return index if index>=0 else self.n+index
        else:
            return None
    def neg_index(self,index):
        pos = self.convert_index(index)
        if pos is not None:
            return self.a[pos]
        else:
            return f'Invalid Index'
    def slicing(self,start=None,end=None):
        if start is None:
            return 0
        if end is None:
            return self.n
        else:
            return [self.a[i] for i in range(start,end)]
    def merge(self,lis1):
            merges = MeraList()
            merges.extend(self.a[:self.n])
            merges.extend(lis1)
            return merges
l = MeraList()
l.append(1)
l.append(2)
print(len(l))
print(l)
# l.append('hello')
print(l)
# l.pop()
# print(l)
print(l.find(2))
l.insert(1,4)
print(l)
# l.remove(4)
# print(l)
l.sort()
print(l)
print(l.min())
print(l.sums())
lis1=[1,2,3]
l.extend(lis1)
print(l)
print(l.neg_index(-1))
 # Accessing the last element using negative index
l1=l.slicing(1, 4)  # Slicing elements from index 1 to 5
print(l1)
lis1 = [1, 2, 3]
merged = l.merge(lis1)  # Merging l with lis1
print(merged)