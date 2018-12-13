
const EventEmitter = require('events');
// const emitter = new EventEmitter();

// Load the logger
const Logger = require('./logger');
const logger = new Logger();

// Register a listener from eventes: messageLogged
// emitter.on('messageLogged', (eventArg) => {
logger.on('messageLogged', (eventArg) => {
  console.log('Listener called', eventArg);
});

// Call the log with message
logger.log('message using emitter');
