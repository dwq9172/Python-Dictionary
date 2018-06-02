__author__ = 'Dennis Qiu'
import time

def main():
    d = dictionary()
    print('Completed reading in', len(d), 'words to the list.')
    print('The first word in the dictionary list is:', d[0])
    print('\t')

    print('SORTING UNSORTED LIST')
    d1 = list(d)
    print('The first word is: {}'.format(d1[0]))
    start = time.clock()
    qsorted = quickSort(d1)
    stop = time.clock()
    print('quickSort takes: {:6f} microseconds'.format(stop-start))
    print('The first word after quickSort sorting is: {}'.format(qsorted[0]))
    print('\t')

    d1 = list(d)
    print('The first word is: {}'.format(d1[0]))
    start = time.clock()
    quickSortText(d1)
    stop = time.clock()
    print('quickSortText takes: {:6f} microseconds'.format(stop-start))
    print('The first word after quickSortText sorting is: {}'.format(d1[0]))
    print('\t')

    d1 = list(d)
    print('The first word is: {}'.format(d1[0]))
    start = time.clock()
    mergeSort(d1)
    stop = time.clock()
    print('mergeSort takes: {:6f} microseconds'.format(stop-start))
    print('The first word after mergeSort sorting is: {}'.format(d1[0]))
    print('\t')

    d1 = list(d)
    print('The first word is: {}'.format(d1[0]))
    start = time.clock()
    msorted = mergesort(d1, 0, len(d1))
    stop = time.clock()
    print('mergesort takes: {:6f} microseconds'.format(stop-start))
    print('The first word after mergesort sorting is: {}'.format(msorted[0]))
    print('\t')

    print('SORTING SORTED LIST')
    d1 = list(msorted)
    start = time.clock()
    try:
        qsorted = quickSort(d1)
    except RecursionError as e:
        print('quickSort returns error: {}'.format(e))
    else:
        stop = time.clock()
        print('quickSort takes: {:6f} microseconds'.format(stop - start))
        print('The first word after quickSort sorting is: {}'.format(qsorted[0]))
    print('\t')

    d1 = list(msorted)
    start = time.clock()
    try:
        quickSortText(d1)
    except RecursionError as e:
        print('quickSortText returns error: {}'.format(e))
    else:
        stop = time.clock()
        print('quickSortText takes: {:6f} microseconds'.format(stop - start))
        print('The first word after quickSortText sorting is: {}'.format(d1[0]))
    print('\t')

    d1 = list(msorted)
    start = time.clock()
    try:
        mergeSort(d1)
    except RecursionError as e:
        print('mergeSort returns error: {}'.format(e))
    else:
        stop = time.clock()
        print('mergeSort takes: {:6f} microseconds'.format(stop - start))
        print('The first word after mergeSort sorting is: {}'.format(d1[0]))
    print('\t')

    d1 = list(msorted)
    start = time.clock()
    try:
        msorted = mergesort(d1, 0, len(d1))
    except RecursionError as e:
        print('mergesort returns error: {}'.format(e))
    else:
        stop = time.clock()
        print('mergesort takes: {:6f} microseconds'.format(stop - start))
        print('The first word after mergesort sorting is: {}'.format(msorted[0]))

def dictionary():
    dic_list = []
    with open('dictionary.txt', 'r', encoding='UTF-8') as words:
        for line in words.readlines():
            dic = line.strip()
            dic_list.append(dic)
    return dic_list

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

def mergeSort(alist):
   if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]: 
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j = j+1
            k = k+1

def mergesort(arr, left, right):
    if right-left == 1:
        return [arr[left]]

    mid = left + (right-left) // 2
    leftarr    = mergesort(arr, left, mid)
    rightarr   = mergesort(arr, mid, right)

    arr = leftarr + rightarr

    mid -= left 
    right -= left
    i = 0
    j = mid
    c = []

    while i < mid and j < right:
        if arr[i] <= arr[j]:
            c.append(arr[i])
            i+=1
        else:
            c.append(arr[j]) 
            j+=1

    for k in range(i,mid):
        c.append(arr[k])

    for k in range(j,right):
        c.append(arr[k])

    return c 

if __name__ == '__main__':
    main()
    
