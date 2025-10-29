print("hello world")

print("hello hello")

#function to add two numbers
def add(num1, num2):
    return num1 + num2


print("This is a new line added to the code.")
print("Another new line added for testing.")

#add function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Todo Task List Class
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_description):
        """Add a new task to the todo list"""
        task = {
            'id': len(self.tasks) + 1,
            'description': task_description,
            'completed': False
        }
        self.tasks.append(task)
        return task
    
    def remove_task(self, task_id):
        """Remove a task by ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return True
        return False
    
    def mark_completed(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return True
        return False
    
    def list_tasks(self):
        """List all tasks"""
        return self.tasks
    
    def get_pending_tasks(self):
        """Get all pending (not completed) tasks"""
        return [task for task in self.tasks if not task['completed']]
    
    def get_completed_tasks(self):
        """Get all completed tasks"""
        return [task for task in self.tasks if task['completed']]

def demo_todo_list():
    """Demonstrate the todo list functionality"""
    print("\n=== Todo List Demo ===")
    
    # Create a new todo list
    todo = TodoList()
    
    # Add some tasks
    print("\nAdding tasks...")
    todo.add_task("Buy groceries")
    todo.add_task("Complete project documentation")
    todo.add_task("Call the dentist")
    todo.add_task("Review pull requests")
    
    # List all tasks
    print("\nAll tasks:")
    for task in todo.list_tasks():
        status = "✓" if task['completed'] else "○"
        print(f"  [{status}] {task['id']}. {task['description']}")
    
    # Mark some tasks as completed
    print("\nMarking tasks 1 and 3 as completed...")
    todo.mark_completed(1)
    todo.mark_completed(3)
    
    # List pending tasks
    print("\nPending tasks:")
    for task in todo.get_pending_tasks():
        print(f"  [○] {task['id']}. {task['description']}")
    
    # List completed tasks
    print("\nCompleted tasks:")
    for task in todo.get_completed_tasks():
        print(f"  [✓] {task['id']}. {task['description']}")
    
    # Remove a task
    print("\nRemoving task 2...")
    todo.remove_task(2)
    
    # List all tasks after removal
    print("\nAll tasks after removal:")
    for task in todo.list_tasks():
        status = "✓" if task['completed'] else "○"
        print(f"  [{status}] {task['id']}. {task['description']}")
    
    print("\n=== Demo Complete ===\n")

# Main execution
if __name__ == "__main__":
    result = add(5, 3)
    print("The sum is:", result)
    
    # Run the todo list demo
    demo_todo_list()