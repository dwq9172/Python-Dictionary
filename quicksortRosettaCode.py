def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more
 

def main():
    import timeit
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print("Running 1,000,000 loops, each sorting {} using quickSort takes".format(a))
    print(timeit.timeit("quickSort({})".format(a),setup="from __main__ import quickSort"), "microseconds per loop.")
    print("Return value from quickSort(a): {}\n\tOriginal list after quickSort: {}.".format(quickSort(a), a))
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print("Running 1,000,000 loops, each sorting {} using quickSortText takes".format(a))
    print(timeit.timeit("quickSortText({})".format(a),setup="from __main__ import quickSortText, quickSortHelper, partition"),
          "microseconds per loop.")
    print("Return value from quickSortText(a): {}\n\tOriginal list after quickSortText: {}.".format(quickSortText(a),a))
    


def quickSortText(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark


if __name__ == '__main__':
    main()
