#!/usr/bin/node
const request = require('request');

const api = process.argv[2];
const usersTasks = {};

request(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const userTasksJSON = JSON.parse(body);

    for (const userTask of userTasksJSON) {
      if (userTask.completed === true) {
        if (!usersTasks[userTask.userId]) {
          usersTasks[userTask.userId] = 0;
        }
        usersTasks[userTask.userId] += 1;
      }
    }
    console.log(usersTasks);
  }
});
