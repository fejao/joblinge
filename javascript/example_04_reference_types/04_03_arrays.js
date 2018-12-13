
//
let selectedColors = [
  'red',
  'blue'
];

// Test output from the created array -> [ 'red', 'blue' ]
console.log(selectedColors);

// Display only the first element -> 'red'
console.log(selectedColors[0]);

// Ypu can add to the array
selectedColors[2] = 'green';
console.log(selectedColors); // [ 'red', 'blue', 'green' ]

// Ypu can also change the content
selectedColors[2] = 1;
console.log(selectedColors); // [ 'red', 'blue', 1 ]

// The array length
console.log(selectedColors.length); // 3
