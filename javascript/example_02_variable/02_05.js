
// Variable einsetzen
const steuersatz = 0.3;

// Mann sollte nicht wieder einsetzen ein 'const'
steuersatz = 0.4;

// Ausdruecken steuersatz -> TypeError: Assignment to constant variable.
console.log(steuersatz);

