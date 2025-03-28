import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL; // Read env variable

function TaskList({ tasks, setTasks }) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [editTask, setEditTask] = useState(null);
  const [newTaskData, setNewTaskData] = useState({ title: '', description: '', is_completed: false });

  const handleEdit = (task) => {
    setEditTask(task);
    setNewTaskData({ title: task.title, description: task.description, is_completed: task.is_completed });
  };

  const handleDelete = (taskId) => {
    setTasks(tasks.filter(task => task.id !== taskId));
  };

  const handleEditSubmit = (event) => {
    event.preventDefault();
    const updatedTask = { ...editTask, ...newTaskData };

    axios.put(`${API_BASE_URL}/tasks/${editTask.id}`, updatedTask)
      .then(response => {
        setTasks(tasks.map(task => (task.id === editTask.id ? response.data : task)));
        setEditTask(null);
      })
      .catch(error => {
        console.error('Error updating task:', error);
        alert('Failed to update task');
      });
  };

  useEffect(() => {
    axios.get(`${API_BASE_URL}/tasks/`)
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
      {editTask ? (
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
      ) : (
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>Task Name</th>
              <th>Description</th>
              <th>Created Date</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map(task => (
              <tr key={task.id}>
                <td>{task.title}</td>
                <td>{task.description}</td>
                <td>{new Date(task.created_at).toLocaleString()}</td>
                <td>
                  <span className={`badge ${task.is_completed ? 'bg-success' : 'bg-danger'}`}>
                    {task.is_completed ? 'Completed' : 'Pending'}
                  </span>
                </td>
                <td>
                  <button className="btn btn-warning btn-sm me-2" onClick={() => handleEdit(task)}>Edit</button>
                  <button className="btn btn-danger btn-sm" onClick={() => handleDelete(task.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default TaskList;
