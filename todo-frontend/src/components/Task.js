import React from 'react';
import axios from 'axios';
import { FaTrash, FaEdit } from 'react-icons/fa';

function Task({ task, onDelete, onEdit }) {
  const handleDelete = () => {
    axios.delete(`http://localhost:8000/tasks/${task.id}`)
      .then(() => onDelete(task.id))
      .catch(error => {
        console.error('Error deleting task:', error);
        alert('Failed to delete task');
      });
  };

  const handleEdit = () => {
    // Calling the passed onEdit function
    onEdit(task);
  };

  return (
    <div className="task-card">
      <div className="task-content">
        <h5>{task.title}</h5>
        <p>{task.description}</p>
        <small>{new Date(task.created_at).toLocaleString()}</small>
        <p className={task.is_completed ? 'text-success' : 'text-danger'}>
          Status: {task.is_completed ? 'Completed' : 'Pending'}
        </p>
      </div>
      <div className="task-actions">
        <button className="icon-btn edit-btn" onClick={handleEdit}>
          <FaEdit />
        </button>
        <button className="icon-btn delete-btn" onClick={handleDelete}>
          <FaTrash />
        </button>
      </div>
    </div>
  );
}

export default Task;
