__author__ = 'Dennis Qiu'
from treeNode import TreeNode

class BinarySearchTree(TreeNode):
    """
    Description:  Implement a binary search tree with the following interface
                  functions:
                  __contains__(y) <==> y in x
                  __getitem__(y) <==> x[y]
                  __init__()
                  __len__() <==> len(x)
                  __setitem__(k,v) <==> x[k] = v, raises KeyError Exception
                  clear()
                  get(k)
                  height()
                  items()
                  keys()
                  values()
                  put(k,v)
                  in
                  del <==>
    """
    def __init__(self):
        """
        Initializes BinarySearchTree.
        :return: reference for self
        """
        self.root = None
        self.size = 0

    def __contains__(self, key):
        """
        Simply calls get.
        Impliments in operation, and overloads in operator
        :param key: index of list in BinarySearchTree
        :return: Return True if get returns a value, or False if it returns None
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def __getitem__(self, key):
        """
        Same logic as __setitem__.
        Calls get() method.
        :param key: indice of list in BinarySearchTree
        :return: key(a node in tree)
        """
        return self.get(key)

    def __len__(self):
        """
        Length of list
        :return: Instance that returns length of list
        """
        return self.size

    def __iter__(self):
        """

        :return:
        """
        return self.root.__iter__()

    def __setitem__(self, k, v):
        """
        v raises KeyError Exception.
        Calls put() method.
        Overloads [] operator to allow access for writing statements
        :param k: indices of list in BinarySearchTree
        :param v: additional info contained in a node
        :return: None
        """
        self.put(k, v)

    def clear(self):
        """
        Removes all items from list.
        Empties (clears) tree by re-setting root to None and size to 0
        :return: None
        """
        self.root = None
        self.size = 0

    def get(self, key):
        """
        Same logic as put() method.
        :param key: index of list in BinarySearchTree
        :return: Returns payload, otherwise none/nothing else
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """
        Same logic as _put() method.
        :param key: index of list in BinarySearchTree
        :param currentNode: node that is currently compared to in tree
        :return:
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def height(self, node):
        """
        Height of tree root
        :param node: root node
        :return: height of tree
        """
        if not self.root:
            return 0
        else:
            return node.height(node)

    def items(self):
        """

        :return:
        """
        Nodes = []
        if not self.root:
            return None
        else:
            self._items(Nodes, self.root)
            while None in Nodes:
                Nodes.remove(None)
            return Nodes

    def _items(self, items, node):
        if node == None:
            return
        else:
            items.append(node)
            if node.hasLeftChild:
                items.append(self._items(items, node.leftChild))
            if node.hasRightChild:
                items.append(self._items(items, node.rightChild))

    def keys(self):
        """
        Keys in list, or nodes in tree
        :return: None
        """
        Keys = []
        if self.root != None:
            self._keys(Keys, self.root)
            while None in Keys:
                Keys.remove(None)
            return Keys
        else:
            return None

    def _keys(self, allkeys, node):
        """

        :param allkeys:
        :param node:
        :return:
        """
        if node == None:
            return
        else:
            allkeys.append(node.key)
            if node.hasLeftChild:
                allkeys.append(self._keys(allkeys, node.leftChild))
            if node.hasRightChild:
                allkeys.append(self._keys(allkeys, node.rightChild))

    def values(self):
        """

        :return:
        """
        Values = []
        for k in self.keys():
           Values.append(self.get(k))
        return Values


    def put(self, key, val):
        """
        Builds Binary Search Tree.
        Checks to see if the tree has a root.
        If no root, creates a new TreeNode and installs it as root of tree.
        :param key: index of list in BinarySearchTree
        :param val: additional info contained in a node
        :return: None
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        """
        If there's already a root node in place
        Compare new key with current node in tree, both subtrees,
        When there's no left or right child to search
        Install new node in this position
        :param key: index of list in BinarySearchTree
        :param val: additional info contained in a node
        :param currentNode: node that is currently compared to in tree
        :return: None
        """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
        else:
            currentNode.replaceNodeData(key, val, currentNode.leftChild, currentNode.rightChild)
            self.size -= 1

    def delete(self, key):
        """
        Use _get method to find node TreeNode to be removed.
        del operator raises KeyError if key is not found.
        :param key: index of list in BinarySearchTree to be removed
        :return: None
        """
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        """
        Calls delete() method. Deletes the key.
        :param key: index of list in BinarySearchTree to be deleted
        :return: None
        """
        self.delete(key)

    def set_balanceFactor(self):
        """

        :return:
        """
        for n in self.items():
            if n.leftChild == None:
                lh = 0
            else:
                lh = n.leftChild.height(n.leftChild)
            if n.rightChild == None:
                rh = 0
            else:
                rh = n.rightChild.height(n.rightChild)
            n.balanceFactor = lh - rh

    def search_random_list(self, val):
        """

        :param val:
        :return:
        """
        if not self.root:
            return None
        else:
            self.Key_found = None
            self._searchRandom(val, self.root)
            return self.Key_found

    def _searchRandom(self, val, node):
        """

        :param val:
        :param node:
        :return: None
        """
        if node == None:
            return
        else:
            if node.payload == val:
                self.Key_found = node.key
                return
            if node.hasLeftChild:
                self._searchRandom(val, node.leftChild)
            if node.hasRightChild:
                self._searchRandom(val, node.rightChild)

    def search_ordered_list(self, val):
        """

        :param val:
        :return:
        """
        if self.root:
            self.Key_found = None
            self._searchOrdered(val, self.root)
            return self.Key_found
        else:
            return None

    def _searchOrdered(self, val, currentNode):
        """

        :param val:
        :param currentNode:
        :return:
        """
        if val < currentNode.payload:
            if currentNode.hasLeftChild():
                self._searchOrdered(val, currentNode.leftChild)
            else:
                return
        elif val > currentNode.payload:
            if currentNode.hasRightChild():
                self._searchOrdered(val, currentNode.rightChild)
            else:
                return
        else:
            self.Key_found = currentNode.key
            return
def main():
    t = BinarySearchTree()
    print('Empty tree, height {}, size {}'.format(t.height(t.root), len(t)))
    t[7] = 'seven'
    print('t[7] = "seven", height {}, size {}'.format(t.height(t.root), len(t)))
    t[2] = 'two'
    print('t[2] = "two", height {}, size {}'.format(t.height(t.root), len(t)))
    t[9] = 'nine'
    print('t[9] = "nine", height {}, size {}'.format(t.height(t.root), len(t)))
    t[10] = 'ten'
    print('t[10] = "ten", height {}, size {}'.format(t.height(t.root), len(t)))
    t[1] = 'one'
    print('t[1] = "one", height {}, size {}'.format(t.height(t.root), len(t)))
    t[3] = 'three'
    print('t[3] = "three", height {}, size {}'.format(t.height(t.root), len(t)))
    t.clear()
    t[7] = '2ndseven'
    print('t[7] = "2ndseven", cleared tree, height {}, size {}'.format(t.height(t.root), len(t)))
    print('\t')

    print('keys in t: {}'.format(t.keys()))
    print('values in t: {}'.format(t.values()))
    nodes = t.items()
    t.set_balanceFactor()
    for i in nodes:
        print('key = "{}", height {}, balanceFactor {}'.format(i.key, i.height(i), i.balanceFactor))
    print('\t')

    print('{} items in t: {}'.format(len(nodes), nodes))
    t[7] = '2ndseven'
    print('t[7] = "{}", height {}, size {}'.format(t[7], t.height(t.root), len(t)))

    t2 = BinarySearchTree()
    names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for k, v in enumerate(names):
        t2[k] = v
        print('t2[{}] = "{}", height {}, size {}'.format(k, t2[k], t2.height(t2.root), len(t2)))
    print('keys in t2: {}'.format(t2.keys()))
    print('\t')

    for v in (5, 25):
        if v in t2:
            print('yes, {} is in t2, t2[{}] = "{}"'.format(v, v, t2[v]))
        else:
            print("no, {} is not in t2".format(v))
    print('\t')

    t2.set_balanceFactor()
    for i in t2.items():
        print('key = "{}", height {}, balanceFactor {}'.format(i.key, i.height(i), i.balanceFactor))

if __name__ == '__main__':
    main()

