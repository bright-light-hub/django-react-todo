import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [todos, setTodos] = useState([])
  const [newTitle, setNewTitle] = useState('') // 1. State for the input box

  // Load data on start
  useEffect(() => {
    fetchTodos()
  }, [])

  const fetchTodos = () => {
    fetch('http://127.0.0.1:8000/api/todos/')
      .then(res => res.json())
      .then(data => setTodos(data))
  }

  // 2. The function to Create a new task
  const createTodo = (e) => {
    e.preventDefault() // Stop page refresh

    fetch('http://127.0.0.1:8000/api/todos/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ 
        title: newTitle,
        // We can add defaults for other fields if needed
      }) 
    })
    .then(response => {
      if (response.ok) {
        fetchTodos() // Refresh the list
        setNewTitle('') // Clear the input box
      } else {
        alert("Something went wrong!")
      }
    })
    .catch(error => console.error(error))
  }

  return (
    <div className="App">
      <h1>Django + React Todo App</h1>

      {/* 3. The Form */}
      <form onSubmit={createTodo}>
        <input 
          type="text" 
          value={newTitle}
          onChange={(e) => setNewTitle(e.target.value)}
          placeholder="Enter a new task..."
        />
        <button type="submit">Add Task</button>
      </form>
      
      <hr />

      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
             {todo.title}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App