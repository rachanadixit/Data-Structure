class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            self.size += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        temp = self.front
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.size -= 1
        else:
            self.front = self.front.next
            return temp.data
        
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end="|")
            temp = temp.next
        print()

Queue = Queue()
Queue.enqueue(30)
Queue.enqueue(20)
Queue.enqueue(10)
Queue.enqueue(50)
print("Queue after enqueue:")
Queue.display()
Queue.dequeue()
Queue.dequeue()
    # print("Dequeued element:", Queue.dequeue())
print("Queue after dequeue:")
Queue.display()
       