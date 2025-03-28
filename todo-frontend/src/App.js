import React, { useState } from 'react';
import TaskList from './components/TaskList';
import TaskForm from './components/TaskForm';

function App() {
  const [tasks, setTasks] = useState([]);

  const handleAddTask = (task) => {
    setTasks((prevTasks) => [...prevTasks, task]); // Add the new task to the list
  };

  return (
    <div className="container">
      <h1 className="my-4">To-Do List</h1>
      <TaskForm onAddTask={handleAddTask} /> {/* Pass onAddTask to TaskForm */}
      <TaskList tasks={tasks} setTasks={setTasks} /> {/* Pass tasks as props */}
    </div>
  );
}

export default App;
