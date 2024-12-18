import sqlite3
import json

# Initialize the SQLite Database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create the Task table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')
conn.commit()

def get_tasks():
    """Get all tasks."""
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    tasks = [{'id': row[0], 'name': row[1]} for row in rows]
    return json.dumps(tasks, indent=2)

def add_task(name):
    """Add a new task."""
    cursor.execute('INSERT INTO tasks (name) VALUES (?)', (name,))
    conn.commit()
    task_id = cursor.lastrowid
    return json.dumps({'id': task_id, 'name': name}, indent=2)

def delete_task(task_id):
    """Delete a task by ID."""
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    if cursor.rowcount > 0:
        conn.commit()
        return "Task deleted successfully."
    else:
        return "Task not found."

# Simulate a command-line interface for testing
if __name__ == "__main__":
    while True:
        print("\nTo-Do App Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nTasks:")
            print(get_tasks())

        elif choice == '2':
            name = input("Enter task name: ")
            print("\nTask Added:")
            print(add_task(name))

        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            print("\n" + delete_task(task_id))

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
