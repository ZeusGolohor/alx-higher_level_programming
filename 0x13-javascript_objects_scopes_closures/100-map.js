#!/usr/bin/node

const { list } = require('./100-data');

const res = list.map((el, index) => el * index);
console.log(list);
console.log(res);
