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
            return None
        value=self.stack.pop()
        self.size-=1
        return value
    def checkSize(self):
        return self.size

def infixConvertor(expression):
    expressionStack=stackClass()
    content=""
    for element in expression:
        if element=='+' or element=='/' or element=='-' or element=='*':
            content=content+' '+element
            while True:
                data=expressionStack.popOut()
                if data=='(' or data is None:
                    break
                else:
                    content=content+' '+data
        elif element!=')':
            expressionStack.push(element)
        elif element==')':
            while True:
                data=expressionStack.popOut()
                if data=='(' or data is None:
                    break
                else:
                    content=content+' '+data
            expressionStack.push(content)
            content=""
    data=expressionStack.popOut()
    print('The pre fix expression is ',data)
    

def calculator (op,op1 , op2):
    op1 = int(op1)
    op2 = int(op2)
    if op == "+":
        result = op1 + op2
    elif op == "*":
        result = op1 * op2
    elif op  == "-":
        result = op1-op2
    elif op == "/":
        result = op1/op2
    return result

def postfixConvertor(expression):
    expressionStack=stackClass()
    content=""
    numbers={"0","1","2","3","4","5","6","7","8","9"}
    symbols={"+","-","/","*"}
    for element in expression:
        if element in numbers:
            content=content+' '+element
            while True:
                data=expressionStack.popOut()
                if data=='(' or data is None:
                    expressionStack.push(data)
                    break
                else:
                    content=content+' '+data
        elif element!=')':
            expressionStack.push(element)
        elif element==')':
            while True:
                data=expressionStack.popOut()
                if data=='(' or data is None:
                    break
                elif data in symbols:
                    another=expressionStack.popOut()
                    content=another+' '+content+' '+data
                    break
                else:
                    content=content+' '+data
            expressionStack.push(content)
            content=""
    data=expressionStack.popOut()
    print('The post fix expression is ',data)
    calculateStack=stackClass()
    for element in data:
        if element in numbers:
            calculateStack.push(element)
        elif element in symbols:
            op=element
            op2=calculateStack.popOut()
            op1=calculateStack.popOut()
            result=calculator(op,op1,op2)
            calculateStack.push(result)
    print("\nThe result is ",calculateStack.popOut())

def expressionEval(expression):
    evaluationStack=stackClass()
    for element in expression:
        if element!=')':
            evaluationStack.push(element)
        elif element==')':
            op2=evaluationStack.popOut()
            op=evaluationStack.popOut()
            op1=evaluationStack.popOut()
            result=calculator(op,op1,op2)
            dummy=evaluationStack.popOut()
            evaluationStack.push(result)
    print('The result is ',evaluationStack.popOut())



def expressionGet():
    expression=input('\nEnter the expression: ')
    expressionEval(expression)
    infixConvertor(expression)
    postfixConvertor(expression)
    

def main():
    expressionGet()

if __name__=="__main__":
    main()