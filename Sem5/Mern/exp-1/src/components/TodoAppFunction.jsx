import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import { Grid, Typography } from '@mui/material';

const TodoAppFunction = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  const handleInputChange = (event) => {
    setNewTodo(event.target.value);
  };

  const handleAddTodo = () => {
    if (newTodo.trim() !== '') {
      setTodos([...todos, newTodo]);
      setNewTodo('');
    }
  };

  return (
    <Paper elevation={3} style={{ padding: '20px', margin: '20px' }}>
      <Typography variant="h5" fontWeight={500}>
        List (Function Component)
      </Typography>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>{todo}</li>
        ))}
      </ul>
      <Grid
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <TextField
          label="Add Todo"
          variant="outlined"
          value={newTodo}
          onChange={handleInputChange}
          fullWidth
        />
        <Button
          variant="contained"
          onClick={handleAddTodo}
          sx={{ marginLeft: 2 }}
        >
          +
        </Button>
      </Grid>
    </Paper>
  );
};

export default TodoAppFunction;
