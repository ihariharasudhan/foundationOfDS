class node:
    def __init__(self,power,prefix):
        self.power=power
        self.prefix=prefix
        self.nextNode=None

class linked:
    def __init__(self):
        self.head=None
    def printer(self):
        search=self.head
        while(True):
            if search==None:
                break
            data=str(search.prefix)+"x^"+str(search.power)
            print(data,end='+')
            search=search.nextNode
        print('0')
    def add(self,power,prefix):
        nodeVal=node(power,prefix)
        nodeVal.nextNode=self.head
        self.head=nodeVal

def main():
    polynomial=linked()
    while True:
        choice=int(input('Enter the operation you would like to perform:\n1.Add\n2.Print and exit'))
        if choice==1:
            prefix=int(input('Enter the prefix: '))
            power=int(input('Enter the power: '))
            polynomial.add(prefix,power)
        elif choice==2:
            polynomial.printer()
            break


if __name__=="__main__":
    main()

        