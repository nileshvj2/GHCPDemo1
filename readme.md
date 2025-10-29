This is demo

## Todo Task List Functionality

This repository now includes a simple Todo Task List implementation.

### Features:
- Add tasks to a todo list
- Mark tasks as completed
- Remove tasks
- View all tasks, pending tasks, or completed tasks

### Usage:
Run the script to see a demo of the todo list functionality:
```bash
python3 index.py
```

### TodoList Class Methods:
- `add_task(description)`: Add a new task
- `remove_task(task_id)`: Remove a task by ID
- `mark_completed(task_id)`: Mark a task as completed
- `list_tasks()`: Get all tasks
- `get_pending_tasks()`: Get pending tasks
- `get_completed_tasks()`: Get completed tasks

### Example:
```python
todo = TodoList()
todo.add_task("Buy groceries")
todo.add_task("Complete project")
todo.mark_completed(1)
print(todo.list_tasks())
```
