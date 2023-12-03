#!/usr/bin/node

const dict = require('./101-data.js').dict;

const myDict = {};

for (const id in dict) {
  const ocr = dict[id];

  if (ocr in myDict) {
    myDict[ocr].push(id);
  } else {
    myDict[ocr] = [id];
  }
}

console.log(myDict);
