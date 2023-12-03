#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

list.map((elem, idx) => elem * idx);
console.log(list);
