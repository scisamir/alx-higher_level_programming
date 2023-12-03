#!/usr/bin/node
function fct (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  }

  return (num * fct(num - 1));
}

console.log(fct(parseInt(process.argv[2])));
