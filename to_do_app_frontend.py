const apiUrl = 'http://localhost:5000/api/tasks'; // Updated backend URL

// Fetch tasks
async function fetchTasks() {
    const response = await fetch(apiUrl);
    const tasks = await response.json();
    taskList.innerHTML = '';
    tasks.forEach(task => addTaskToDOM(task));
}

// Add a new task
taskForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const taskName = taskInput.value.trim();
    if (!taskName) return;

    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: taskName }),
    });

    if (response.ok) {
        const newTask = await response.json();
        addTaskToDOM(newTask);
        taskInput.value = '';
    } else {
        alert('Failed to add task');
    }
});

// Delete a task
async function deleteTask(taskId) {
    const response = await fetch(`${apiUrl}/${taskId}`, {
        method: 'DELETE',
    });

    if (response.ok) {
        document.querySelector(`button[data-id="${taskId}"]`).parentElement.remove();
    } else {
        alert('Failed to delete task');
    }
}
