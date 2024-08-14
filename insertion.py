class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head,data):
   node = Node(data)
   node.next = head
   return node


def print_list(head):
    current = head
    while current is not None:
        print(f" {current.data}", end="")
        current = current.next
    print()


if __name__ == "__main__":

    head = Node(20)
    head.next = Node(30)
    head.next.next = Node(40)
    head.next.next.next = Node(50)
    print("Original Linked List:", end="")
    print_list(head)
    print("After inserting Nodes at the end:", end="")
    data = 10
    head = insert_at_end(head, data)
    print_list(head)
