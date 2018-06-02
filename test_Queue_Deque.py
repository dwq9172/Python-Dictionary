__author__ = 'Dennis Qiu'
from aqueue import Queue
from deque import Deque

def test_queue():
    items = ['first one', 5, 10, 15, 20, 'last one']
    score = 0
    q = Queue()
    s = "q = Queue(), is empty? {} Let's peek: q.peek() returns {}".format(q.is_empty(), q.peek())
    print("q = Queue(), is empty? {} Let's peek: q.peek() returns {}".format(q.is_empty(), q.peek()))
    if s == "q = Queue(), is empty? True Let's peek: q.peek() returns None":
        score += 29
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
    print('Queue score = {}/60'.format(score))
    return score

def test_inherited():
    items = ['first one', 5, 10, 15, 20, 'last one']
    inherit_score = 0
    d = Deque()
    s = "d = Queue(), is empty? {} Let's peek: d.peek() returns {}".format(d.is_empty(), d.peek())
    if s == "d = Queue(), is empty? True Let's peek: d.peek() returns None":
        inherit_score += 29
    for i, item in enumerate(items):
        d.enqueue(item)
    else:
        inherit_score += 13
    for i in range(d.size):
        d.dequeue()
    else:
        inherit_score += 11
    try:
        d.dequeue()
    except IndexError:
        inherit_score += 7
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
        score += 11
    back = d.peek_back()
    print('\nafter enquing {} items, peek_back: {} == {}? {}'.format(d.size, back, people[0], back == people[0]))
    if back == 'Thorin':
        score += 5
        if d.size == 13:
            score += 7
    print('dequeuing {} items from the back'.format(d.size))
    for i in range(d.size):
        item = d.dequeue_back()
        print(i, item, end=', ')
        if d.size != len(people) - i - 1:
            break
    else:
        score += 9
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
    queue_score = test_queue()
    inheritance_score = test_inherited()
    total_score = main() + queue_score - (max(queue_score, inheritance_score) - min(queue_score, inheritance_score))
    print('Overall Score: {}/100'.format(total_score))
