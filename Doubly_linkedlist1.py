class Node :
    def __init__(self ,name ,quantity ,price ) :
        self.name =name 
        self.quantity = quantity
        self.price  =price
        self.prev = None
        self.next = None

class DoubluCircularLL :
    def __init__(self) :
        self.head = None 

    def add_item(self,name,quantity,price ):
        new_node = Node(name,quantity,price)
        if self.head is None :
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else  :
            tail = self.head.prev 
            new_node.next = self.head 
            new_node.prev = tail
            tail.next = new_node

    def remove_item(self,name):
        if not self.head:
            print("No item in the queue.")
            return  
        current = self.head
        while True:
            if current.name == name:
                if current.name == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                print(f"Item'{name}' removed successfully.")
                return
            current = current.next
            if current == self.head:
                break
        print(f"Item'{name}' not found.")     

    def update_item(self,name,quantity = None ,price = None ):
        current = self.head 
        while True :
            if current.name == name :
                if quantity is not None :
                    current.quantity = quantity 
                if price is not None :
                    current.price = price 
                
                print(f"Item {name} updated Succesfully.")
                return
            current = current.next 
            if current == self.head :
                break 
        print(f"Item Not Found ")

    def search_item(self,name):
        current = self.head 
        while True :
            if current.name == name:
                return current 
            current = current.next 
            if current == self.head :
                break 
        return None 
            
    def display_order(self):
        if self.head is None:
            print("the list is empty.")
            return
        current = self.head
        while True:
            print(f"Name:{current.name},Quantity:{current.quantity},Price:${current.price}")
            current = current.next
            if current == self.head:
                break
def main():
    order = DoubluCircularLL()

    while True:
        command = input("Enter command (add , remove, update , search, view , exit): ").strip().lower()

        if command == "add":
            name = input("Enter Item Name : ")
            quantity = int(input("Enter Quantity : "))
            price = int(input("Enter Price : "))
            order.add_item(name ,quantity,price)
            print("Item Added Succesfully ")
            
        elif command == "remove":
            name = input("Enter item name to remove: ")
            order.remove_item(name)
            print("Item Removed Succesfully ")
    
        elif command == "search":
            name = input("Enter item name to search : ")
            order.search(name)

        elif command == "update" :
            name = input("Enter Item Name to update : ")
            quantity = int(input("Enter New quantity : "))
            price = int(input("Enter New Price : "))

     

        elif command == "exit":
            print("Exiting the Retail management system.")
            break

        else:
            print("Invalid command. Please enter add , remove, update , search, view , exit.")

if __name__ == "__main__":
    main()