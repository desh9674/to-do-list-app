import React from 'react';
import TaskList from './TaskList';
import TaskForm from './TaskForm';

function App() {
  return (
    <div className="container">
      <h1 className="my-4">To-Do List</h1>
      <TaskForm />
      <TaskList />
    </div>
  );
}

export default App;
