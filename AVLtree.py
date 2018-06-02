__author__ = 'Dennis Qiu'
from treeNode import TreeNode
from binarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    """

    """
    def __init__(self):
        """

        """
        super().__init__()

    def _put(self, key, val, currentNode):
        """

        :param key:
        :param val:
        :param currentNode:
        :return:
        """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        """

        :param node:
        :return:
        """
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        """

        :param rotRoot:
        :return:
        """
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        """

        :param node:
        :return:
        """
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

def main():
    t = AVLTree()
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
    print('\t')

    print('keys in t: {}'.format(t.keys()))
    print('values in t: {}'.format(t.values()))
    nodes = t.items()
    print('{} items in t: {}'.format(len(nodes), nodes))
    print('\t')

    t[7] = '2ndseven'
    print('t[7] = "{}", height {}, size {}'.format(t[7], t.height(t.root), len(t)))

    t2 = AVLTree()
    names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for k, v in enumerate(names):
        t2[k] = v
        print('t2[{}] = "{}", height {}, size {}'.format(k, t2[k], t2.height(t2.root), len(t2)))

    print('\t')
    print('keys in t2: {}'.format(t2.keys()))

    for v in (5, 25):
        if v in t2:
            print('yes, {} is in t2, t2[{}] = "{}"'.format(v, v, t2[v]))
        else:
            print("no, {} is not in t2".format(v))

if __name__ == '__main__':
    main()
