
const path = require('path');

var pathObj = path.parse(__filename);

console.log(pathObj);
// {
//   root: '/',
//   dir: '/media/DATA/Coding/joblinge_repositories/joblinge/node/example_04_path_module',
//   base: 'app.js',
//   ext: '.js',
//   name: 'app'
// }
