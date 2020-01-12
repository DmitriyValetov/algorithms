import os


class Heap:
    """
    max-heap
    """

    def __init__(self, type='min'):
        if type not in ['min', 'max']:
            raise ValueError(f'invalid heap type: {type}')

        self.type=type # min/max
        self.list = []
        

    def __len__(self):
        return len(self.list)


    def add(self, value):
        self.list.append(value)
        self.Sift_Up(len(self)-1)
    

    def Sift_Down(self, i):
        leftChild = 2*i+1
        rightChild = 2*i+2
        toReplace = i

        if leftChild >= len(self):
            return

        if rightChild < len(self):
            if self.type == 'min':
                if self.list[i] > self.list[rightChild] and self.list[rightChild]<=self.list[leftChild]:
                    toReplace = rightChild

                if self.list[i] > self.list[leftChild]  and self.list[rightChild]>=self.list[leftChild]:
                    toReplace = leftChild
            else:
                if self.list[i] < self.list[rightChild] and self.list[rightChild]>=self.list[leftChild]:
                    toReplace = rightChild

                if self.list[i] < self.list[leftChild]  and self.list[rightChild]<=self.list[leftChild]:
                    toReplace = leftChild

        else:
            if self.type == 'min':
                if self.list[i] > self.list[leftChild]:
                    toReplace = leftChild
            else:
                if self.list[i] < self.list[leftChild]:
                    toReplace = leftChild

        if toReplace == i:
            return 

        temp = self.list[i]
        self.list[i] = self.list[toReplace]
        self.list[toReplace] = temp
        self.Sift_Down(toReplace)


    def Sift_Up(self, i):
        if ( (i == 0) or 
             (self.type == 'min' and self.list[i] > self.list[(i-1)//2]) or 
             (self.type == 'max' and self.list[i] < self.list[(i-1)//2]) ):
            return

        temp = self.list[i]
        self.list[i] = self.list[(i-1)//2]
        self.list[(i-1)//2] = temp

        self.Sift_Up((i-1)//2)


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


    def pop(self):
        result = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop() # last
        self.Sift_Down(0)
        return result


    def ordered(self, descending=False):
        arr = []
        for _ in range(len(self)):
            arr.append(self.pop())

        if (self.type == 'min' and descending) or (self.type == 'max' and not descending):
            return arr[::-1]
        return arr


    def __str__(self):
        return " ".join(map(str, self.ordered()))


def sort1():
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[1].split()))
    heap = Heap(type='min')
    heap.buildHeap(numbers, alg='sift_down')

    with open(file="output.txt", mode='w') as f:
        f.write(str(heap))


def sort2():
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[1].split()))
    heap = Heap(type='max')
    heap.buildHeap(numbers, alg='sift_down')

    with open(file="output.txt", mode='w') as f:
        f.write(str(heap))


def insert_extract_promo():
    # ok, but too slow
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = []
    extracted = []
    for line in lines[1:]:
        if line[0] == '0':
            new_number = int(line.split()[1])
            numbers.append(new_number)
            numbers.sort(reverse=True)
        elif line[0] == '1':
            extracted.append(numbers.pop(0))

    with open(file="output.txt", mode='w') as f:
        f.write(" ".join(map(str, extracted)))    


def insert_extract():
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    # numbers = []
    extracted = []
    heap = Heap(type='max')
    for line in lines[1:]:
        if line[0] == '0':
            new_number = int(line.split()[1])
            # numbers.append(new_number)
            # numbers.sort(reverse=True)
            heap.add(new_number)
            # if heap.list[0] != numbers[0]:
            #     print('error after add')
        elif line[0] == '1':
            extracted.append(heap.pop())
            # if extracted[-1] != numbers.pop(0):
            #     print('error after extract')

    with open(file="output.txt", mode='w') as f:
        f.write(" ".join(map(str, extracted)))


if __name__ == "__main__":
    # sort1()
    insert_extract()
    # insert_extract_promo()