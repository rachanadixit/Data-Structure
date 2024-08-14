class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_in_front(head,data):
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

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    print("Original Linked List:", end="")
    print_list(head)
    print("After inserting Node at the front:", end=" ")
    data = 50
    head = insertion_in_front(head, data)
    print_list(head)
    data = 60
    head = insertion_in_front(head, data)
    print_list(head)