import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Task from './Task';

function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [editTask, setEditTask] = useState(null);  // State for selected task to edit
  const [newTaskData, setNewTaskData] = useState({ title: '', description: '', is_completed: false });  // State for editing task data

  const handleEdit = (task) => {
    setEditTask(task);  // Set the task to be edited
    setNewTaskData({ title: task.title, description: task.description, is_completed: task.is_completed });  // Populate form with current data
  };

  const handleDelete = (taskId) => {
    setTasks(tasks.filter(task => task.id !== taskId));
  };

  const handleEditSubmit = (event) => {
    event.preventDefault();
    const updatedTask = { ...editTask, ...newTaskData };  // Merge new task data with the selected task

    // Update the task in the backend
    axios.put(`http://localhost:8000/tasks/${editTask.id}`, updatedTask)
      .then(response => {
        // Update the task in the state after successful update
        setTasks(tasks.map(task => (task.id === editTask.id ? response.data : task)));
        setEditTask(null);  // Close the edit form
      })
      .catch(error => {
        console.error('Error updating task:', error);
        alert('Failed to update task');
      });
  };

  useEffect(() => {
    axios.get('http://localhost:8000/tasks/')
      .then(response => {
        setTasks(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the tasks!', error);
        setError('Failed to fetch tasks');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      {editTask && (
        <div className="edit-form">
          <h3>Edit Task</h3>
          <form onSubmit={handleEditSubmit}>
            <div className="mb-3">
              <input
                type="text"
                value={newTaskData.title}
                onChange={(e) => setNewTaskData({ ...newTaskData, title: e.target.value })}
                className="form-control"
                placeholder="Task Title"
              />
            </div>
            <div className="mb-3">
              <input
                type="text"
                value={newTaskData.description}
                onChange={(e) => setNewTaskData({ ...newTaskData, description: e.target.value })}
                className="form-control"
                placeholder="Task Description"
              />
            </div>
            <div className="mb-3">
              <label>
                <input
                  type="checkbox"
                  checked={newTaskData.is_completed}
                  onChange={(e) => setNewTaskData({ ...newTaskData, is_completed: e.target.checked })}
                />
                Completed
              </label>
            </div>
            <button type="submit" className="btn btn-primary">Save Changes</button>
            <button type="button" className="btn btn-secondary" onClick={() => setEditTask(null)}>Cancel</button>
          </form>
        </div>
      )}

      {!editTask && (
        <div>
          {tasks.map(task => (
            <Task
              key={task.id}
              task={task}
              onDelete={handleDelete}
              onEdit={handleEdit} // Pass the onEdit function here
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default TaskList;
