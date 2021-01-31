class graphClass:
    def __init__(self):
        self.vertices_count=0
        self.vertices=[]
        self.connections=[]
    def addVertex(self,value):
        if value in self.vertices:
            return False
        else:
            self.vertices.append(value)
            self.vertices_count+=1
            if self.vertices_count>=1:
                for i in self.connections:
                    i.append(0)
                insertList=[]
                for i in range(self.vertices_count):
                    insertList.append(0)
                self.connections.append(insertList)
        return True
    def addEdge(self,fromVertex,toVertex,weight):
        if fromVertex in self.vertices:
            if toVertex in self.vertices:
                frm=self.vertices.index(fromVertex)
                to=self.vertices.index(toVertex)
                self.connections[frm][to]=weight
                return True
            else:
                return False
        else:
            return False
    def printMatrix(self):
        for i in range(self.vertices_count):
            print(i,"is",self.vertices[i])
        for i in self.connections:
            print("\n",i)
    def DFS(self,startNode,blacked):
        print(startNode,end=" ")
        index=self.vertices.index(startNode)
        blacked[index]=True
        for i in range(self.vertices_count):
            if self.connections[index][i]!=0 and blacked[i]==False:
                self.DFS(self.vertices[i],blacked)
    def BFS(self,startNode):
         blacked=[False]*self.vertices_count
         popQueue=[startNode]
         blacked[self.vertices.index(startNode)]=True
         while popQueue:
             visited=popQueue[0]
             index=self.vertices.index(visited)
             print(visited,end=" ")
             popQueue.pop(0)
             for i in range(self.vertices_count):
                 if self.connections[index][i]!=0 and blacked[i]==False:
                     popQueue.append(self.vertices[i])
                     blacked[i]=True
    def Center(self,startNode,blacked,weight,noOfvertex):
        index=self.vertices.index(startNode)
        blacked[index]=True
        for i in range(self.vertices_count):
            if self.connections[index][i]!=0 and blacked[i]==False:
                weight = weight + self.connections[index][i]
                noOfvertex.append(self.vertices[i])
                self.Center(self.vertices[i],blacked,weight,noOfvertex)
        lengthofVertex = len(noOfvertex)
        middle = (lengthofVertex - 1) // 2
        print("The center of the vertex is ", noOfvertex[middle])



def wordLadder():
    ladder=graphClass()
    for i in range(5):
        nodeName=input("Enter the 5 letter word: ")
        if len(nodeName)!=5:
            i=i-1
            print("It is not a 5 letter word")
            continue
        result=ladder.addVertex(nodeName)
    for i in range(4):
            compare1=ladder.vertices[i]
            compare2=ladder.vertices[i+1]
            change=0
            for k in range(5):
                if compare1[k]!=compare2[k]:
                    change+=1
            if change==1:
                result=ladder.addEdge(compare1,compare2,1)
    ladder.printMatrix()

def main():
    graphUsed=graphClass()
    blacked=[]
    while(True):
        choice=int(input("\nEnter the operation that you would like to perform:\n1.Add vertex\n2.Add edge\n3.Print\n4.DFS\n5.BFS\n6.Centre\n7.Exit\n"))
        if choice==1:
            vName=input("\nEnter the vertex name:")
            result=graphUsed.addVertex(vName)
            if result==True:
                print("\nAdded")
            else:
                print("\nEnter a unique name")
        elif choice==2:
            fromVertex=input("\nEnter the source vertex: ")
            toVertex=input("\nEnter the destination vertex: ")
            weight=int(input("\nEnter the weight: "))
            result=graphUsed.addEdge(fromVertex,toVertex,weight)
            if result==True:
                print("\nAdded")
            else:
                print("\nVertex doesn't exist")
        elif choice==3:
            graphUsed.printMatrix()
        elif choice==4:
            startNode=input("\nEnter the start vertex: ")
            if startNode in graphUsed.vertices:
                blacked=[False]*graphUsed.vertices_count
                graphUsed.DFS(startNode,blacked)
            else:
                print("\nVertex doesn't exist")
        elif choice==5:
            startNode=input("\nEnter the start vertex: ")
            graphUsed.BFS(startNode)
        elif choice==6:
            startNode=input("\nEnter start vertex: ")
            if startNode in graphUsed.vertices:
                blacked=[False]*graphUsed.vertices_count
                graphUsed.Center(startNode,blacked,0,[startNode])
        elif choice==7:
            break
    wordLadder()
        
if __name__=="__main__":
    main()

