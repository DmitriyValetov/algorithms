import os


class Heap:
    """
    max-heap
    """

    def __init__(self):
        self.list = []
        

    def __len__(self):
        return len(self.list)


    def add(self, value):
        self.list.append(value)
        self.Sift_Up(len(self)-1)
    

    def Sift_Down(self, i):
        leftChild = 2*i+1
        rightChild = 2*i+2
        largest = i

        if leftChild >= len(self):
            return

        if rightChild < len(self):
            if self.list[i] > self.list[rightChild] and self.list[rightChild]<=self.list[leftChild]:
                largest = rightChild

            if self.list[i] > self.list[leftChild]  and self.list[rightChild]>=self.list[leftChild]:
                largest = leftChild

        else:
            if self.list[i] > self.list[leftChild]:
                largest = leftChild

        if largest == i:
            return 

        temp = self.list[i]
        self.list[i] = self.list[largest]
        self.list[largest] = temp

        self.Sift_Down(largest)


    def Sift_Up(self, i):
        if i == 0 or (self.list[i] < self.list[(i-1)//2]):
            return

        temp = self.list[i]
        self.list[i] = self.list[i//2]
        self.list[i//2] = temp

        self.Sift_Up(i//2)


    def buildHeap(self, arr, alg='insert'):
        if alg == 'insert': # -
            for el in arr:
                self.add(el)

        elif alg == 'sift_up': # -
            self.list = arr.copy()
            for i in range(len(self)):
                self.Sift_Up(i)

        elif alg == 'sift_down':
            self.list = arr.copy()
            for i in range(len(self)-1, -1, -1):
                self.Sift_Down(i)


    def changePriority(self, i, newValue):
        if self.list[i] > newValue:
            self.list[i] = newValue
            self.Sift_Up(i)
        else:
            self.list[i] = newValue
            self.Sift_Down(i)


    def __getitem__(self, key):
        return None


    def __setitem__(self, key, value):
        pass


    def pop(self):
        result = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop()
        self.Sift_Down(0)
        return result


    def ordered(self, descending=False):
        arr = []
        for _ in range(len(self)):
            arr.append(self.pop())

        if descending:
            return arr[::-1]
        return arr


    def __str__(self):
        return " ".join(map(str, self.ordered()))



if __name__ == "__main__":
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[1].split()))
    heap = Heap()
    heap.buildHeap(numbers, alg='sift_down')

    with open(file="output.txt", mode='w') as f:
        f.write(str(heap))