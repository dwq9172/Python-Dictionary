__author__ = 'Dennis Qiu'

class TreeNode():
    """
    Description:  Implement a tree node with the following interface
                  functions:
                  __init__(k, v, lc, rc, p)
                  hasLeftChild()
                  hasRightChild()
                  isLeftChild()
                  isRightChild()
                  isRoot()
                  isLeaf()
                  hasAnyChildren()
                  hasBothChildren()
                  replaceNodeData(k, v, lc, rc)
    """
    def __init__(self,key,val,left=None,right=None,
                                           parent=None):
        """
        Initializes TreeNode.
        :param key: indices of list in TreeNode
        :param val: additional info contained in a node
        :param left: node to the left below its parent node (incoming edges)-->node on left subtree
        :param right: node to the right below its parent node (incoming edges)--> node on right subtree
        :param parent: "Parent" of all nodes it connects with outgoing edges
        :return: reference for self
        """
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        """
        The subtree containing the left child node
        :return: node for left child
        """
        return self.leftChild

    def hasRightChild(self):
        """
        The subtree containing the right child node
        :return: node for right child
        """
        return self.rightChild

    def isLeftChild(self):
        """
        If node is the lc node
        :return: parent node and lc node attached to parent node
        """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """
        If node is the rc node
        :return: parent node and rc node attached to parent node
        """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """
        (The root of the tree) node in tree with no incoming edges
        :return: does not return parent node
        """
        return not self.parent

    def isLeaf(self):
        """
        Node that has no children
        :return: does not return node for rc or node for lc
        """
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """
        If a node has a lc node or rc node
        :return: either node for rc or node for lc
        """
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """
        If a node has both lc and rc nodes
        :return: both nodes for lc and rc
        """
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        """
        Replaces original node data with new node data
        :param key: indices of list
        :param value: additional info contained in a node
        :param lc: node to the left below its parent node (incoming edges)-->node on left subtree
        :param rc: node to the right below its parent node (incoming edges)--> node on right subtree
        :return: None
        """
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def height(self, node):
        """
        Height of any given node in tree
        :param node: node in tree
        :return: height of any given node
        """
        return 1 + max(self.height(node.leftChild) if node.leftChild is not None else 0,
                       self.height(node.rightChild) if node.rightChild is not None else 0)