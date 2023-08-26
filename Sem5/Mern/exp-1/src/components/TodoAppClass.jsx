import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import { Grid, Typography } from '@mui/material';

class TodoAppClass extends Component {
  constructor(props) {
    super(props);
    this.state = {
      todos: [],
      newTodo: '',
    };
  }

  handleInputChange = (event) => {
    this.setState({ newTodo: event.target.value });
  };

  handleAddTodo = () => {
    if (this.state.newTodo.trim() !== '') {
      this.setState((prevState) => ({
        todos: [...prevState.todos, prevState.newTodo],
        newTodo: '',
      }));
    }
  };

  render() {
    return (
      <Paper elevation={3} style={{ padding: '20px', margin: '20px' }}>
        <Typography variant="h5" fontWeight={500}>
          List (Class Component)
        </Typography>
        <ul>
          {this.state.todos.map((todo, index) => (
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
            value={this.state.newTodo}
            onChange={this.handleInputChange}
            fullWidth
          />
          <Button
            variant="contained"
            onClick={this.handleAddTodo}
            sx={{ marginLeft: 2 }}
          >
            +
          </Button>
        </Grid>
      </Paper>
    );
  }
}

export default TodoAppClass;
