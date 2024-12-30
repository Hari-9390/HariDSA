class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1

    def enqueue(self,data):
        if(self.rear+1)%self.size==self.front:
            print("queue is full")
            return
        elif self.front==-1:
            self.front=0
            self.rear=0

        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
            print(f"enqueued {data}")

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        data=self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return data
    
    def display(self):
        if self.is_empty():
            print("queue is empty")
            return
        if self.rear>=self.front:
            i=self.front
            while i<=self.rear:
                print(self.queue[i],end=" ")
                i+=1
        else:
            i=self.front
            while i<self.size:
                print(self.queue[i],end=" ")
                i+=1
            i=0
            while i<=self.rear:
                print(self.queue[i],end=" ")
                i+=1
        print()
cq=CircularQueue(3)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(6)
cq.enqueue(7)
cq.enqueue(8)
cq.enqueue(9)
cq.display()
