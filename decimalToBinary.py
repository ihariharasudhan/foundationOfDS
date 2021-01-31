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

def decimalToBinary():
    maxSize=int(input('\nEnter the maximum size of the stack: '))
    stackUsed=stackClass(maxSize)
    decimal=int(input('\nEnter the decimal number: '))
    while decimal>0:
        if decimal==1:
            stackUsed.push(1)
            break
        data=decimal%2
        stackUsed.push(data)
        decimal=decimal//2
    print('\n The binary form of the number is ',end='')
    for i in range(stackUsed.checkSize()):
        data=stackUsed.popOut()
        print(data,end='')
    print('\n')

def main():
    decimalToBinary()

if __name__=="__main__":
    main()