#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

const firstFile = fs.readFileSync(args[2], 'utf-8');
const secondFile = fs.readFileSync(args[3], 'utf-8');

fs.writeFileSync(args[4], firstFile + secondFile);
