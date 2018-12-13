
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.write('Hello World!');
    res.end();
  }

  if (req.url === '/api/courses') {
    res.write(JSON.stringify([1, 2, 3]));
    res.end();
  }
});

server.on('connection', () => {
  console.log('New connection...');
});

// Set the server to listen at the port 3000
server.listen(3000);

console.log('Listening on port 3000...');