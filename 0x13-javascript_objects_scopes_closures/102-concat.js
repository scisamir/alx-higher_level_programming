#!/usr/bin/node

const fs = require('fs');

const src1 = fs.readFileSync(process.argv[2]).toString();
const src2 = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], src1 + src2);
