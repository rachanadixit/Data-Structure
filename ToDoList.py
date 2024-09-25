class Node:
    def __init__(self,task,priority):
        self.task=task
        self.priority=priority
        self.next=None
class Stack:
    def __init__(self):
        self.head=Node("Complete project proposal","High")
        
    def push(self,task,priority):
       new_node=Node(task,priority)
       new_node.next=self.head
       self.head=new_node
       print( f"Task '{task}' with priority '{priority}' added successfully.")
       
       
    def pop(self):
        if not self.head:
            return print("stack is empty")
        else:
            poped_node=self.head.task
            self.head=self.head.next
            print()
            print( f"Task '{poped_node}'  removed successfully.")


        
        
    def peek(self):
        if not self.head:
            return None
        else:
            print()
            
            print(self.head.task," is at peek")   
        

    
if __name__=="__main__":
    stack=Stack()
    stack.push("Complete project proposal","High")
    stack.push("Schedule Team Meeting","Medium")
    stack.push("Review draft presentation","Low")
    stack.push("Prepare weekly report","High")
    stack.push("Respond to client emails","Medium")
    stack.peek()
    stack.pop()

            
