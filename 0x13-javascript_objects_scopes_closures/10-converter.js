#!/usr/bin/node

exports.converter = (base) => {
  return (num) => {
    return (parseInt(num, base));
  };
};
