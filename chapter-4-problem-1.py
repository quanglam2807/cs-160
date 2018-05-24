# Quang Lam

import datetime
import random
import time

class PyList:
    def __init__(self,contents=[], size=10):
        # The contents allows the programmer to construct a list with
        # the initial contents of this value. The initial_size
        # lets the programmer pick a size for the internal size of the
        # list. This is useful if the programmer knows he/she is going
        # to add a specific number of items right away to the list.
        self.items = [None] * size
        self.numItems = 0
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self,index):
        if index < self.numItems:
            return self.items[index]

        raise IndexError("PyList index out of range")

    def __setitem__(self,index,val):
        if index < self.numItems:
            self.items[index] = val
            return

        raise IndexError("PyList assignment index out of range")

    def insert(self,i,e):
        if self.numItems == self.size:
            self.__makeroom()

        if i < self.numItems:
            for j in range(self.numItems-1,i-1,-1):
                self.items[j+1] = self.items[j]

            self.items[i] = e
            self.numItems += 1
        else:
            self.append(e)


    def __add__(self,other):
        result = PyList()

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(other.numItems):
            result.append(other.items[i])

        return result


    def __contains__(self,item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True

        return False

    def __delitem__(self,index):
        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        self.numItems -= 1 # same as writing self.numItems = self.numItems - 1

    def __eq__(self,other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False

        return True

    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

    def __len__(self):
        return self.numItems

    # This method is hidden since it starts with two underscores.
    # It is only available to the class to use.
    def __makeroom(self):
        # increase list size by 1/4 to make more room.
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.size = newlen

    def append(self,item):
        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems] = item
        self.numItems += 1 # Same as writing self.numItems = self.numItems + 1

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "]"
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s

    def _select(self, start):
        minIndex = start

        for j in range(start + 1,  self.numItems):
            if self.items[minIndex] > self.items[j]:
                minIndex = j

        return minIndex

    def selSort(self):
        for i in range(self.numItems - 1):
            minIndex = self._select(i)
            tmp = self.items[i]
            self.items[i] = self.items[minIndex]
            self.items[minIndex] = tmp

    def _merge(self, start, mid, stop):
        lst = []
        i = start
        j = mid

        while i < mid and j < stop:
            if (self.items[i] < self.items[j]):
                lst.append(self.items[i])
                i += 1
            else:
                lst.append(self.items[j])
                j += 1

        while i < mid:
            lst.append(self.items[i])
            i += 1

        for i in range(len(lst)):
            self.items[start + i] = lst[i]

    def _mergeSortRecursively(self, start, stop):
        if start >= stop - 1:
            return

        mid = (start + stop) // 2

        self._mergeSortRecursively(start, mid)
        self._mergeSortRecursively(mid, stop)
        self._merge(start, mid, stop)

    def mergeSort(self):
        self._mergeSortRecursively(0, self.numItems)

    def _partition(self, start, stop):
        pivotIndex = start
        pivot = self.items[pivotIndex]
        i = start + 1
        j = stop - 1

        while i <= j:
            while i <= j and not pivot < self.items[i]:
                i += 1
            while i <= j and pivot < self.items[j]:
                j -= 1

            if i < j:
                tmp = self.items[i]
                self.items[i] = self.items[j]
                self.items[j] = tmp
                i += 1
                j -= 1

        self.items[pivotIndex] = self.items[j]
        self.items[j] = pivot

        return j

    def _quickSortRecursively(self, start, stop):
        if (start >= stop - 1):
            return

        pivotIndex = self._partition(start, stop)

        self._quickSortRecursively(start, pivotIndex)
        self._quickSortRecursively(pivotIndex + 1, stop)

    def quickSort(self):
        for i in range(self.numItems):
            j = random.randint(0, self.numItems - 1)
            tmp = self.items[i]
            self.items[i] = self.items[j]
            self.items[j] = tmp

        self._quickSortRecursively(0, self.numItems)

def main():

    # Test list of size 1000 to 100000.
    xmin = 1000
    xmax = 10000

    # Record the string sizes in xList
    #  and the average access time to compare the strings in yList
    xList = []
    yQuickSortList = []
    yMergeSortList = []
    ySelSortList = []

    for x in range(xmin, xmax+1, 1000):
        xList.append(x)

        arr = [random.randint(0, x) for i in range(x)]

        # Quick Sort
        lst = PyList(arr)
        starttime = datetime.datetime.now()
        lst.quickSort()
        quickSortTime = (datetime.datetime.now() - starttime).total_seconds() * 1000
        yQuickSortList.append(quickSortTime)

        # Merge Sort
        lst = PyList(arr)
        starttime = datetime.datetime.now()
        lst.mergeSort()
        mergeSortTime = (datetime.datetime.now() - starttime).total_seconds() * 1000
        yMergeSortList.append(mergeSortTime)

        # Selection Sort
        lst = PyList(arr)
        starttime = datetime.datetime.now()
        lst.selSort()
        selSortTime = (datetime.datetime.now() - starttime).total_seconds() * 1000
        ySelSortList.append(selSortTime)

    # Write an XML file with the results
    file = open("Sort.xml","w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    file.write('<Plot title="Sort Algorithm Comparison">\n')

    file.write('  <Axes>\n')
    file.write('    <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">List Size</XAxis>\n')
    file.write('    <YAxis min="'+str(0)+'" max="'+str(max(ySelSortList))+'">Microseconds</YAxis>\n')
    file.write('  </Axes>\n')

    file.write('  <Sequence title="Quick Sort" color="red">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yQuickSortList[i])+'"/>\n')

    file.write('  </Sequence>\n')

    file.write('  <Sequence title="Merge Sort" color="blue">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(yMergeSortList[i])+'"/>\n')

    file.write('  </Sequence>\n')

    file.write('  <Sequence title="Selection Sort" color="green">\n')

    for i in range(len(xList)):
        file.write('    <DataPoint x="'+str(xList[i])+'" y="'+str(ySelSortList[i])+'"/>\n')

    file.write('  </Sequence>\n')

    file.write('</Plot>\n')
    file.close()


if __name__ == "__main__":
    main()
