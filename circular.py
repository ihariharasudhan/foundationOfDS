class node:
    def __init__(self,name):
        self.name=name
        self.nextNode=None

class linked:
    def __init__(self):
        self.head=None
        self.length=0
    def printer(self):
        search=self.head
        for i in range(self.length):
            print(search.name)
            search=search.nextNode
    def add(self,choice,value):
        nodeVal=node(value)
        temp=self.head
        if choice==1:
            if temp!=None:
                nodeVal.nextNode=temp
                self.head=nodeVal
            else:
                nodeVal.nextNode=nodeVal
                self.head=nodeVal
        elif choice==2:
            if(self.head==None):
                print('Cannot insert it in end when head is None')
                return
            runner=self.head
            for i in range(self.length-1):
                runner=runner.nextNode
            print('Adding to the end of ',runner.name)
            runner.nextNode=nodeVal
            nodeVal.nextNode=self.head
        elif choice==3:
            runner=self.head
            location=int(input('\nEnter the location where you want to input: '))
            for i in range(location-2):
                runner=runner.nextNode
            nodeVal.nextNode=runner.nextNode
            runner.nextNode=nodeVal
        self.length=self.length+1
    
    def delete(self,value):
        search=self.head
        node=self.head
        runner=0
        if search!=None:
            if search.name==value:
                self.head=search.nextNode
                for i in range(self.length):
                    node=node.nextNode
                node.nextNode=search.nextNode
                self.length=self.length-1
                return
        for runner in range(self.length-1):
            if search.name==value:
                break
            before=search
            search=search.nextNode
        if runner==self.length:
            return
        before.nextNode=search.nextNode
        self.length=self.length-1

        
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