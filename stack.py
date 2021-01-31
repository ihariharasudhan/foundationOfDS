class stackClass:
    def __init__(self, maximum=None):
        self.stack=[]
        self.size=0
        self.maxSize=maximum 
    def push(self,value):
        if self.maxSize==None: 
            self.stack.append(value)
            self.size+=1
        elif self.maxSize>self.size:
            self.stack.append(value)
            self.size+=1
        else:
            print("\nStack Full!")
    def popOut(self):
        if self.size==0:
            print('\nStack empty')
            return
        value=self.stack.pop()
        self.size-=1
        return value
    def checkSize(self):
        return self.size

def reverse(dupStack):
    revStack=stackClass(dupStack.maxSize)
    while(True):
        if dupStack.checkSize()==0:
            break
        else:
            value=dupStack.popOut()
            revStack.push(value)
    print("\nThe size of the reverse stack is ",revStack.checkSize())
    while(True):
                if revStack.checkSize()==0:
                    break
                else:
                    value=revStack.popOut()
                    print("The value popped out is ",value)


def bracket():
    braces=stackClass()
    inputVal=input('\nEnter the input: ')
    for value in inputVal:
        if value=='(':
            braces.push(value)
        elif value==')':
            if braces.checkSize()==0:
                print('\nThe brackets are not balanced')
                return
            dummy=braces.popOut()
    if braces.checkSize()==0:
        print('\nThe brackets are balanced')
    else:
        print('\nIt is not balanced')

def normalStack():
    size=int(input("\nEnter the maximum size of the stack: "))
    realStack=stackClass(size)
    while(True):
        choice=int(input('\nEnter the operation that you would like to perform\n1.Push\n2.Pop\n3.Check size\n4.Clear\n5.Reverse\n6.Exit\n'))
        if choice==1:
            value=input("\nEnter the data: ")
            realStack.push(value)
        elif choice==2:
            result=realStack.popOut()
            print("\nThe value popped out is ",result)
        elif choice==3:
            print("\nThe size of the stack is ",realStack.checkSize())
        elif choice==4:
            while(True):
                if realStack.checkSize()==0:
                    break
                else:
                    result=realStack.popOut()
                    print("\nThe value popped out is ",result)
        elif choice==5:
            reverse(realStack)
        elif choice==6:
            break
        else:
            print("\nInvalid entry!")
            
def main():
    bracket()
    normalStack()

if __name__=="__main__":
    main()
