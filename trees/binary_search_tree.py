
class Tree(object):
    def __init__(self,root):
        self.root=root
        self.leftChild=None
        self.rightChild=None


    def pre_traverse(self,tree):
        if tree:
            print(tree.root)
            self.pre_traverse(tree.leftChild)
            self.pre_traverse(tree.rightChild)



class BinarySearchTree(Tree):
    def __init__(self,rootNode):
        self.node=Tree(rootNode)


    def insertleft(self,val):
        t=self.node.leftChild
        if t is None:
                t=Tree(val)
        else:
            while t:
                t=self.leftChild
                if t is None:
                    t=Tree(val)

    def insertright(self,val):
        t=self.node
        while t:
            t=t.rightChild
        t=Tree(val)

    # def createbst(self,indata):


    def traverseTree(self):
        t = self.node
        while t:
            print(t.root)
            t = t.leftChild




bs=BinarySearchTree(10)
bs.insertleft(23)
bs.insertright(54)

# bs.createbst([5,9,10,12,34,56,2,98])

print(bs)
bs.pre_traverse(bs.node)