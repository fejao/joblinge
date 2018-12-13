
const fs = require('fs');

const files = fs.readdirSync('./');

console.log(files); // --> [ 'app_1.js, app_2.js' ]
