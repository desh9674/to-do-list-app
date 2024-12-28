import React, { useState } from 'react';
import axios from 'axios';

function TaskForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://localhost:8000/tasks/', {
      title: title,
      description: description
    })
    .then(response => {
      console.log(response.data);
      // Optionally, refresh the task list here
    })
    .catch(error => {
      console.error('There was an error creating the task!', error);
    });
  };

  return (
    <form onSubmit={handleSubmit} className="mb-3">
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
      <button type="submit" className="btn btn-primary">Add Task</button>
    </form>
  );
}

export default TaskForm;
