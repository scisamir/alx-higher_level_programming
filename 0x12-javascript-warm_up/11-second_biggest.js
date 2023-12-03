#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const bgst = [0, 0];

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > bgst[0]) {
      bgst[0] = num;

      if (bgst[0] > bgst[1]) {
        const temp = bgst[0];
        bgst[0] = bgst[1];
        bgst[1] = temp;
      }
    }
  }

  console.log(bgst[0]);
}
