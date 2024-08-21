class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

N1=Node(10)
N2=Node(20)
N3=Node(30)

N1.next=N2
N2.next=N3

head=N1
current=head
new_node=Node(40)

head=new_node
current=head







while(current != None):
    print(current.data)
    current=current.next





        