#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });
  console.log(completedTasks);
});
