__author__ = 'Dennis Qiu'
from node import Node
from aqueue import Queue

class Deque(Queue):
    def __init__(self):
        """
        Instantiates three elements, self.head and self.tail, which are nodes
        corresponding to the lower and upper bounds of the deque, respectively,
        and self.size.
        """
        super().__init__()
        print('created Deque')

    def peek_back(self):
        if self.tail:
            return self.tail.data

    def enqueue_front(self, item):
        """
        Adds an element to the front of the deque.
        :param item: to add to the front of the deque.
        """
        new_head = Node(item)
        if self.is_empty():
            self.head = new_head
            self.tail = new_head
        else:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        self.size += 1

    def dequeue_back(self):
        if self.is_empty():
            raise IndexError('attempted dequeue_back on an empty deque')
        data = self.tail.data
        if self.tail.prev:
            self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return data

def test_inherited():
    items = ['first one', 5, 10, 15, 20, 'last one']
    inherit_score = 0
    d = Deque()
    s = "d = Deque(), is empty? {} Let's peek: d.peek() returns {}".format(d.is_empty(), d.peek())
    if s == "d = Deque(), is empty? True Let's peek: d.peek() returns None":
        inherit_score += 30
    for i, item in enumerate(items):
        d.enqueue(item)
    else:
        inherit_score += 10
    for i in range(d.size):
        d.dequeue()
    else:
        inherit_score += 10
    try:
        d.dequeue()
    except IndexError:
        inherit_score += 10
    except Exception as e:
        print('Unexpected error:', e)
    print('Inheritance score = {}/60'.format(inherit_score))
    return inherit_score

def main():
    score = 0
    people = [
        'Thorin', 'Dwalin', 'Balin', 'Gloin', 'Kili', 'Fili',
        'Dori', 'Nori', 'Ori', 'Oin', 'Bifur', 'Bombur', 'Bofur'
    ]
    d = Deque()
    print('enqueuing in the front')
    for i, item in enumerate(people):
        d.enqueue_front(item)
        print(i, item, end=', ')
        if d.size != i + 1:
            break
    else:
        score += 8
    back = d.peek_back()
    print('\nafter enqueuing {} items, peek_back: {} == {}? {}'.format(d.size, back, people[0], back == people[0]))
    if back == 'Thorin':
        score += 8
        if d.size == 13:
            score += 8
    print('dequeuing {} items from the back'.format(d.size))
    for i in range(d.size):
        item = d.dequeue_back()
        print(i, item, end=', ')
        if d.size != len(people) - i - 1:
            break
    else:
        score += 8
    try:
        print('\nd.dequeue() returns {}'.format(d.dequeue()))
        print('\nSHOULD NOT PRINT 2nd attempt on empty deque, d.dequeue() returns {}'.format(d.dequeue()))
    except IndexError as ie:
        print(ie)
        score += 8
    except Exception as e:
        print('Unexpected error:', e)
    print('Added features score = {}/40'.format(score))
    return score

if __name__ == '__main__':
    inheritance_score = test_inherited()
    total_score = main() + inheritance_score
    print('The Deque ancestor tree, officially known as the Method Resolution Order or MRO:\n\t{}'.format(Deque.__mro__))
    print('Deque Score: {}/100'.format(total_score))
