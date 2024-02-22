#!/usr/bin/node
const request = require('request');

function stat (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode !== 200) {
        console.error('Failed to fetch data');
        return;
      }
      const tasks = JSON.parse(body);
      const completedTasks = tasks.filter(task => task.completed);
      const completedByUser = {};
      completedTasks.forEach(task => {
        const userId = task.userId;
        if (completedByUser[userId]) {
          completedByUser[userId]++;
        } else {
          completedByUser[userId] = 1;
        }
      });
      console.log(completedByUser);
    }
  });
}

if (process.argv.length === 3) {
  const url = process.argv[2];
  stat(url);
} else {
  console.log('Usage: script <URL>');
}
