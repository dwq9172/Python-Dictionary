__author__ = 'Dennis Qiu'
from node import Node

class Queue:
    """
       A Queue(builtins.object).
       The Queue class is a FIFO data structure.
       Contains three fields in the constructor method:
           head
           tail
           size
       Contains 4 methods, all running in constant time:
           constructor
           is_empty
           peek
           enqueue
           dequeue
       """
    def __init__(self):
        """
        Initializes Queue.
        :return: reference for self
        """
        self.head = None
        self.tail = self.head
        self.size = 0
        print('created Queue')

    def is_empty(self):
        """
        Checks size of queue.
        :return: True if size is empty, otherwise False
        """
        if self.size == 0:
            return True
        return False

    def peek(self):
        """
        Looks at item on top of queue.
        :return: Top item on queue.
        """
        if self.head:
            return self.head.data

    def enqueue(self, item):
        """
        Places item on back of queue.
        :param item: object to be added to back.
        :return: None
        """
        newNode = Node(item)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        """
        Removes item at front of queue.
        :return: item at the front of queue.
        """
        rmve = self.head
        if (self.size == 0):
            raise IndexError('Attempting to dequeue from empty queue')
        else:
            self.head = self.head.next
            self.size -= 1
        return rmve

def main():
    items = ['first one', 5, 10, 15, 20, 'last one']
    score = 0
    q = Queue()
    s = "q = Queue(), is empty? {} Let's peek: q.peek() returns {}".format(q.is_empty(), q.peek())
    print("q = Queue(), is empty? {} Let's peek: q.peek() returns {}".format(q.is_empty(), q.peek()))
    if s == "q = Queue(), is empty? True Let's peek: q.peek() returns None":
        score += 29
        s = ''
    print('enqueuing')
    for i, item in enumerate(items):
        q.enqueue(item)
        print(i, item)
    else:
        score += 13
        if q.size != 6:
            score -= 5
    print('dequeuing {} items'.format(q.size))
    for i in range(q.size):
        item = q.dequeue()
        print(i, item)
    else:
        score += 11
    try:
        print(q.dequeue())
    except IndexError as ie:
        print(ie)
        score += 7
    except Exception as e:
        print('Unexpected error:', e)
    print('Score = {}/60'.format(score))

if __name__ == '__main__':
    main()
