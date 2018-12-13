

// Declaration of the object person
let person = {
  name: 'Bruno',
  age: 30,
  address: 'Meinstr. 23'
}

// Change the value of the name key from the object person
person.name = 'Andres';

// Print: name should have changed
console.log(person.name); // Andres

// Change the value of the name key from the object person
person['name'] = 'Martin';

// Print: name should have changed
console.log(person['name']); // Martin

let selection = 'name';
// Print: name should have changed
console.log(person[selection]); // Martin
