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
        
        name = input("Enter the name of the patient to remove: ")
        
        current = self.head
        previous = None
        
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:  
                    self.head = current.next

                if current == self.tail:  
                    self.tail = previous
                
                print(f"Removed patient: {current.name}")
                return
            
            previous = current
            current = current.next

        print(f"No patient found with the name: {name}")

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




        
        




        
