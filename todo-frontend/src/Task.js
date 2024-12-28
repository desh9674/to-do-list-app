import React from 'react';

function Task({ task }) {
  return (
    <div className="card mb-3">
      <div className="card-body">
        <h5 className="card-title">{task.title}</h5>
        <p className="card-text">{task.description}</p>
        <small className="text-muted">{new Date(task.created_at).toLocaleString()}</small>
      </div>
    </div>
  );
}

export default Task;
