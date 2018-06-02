__author__ = 'Dennis Qiu'

class Node:
    """
    The Node class has 3 instance variables:
        item: The referenced item.
        next: The next node in the line.
    """
    def __init__(self, item=None):
        """
        The constructor sets fields data to item, next and prev to None.
        :return: The reference for self, item.
        """
        self.data = item
        self.next = None
        self.prev = None

    def get_data(self):
        """
        :return: data
        """
        return self.data

    def get_next(self):
        """
        :return: reference to the next node
        """
        return self.next

    def get_prev(self):
        """
        :return: reference to the previous node
        """
        return self.prev

    def set_data(self,item):
        """
        sets the data
        """
        self.data = item

    def set_next(self,newnext):
        """
        sets the reference to the next node
        """
        self.next = newnext

    def set_prev(self,newnext):
        """
        sets the reference to the previous node
        """
        self.prev = newnext

def main():
    print('prev <= data => next')
    n1 = Node()
    n2 = Node()
    n3 = Node(89)
    n1.set_data(23)
    n2.set_data(56)
    print('three nodes, n1 = {}, n2 = {}, and n3 = {}'.format(n1.get_data(), n2.get_data(), n3.get_data()))
    print('changing n1 data to {1}. Happy birthday n1!'.format(n1.set_data(24), 24))
    print('n1 is at {}\nn2 is at {}\nn3 is at {}'.format(n1, n2, n3))
    print('connecting the three nodes, \n\tn1 next=> n2 next=> n3, \n\tn1 <= prev n2 <= prev n3')
    n1.set_next(n2)
    n2.set_prev(n1)
    n2.set_next(n3)
    n3.set_prev(n2)
    print(" "*39,'{} {} {}'.format(n1.get_prev(), n1.get_data(), n1.get_next()))
    print(n2.get_prev(), n2.get_data(), n2.get_next())
    print(n3.get_prev(), n3.get_data(), n3.get_next())
    
if __name__ == '__main__':
    main()
