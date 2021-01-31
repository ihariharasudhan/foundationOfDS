class newNode:
    def __init__(self, data): 
        self.key = data
        self.left = None
        self.right = None

class binaryTree(): 
    def __init__(self):
        self.head=None 
    def insert(self,key):
        if self.head is None:
            self.head=newNode(key)
            return
        q = [] 
        q.append(self.head) 
        while (len(q)): 
            temp = q[0] 
            q.pop(0) 
            if temp.left is None:
                temp.left = newNode(key) 
                break
            else:
                q.append(temp.left) 
            if temp.right is None:
                temp.right = newNode(key) 
                break
            else:
                q.append(temp.right)
    def deletion(self, key): 
        if self.head == None : 
            return False
        if self.head.left == None and self.head.right == None: 
            if self.head.key == key :  
                return True
            else : 
                return False 
        keyValue = None
        queueUsed = [] 
        queueUsed.append(self.head) 
        while queueUsed: 
            temp = queueUsed.pop(0) 
            if temp.key == key: 
                keyValue = temp 
            if temp.left: 
                queueUsed.append(temp.left) 
            if temp.right: 
                queueUsed.append(temp.right)
        print("Temp is ",temp.key) 
        if keyValue is not None:  
            x = temp.key
            inorder(self.head)  
            queueTo = [] 
            queueTo.append(self.head) 
            while queueTo:
                trial = queueTo.pop(0)
                if trial.key==temp.key: 
                    trial = None
                    break
                if trial.right is not None: 
                    if trial.right.key==temp.key: 
                        print("Deleting ",trial.right.key)
                        trial.right = None
                        break
                    else: 
                        queueTo.append(trial.right) 
                if trial.left is not None: 
                    if trial.left.key==temp.key: 
                        print("Deleting ",trial.left.key)
                        trial.left = None
                        break
                    else: 
                        queueTo.append(trial.left) 
            keyValue.key = x
            return True
        else:
            return False 

def mirror(root):
    if root.left  is None:
        return 
    elif root.right is None:
        return
    else:
        temp = root.key
        mirror(root.left)
        mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

def depth(root):
    if root.left is None and root.right:
        return 1
    if root.right is None and root.left:
        return 1
    if root.left is None and root.right is None:
        return 0
    else:
        leftdepth = depth(root.left)
        rightdepth = depth(root.right)
        if leftdepth > rightdepth :
            return leftdepth + 1
        else :
            return rightdepth + 1

def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.left)
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

def inorder(root):
    if root is None:
        return
    inorder(root.left) 
    print(root.key,end = " ")
    inorder(root.right)

def preorder(root,lis):
    lis.append(root.key)
    if root.left:
        preorder(root.left,lis)
    if root.right:
        preorder(root.right,lis)
    return lis

def postorder(root, lis):
    if root.left:
        postorder(root.left,lis)
    if root.right:
        postorder(root.right,lis)
    lis.append(root.key)
    return lis

def height(root):
        if root is None:
            return 0
        return 1 + max(height(root.left),height(root.right))

def countLeaf(node):
    if node is None:
        return 0
    if node.left is None and node.right is None :
        return 1
    else :
        return countLeaf(node.left) + countLeaf(node.right)

def recursiveCount(node):
    if node is None: 
        return 0 
    else: 
        return (recursiveCount(node.left)+ 1 + recursiveCount(node.right))

def main():
    treeUsed=binaryTree()
    while True:
        choice=int(input("\nEnter the operation that you would like to perform:\n1.Add\n2.Delete\n3.Diameter\n4.Count nodes\n5.Traversal\n6.Mirror\n7.Depth\n8.Count leaves\n9.Exit\n"))
        if choice==1:
            name=input("\nEnter the value in the node: ")
            treeUsed.insert(name)
        elif choice==2:
            value=input("Enter the node you want to delete: ")
            success=treeUsed.deletion(value)
            if success==True:
                print("Deleted")
            else:
                print("Node doesn't exist")
        elif choice==3:
            dia=diameter(treeUsed.head)
            print("\nDiameter of the tree is ",dia)
        elif choice==4:
            nodes=recursiveCount(treeUsed.head)
            print("The number of nodes is ",nodes)
        elif choice==5:
            print("Inorder traversal of tree is ")
            inorder(treeUsed.head)
            print("Post order traversal of tree is ")
            post=[]
            postorder(treeUsed.head,post)
            print(post)
            print("Pre order traversal of tree is ")
            pre=[]
            preorder(treeUsed.head,pre)
            print(pre)
        elif choice==6:
            mirror(treeUsed.head)
            print("The mirror of the tree is ")
            inorder(treeUsed.head)
        elif choice==7:
            depthCalc=depth(treeUsed.head)
            print("Depth of the tree is ",depthCalc)
        elif choice==8:
            leafCount=countLeaf(treeUsed.head)
            print("Number of leaves ",leafCount)
        elif choice==9:
            break
        else:
            print("Invalid input")


if __name__=="__main__":
    main()
