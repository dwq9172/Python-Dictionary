__author__ = 'Bradley N. Miller, David L. Ranum modified by: Dennis Qiu'
from urllib.request import urlopen
from time import clock

class BinHeap:
    """
     A BinHeap(builtins.object).
       Contains two fields in the constructor method:
           heapList
           currentSize
       Contains 6 methods, all running in constant time:
           constructor
           percUp
           insert
           percDown
           minChild
           delMin
           buildHeap
    """
    def __init__(self):
        """
        Initializes BinHeap.
        :return: reference for self
        """
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,i):
        """
        Percolates a new item as far up in the tree as it
        needs to go to maintain the heap order.
        :param i: index value
        :return: None
        """
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
          
    def insert(self,k):
        """
        Adds a new item to the heap.
        :param k: new item
        :return: None
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
  
    def percDown(self,i):
        """
        Percolates a new item as far down in the tree as it
        needs to go to maintain the heap order.
        :param i: index value
        :return: None
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        """
        Helper to percDown.
        :param i: index value
        :return: Returns left child index, otherwise i*2, otherwise right child index.
        """
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
          
    def delMin(self):
        """
        Decrements size(currentSize) of list.
        :return: Returns the item with the minimum key value,
                 removing the item from the heap.
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
  
    def buildHeap(self,alist):
        """
        Builds a new heap from a list of keys.
        :param alist: the list of keys (dictionsary.txt for example)
        :return: None
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

def main():
    d = urlopen('http://people.uncw.edu/tompkinsj/231/resources/dictionary.txt').read().split()
    print(len(d), 'words beginning with {}.'.format(d[0].decode()))
    bh = BinHeap()
    print('\t')

    import math
    sorted_d = []
    start = clock()
    bh.buildHeap(d)
    for i in range(len(d)):
        sorted_d.append(bh.delMin())
    stop = clock()
    time1 = stop-start
    print(len(d), 'words sorted in {:6f} seconds.'.format(stop-start))
    print('The first word after sorting the list is: {}'.format(sorted_d[0].decode()))
    next_expected_time = time1/10/math.log(len(d))*math.log(len(d)//10)
    print('The expected time for 10x smaller list is {:6f} seconds.'.format(next_expected_time))
    print('\t')

    sorted_d = []
    start = clock()
    bh.buildHeap(d[:len(d)//10])
    for i in range(len(d[:len(d)//10])):
        sorted_d.append(bh.delMin())
    stop = clock()
    time1 = stop-start
    print(len(d[:len(d)//10]), 'words sorted in {:6f} seconds.'.format(stop - start))
    sorted_d = []
    start = clock()
    bh.buildHeap(d[:len(d) // 100])
    for i in range(len(d[:len(d) // 100])):
        sorted_d.append(bh.delMin())
    stop = clock()
    print(len(d[:len(d) // 100]), 'words sorted in {:6f} seconds.'.format(stop - start))
    print('The first word after sorting the list is: {}'.format(sorted_d[0].decode()))
    next_expected_time = time1/10/math.log(len(d)//10)*math.log(len(d)//100)
    print('The expected time for 10x smaller list is {:6f} seconds.'.format(next_expected_time))

if __name__ == '__main__':
    main()
