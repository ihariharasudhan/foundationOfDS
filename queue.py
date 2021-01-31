class queueClass:
    def __init__(self,size):
        self.queue=[]
        self.maxSize=size
        self.size=0
    
    def similar(self):
        for i in range(len(self.queue)):
            for j in range(i+1,len(self.queue)):
                if self.queue[i].searcher()==self.queue[j].searcher():
                    print('There are duplicates')
                    return
        print('No duplicates')
    
    def search(self):
        key=input('Enter the value you want to search: ')
        for i in range(len(self.queue)):
            if self.queue[i].searcher()==key:
                print('Found')
                return
        print('Not found')
    
    def enqueue(self):
        if self.size<self.maxSize:
            self.size+=1
            value=input('Enter the name of the person in the queue: ')
            obj=element(value)
            self.queue.append(obj)
        else:
            print('\nQueue is full')
    
    def dequeue(self): 
        if self.size==0:
            print('\nQueue is empty')
        else:
            self.size-=1
            value=self.queue.pop(0)
            print('The person being served is ')
            print(self.size)
            value.printer()
    
    def length(self):
        print('No. of individuals in the queue is ',len(self.queue))
    
    def between(self):
        value=input('Enter the name of the person in the queue: ')
        obj=element(value)
        location=int(input('Enter the location in which you want to enter it: '))
        self.queue.insert(location,obj)
        self.size+=1
    
    def autoAdd(self,value):
        if self.size<self.maxSize:
            self.size+=1
            obj=element(value)
            self.queue.append(obj)
        else:
            print('\nQueue is full')

    def reverse(self):
        reverse=queueClass(self.maxSize)
        for i in range(len(self.queue)):
            obj=self.queue.pop()
            self.size-=1 #the missing problem
            value=obj.searcher()
            reverse.autoAdd(value)
        print('\nThe reversed queues is ')
        while(reverse.size!=0):
            reverse.dequeue()

class element:
    def __init__(self, name=None):
        self.name=name
    
    def printer(self):
        print('Name: ',self.name)
    
    def searcher(self):
        return self.name

def main():
    size=int(input('Enter the size of the queue: '))
    queue=queueClass(size)
    while(True):
        choice=int(input('Enter the operation that you would like to perform:\n1.Enqueue\n2.Dequeue\n3.Check size\n4.Flush\n5.Add anywhere\n6.Searh\n7.Similiar\n8.Reverse\n9.Exit\n'))
        if choice==1:
            queue.enqueue()
        elif choice==2:
            queue.dequeue()
        elif choice==3:
            queue.length()
        elif choice==4:
            for i in range (len(queue.queue)):
                queue.dequeue()
        elif choice==5:
            queue.between()
        elif choice==6:
            queue.search()
        elif choice==7:
            queue.similar()
        elif choice==8:
            queue.reverse()
        elif choice==9:
            break
        else:
            print('Invalid input')


if __name__=="__main__":
    main()
