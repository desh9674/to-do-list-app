import React, { useState } from 'react';
import axios from 'axios';

function TaskForm({ onAddTask }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isCompleted, setIsCompleted] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    axios.post('http://localhost:8000/tasks/', {
      title: title,
      description: description,
      is_completed: isCompleted,
    })
    .then(response => {
      console.log(response.data);
      if (onAddTask) {
        onAddTask(response.data); // Add task to the list without refreshing
      }
      setTitle('');
      setDescription('');
      setIsCompleted(false); // Reset the form state
      setError('');
    })
    .catch(error => {
      console.error('There was an error creating the task!', error);
      setError('Failed to create task');
    });
  };

  return (
    <form onSubmit={handleSubmit} className="mb-3">
      {error && <div className="alert alert-danger">{error}</div>}
      <div className="mb-3">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Task Title"
          className="form-control"
        />
      </div>
      <div className="mb-3">
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Task Description"
          className="form-control"
        />
      </div>
      <div className="mb-3">
        <label>
          <input
            type="checkbox"
            checked={isCompleted}
            onChange={(e) => setIsCompleted(e.target.checked)} // Toggle checkbox state
          />
          {' '}Completed
        </label>
      </div>
      <button type="submit" className="btn btn-primary">Add Task</button>
    </form>
  );
}

export default TaskForm;
