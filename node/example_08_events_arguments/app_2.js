
const EventEmitter = require('events');

const emitter = new EventEmitter();

// Register a listener from eventes: messageLogged
// emitter.on('messageLogged', function(eventArg) {
//   console.log('Listener called', eventArg);
// });

emitter.on('messageLogged', (eventArg) => {
  console.log('Listener called', eventArg);
});

// Signals that an event happend
emitter.emit('messageLogged', { id: 1, url: 'http://'});

// Raise: logging(data: message)
