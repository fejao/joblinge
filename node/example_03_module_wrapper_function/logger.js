// How NODE sees it
// (function(exports, require, module, __filename, __dirname) {

console.log(__filename);
console.log(__dirname);


function log(message) {
  console.log(message);
}

module.exports = log;

// exports = log  --> module.exports
// })
