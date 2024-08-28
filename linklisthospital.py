
class hospital:
    
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease
        self.next = None

class PatientQueue:
   
    def __init__(self):
        self.head = None 
        self.tail = None

    def add_patient(self, name, disease):
        new_patient = hospital(name, disease)
        if not self.tail:
            self.head = self.tail = new_patient
            return
        self.tail.next = new_patient
        self.tail = new_patient

    def remove_patient(self):
        if not self.head:
            print("No patients in the queue.")
            return
        removed = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        print(f"Removed patient: {removed.name}")

    def display_queue(self):
        current = self.head
        if not current:
            print("No patients in the queue.")
            return
        print("Current queue:")
        while current:
            print(f"Patient: {current.name}, disease: {current.disease}")
            current = current.next

    def manage_queue(self):
        while True:
            print("\n1. Add Patient\n2. Remove Patient\n3. Display Queue\n4. Exit")
            choice = input("Enter your choice (1-4): ")

            match choice:
                case "1":
                    name = input("Enter patient name: ")
                    disease = input("Enter patient disease: ")
                    self.add_patient(name, disease)
                case "2":
                    self.remove_patient()
                case "3":
                    self.display_queue()
                case "4":
                    print("Exiting...")
                    return
                case _:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    queue = PatientQueue()
    queue.manage_queue()
        




        