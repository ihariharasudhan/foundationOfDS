class node:
    def __init__(self,name):
        self.name=name
        self.nextNode=None
        self.previousNode=None

class linked:
    def __init__(self):
        self.head=None
    def printer(self):
        search=self.head
        while(True):
            if search==None:
                break
            print(search.name)
            prev=search
            search=search.nextNode
        print('Printing in reverse ')
        while True:
            if prev==None:
                break
            print(prev.name)
            prev=prev.previousNode

    def add(self,choice,value):
        nodeVal=node(value)
        temp=self.head
        if choice==1:
            if temp!=None:
                nodeVal.nextNode=temp
                temp.previousNode=nodeVal
                nodeVal.previousNode=None
                self.head=nodeVal
            else:
                nodeVal.nextNode=None
                nodeVal.previousNode=None
                self.head=nodeVal
        elif choice==2:
            if(self.head==None):
                print('Cannot insert it in end when head is None')
                return
            runner=self.head
            while(runner.nextNode):
                runner=runner.nextNode
            runner.nextNode=nodeVal
            nodeVal.previousNode=runner
        elif choice==3:
            runner=self.head
            location=int(input('\nEnter the location where you want to input: '))
            for i in range(location-2):
                runner=runner.nextNode
            nodeVal.previousNode=runner
            nodeVal.nextNode=runner.nextNode
            runner.nextNode=nodeVal
            (nodeVal.nextNode).previousNode=nodeVal
    def delete(self,value):
        search=self.head
        if search!=None:
            if search.name==value:
                (search.nextNode).previousNode=None
                self.head=search.nextNode
                return
        while search!=None:
            if search.name==value:
                break
            before=search
            search=search.nextNode
        if search==None:
            return
        if search.nextNode!=None:
            (search.nextNode).previousNode=before
            before.nextNode=search.nextNode
        else:
            before.nextNode=None


        
def main():
    listOrg=linked()
    while True:
        option=int(input('\nEnter the operation in you would like to perform \n1.Add\n2.Delete\n3.Printer\n4.Exit\n'))
        if option==1:
            value=int(input('\nEnter the value you want to enter: '))
            choice=int(input('\nEnter the location where you want to insert \n1.Front\n2.Rear\n3.Middle'))
            listOrg.add(choice,value)
        elif option==2:
            value=int(input('\nEnter the number you want to delete: '))
            listOrg.delete(value)
        elif option==3:
            print('\nThe data in the list ')
            listOrg.printer()
        elif option==4:
            break

if __name__=='__main__':
    main()
