class Tree(object):

    def __init__(self,root):
        self.root=root
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,leftnode):
        if self.leftChild is None:
            self.leftChild=Tree(leftnode)
        else:
            t=Tree(leftnode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def inserRight(self,rightnode):
        if self.rightChild is None:
            self.rightChild = Tree(rightnode)
        else:
            t = Tree(rightnode)
            t.rightChild = self.rightChild
            self.rightChild=t

    def getRootNode(self):
        return self.root

    def setRootNode(self,val):
        self.root=val
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild



def preorder_traverse(tree):


    if tree :
        print(tree.getRootNode())
        preorder_traverse(tree.leftChild)
        preorder_traverse(tree.rightChild)

def Inorder_traverse(tree):

    if tree:
        Inorder_traverse(tree.leftChild)
        print(tree.getRootNode())
        Inorder_traverse(tree.rightChild)

def postorder_traverse(tree):
    # print(root.getRootNode())
    if tree:
        postorder_traverse(tree.leftChild)
        postorder_traverse(tree.rightChild)
        print(tree.getRootNode())










root=Tree(1)
root.insertLeft(2)
root.inserRight(3)
root.getLeftChild().inserRight(5)
root.getLeftChild().insertLeft(4)

preorder_traverse(root)