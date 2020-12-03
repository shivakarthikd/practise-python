def create_tree(r):
    return [r,[],[]]

def insertLeft(root,branch):
    t=root.pop(1)
    if len(t)>0:
        root.insert(1,[branch,t,[]])
    else:
        root.insert(1,[branch,[],[]])
    return root
def insertRight(root,branch):
    t=root.pop(2)
    if len(t)>0:
        root.insert(2,[branch,[],t])
    else:
        root.insert(2,[branch,[],[]])
    return root

def getRootValue(root):
    return root[0]

def setRootValue(root,newroot):
    root[0]=newroot
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]



root=create_tree(5)

print(insertLeft(root,4))
print(insertRight(root,5))

setRootValue(root,10)
print(getLeftChild(root))


