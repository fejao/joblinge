
const http = require('http');

const server = http.createServer();

server.on('connection', () => {
  console.log('New connection...');
});

// Set the server to listen at the port 3000
server.listen(3000);

console.log('Listening on port 3000...');
