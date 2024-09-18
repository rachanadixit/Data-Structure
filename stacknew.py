class Task:
    def __init__(self, priority, description):
        if priority not in ['high', 'medium', 'low']:
            raise ValueError("Priority must be 'high', 'medium', or 'low'.")
        self.priority = priority
        self.description = description
        
    def __repr__(self):
        return f"Priority: {self.priority}, Description: {self.description}"

class PriorityStack:
    def __init__(self):
        self.stack = []
        self.priority = {'high': [], 'medium': [], 'low': []}
        
    def push(self, task):
        self.stack.append(task)
        self.priority[task.priority].append(task)

    def pop(self):
        if not self.stack:
            raise ValueError("No stack available")
        task = self.stack.pop()
        self.priority[task.priority].remove(task)
        return task

    def display(self):
        for priority, tasks in self.priority.items():
            print(f"Priority: {priority}")
            for task in tasks:
                print(f"  {task}")
            print()

    def get_all_tasks(self):
        return self.stack

def main():
    todo = PriorityStack()        
    todo.push(Task('high', 'Implement a stack data structure'))
    todo.push(Task('medium', 'Write unit tests for the stack'))
    todo.push(Task('low', 'Implement a queue data structure'))
    todo.push(Task('medium', 'Write unit tests for the queue'))
    
    print("Tasks by priority stack:")
    todo.display()
    
    remove_task = todo.pop()
    print(f"Popped task: {remove_task}")
    
    print("Updated tasks by priority stack:")
    todo.display()

if __name__ == '__main__':
    main()
