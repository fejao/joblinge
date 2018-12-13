// CLASS   -> HUMAN
// OBJECT  -> John

// EventEmitter is a CLASS
const EventEmitter = require('events');

const emitter = new EventEmitter();

// Register a listener from eventes: messageLogged
emitter.on('messageLogged', function() {
  console.log('Listener called');
});


// EMIT: make, produce,

// Signals that an event happend
emitter.emit('messageLogged');
