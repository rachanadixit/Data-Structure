class hospital:
    def __init__(self, name,age,patient_id,disease):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.disease = disease
        self.next = None

class PatientQueue:
    def __init__(self):
        self.head = None 
        

    def add_patient(self, name, age,patient_id,disease):
        new_patient = hospital(name,age,patient_id,disease)
        if self.head is None:
            self.head = new_patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_patient

    def search_patient(self,patient_id):
        current = self.head
        while current:
            if current.patient_id == patient_id:
               print("patient name: ", current.name)
            else:
                print("No patient found with the given ID.")
            current = current.next
           

    def remove_patient(self, name,patient_id):
        current = self.head
        previous = None
        
        while current and current.patient_id!= patient_id:
            previous = current
            current = current.next
        if current is None:
            print(f"No patient found with the name: {name}")
            return    
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        print(f"patient with ID{patient_id} has been removed.")    

    
    def schedule_to_front(self, patient_id):
        if self.head is None or self.head.patient_id == patient_id:
            print(f"patient with ID{patient_id} is already in front")
            return
        current = self.head
        previous = None
        
        while current and current.patient_id!=patient_id:
            previous = current
            current = current.next   
                              
        if current is None:
            print(f"No patient found with the ID: {patient_id}")
            return
        if previous:
            previous.next = current.next
        current.next = self.head
        self.head = current
        print(f"Patient with ID{patient_id} has been scheduled to the front.")
    
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
            print("\n1. Add Patient\n2.Search Patient\n3. Remove Patient\n4. Display Queue\n5.schedule_to_front\n6. Exit")
            choice = input("Enter your choice (1-6): ")

            match choice:
                case "1":
                    name = input("Enter patient name: ")
                    age = int(input("Enter patient age: "))
                    patient_id = int(input("Enter patient ID: "))
                    disease = input("Enter patient disease: ")
                    self.add_patient(name,age,patient_id,disease)
                case "2":
                    patient_id = int(input("Enter patient ID to search: "))
                    self.search_patient(patient_id)    
                case "3":
                    name = input("Enter patient name to remove: ")
                    patient_id = int(input("Enter patient ID to remove: "))
                    self.remove_patient(name,patient_id)
                case "4":

                    self.display_queue()
                case "5": 
                    patient_id = int(input("Enter patient ID to schedule to front: "))
                    self.schedule_to_front(patient_id) 
                case "6":
                    print("Exiting...")
                    return
                case _:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    queue = PatientQueue()
    queue.manage_queue()       




        