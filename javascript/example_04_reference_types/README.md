
# Reference Types

- ## 1- Objects
  AAA

  - ### 1.1- Declaration
    Is a object in real life, for example a person
    It has a name, age, address and etc.
    key-> values
    ```javascript
    let object = {
      key1: 'value1',
      key2: 'value2',
      key3: 'value3',
      ...
      keyN: 'valueN',
    };
    ```
    Using a person for example, it would be:
    ```javascript
    let name = 'Bruno';
    let age = 40;
    let address = 'Meinstr. 23';

    let person = {
      name: 'Bruno',
      age: 30,
      address: 'Meinstr. 23'
    };
    ```

  - ### 2.2- Dot notation
    How to access or change a value from a key in a object

    Access
    ```javascript
    console.log(person.name);
    ```
    Change
    ```javascript
    person.name = 'Andres';
    ```

  - ### 2.3- Brackets notation
    How to access or change a value from a key in a object

    Access
    ```javascript
    console.log(person['name']);
    console.log(person["name"]);
    ```

    Change
    ```javascript
    person['name'] = 'Andres';
    ```

    Advantage
    ```javascript

    let selection = 'name';
    console.log(person[selection]);
    ```

- ## 2- Array
  List of objects, for example, the list of items a user have selected

  - ### 2.1- AAA
    AAA

    ```javascript
    let selectedColors = [
      'red',
      'blue'
    ];
    ```
    Access
    ```javascript
    console.log(selectedColors);
    ```

  - ### 2.2- AAA
    AAA

- ## 3- Function
  AAA

  - ### 3.1- Declaration
    AAA
    ```javascript
    function sayHello() {
      console.log('Hello World');
    }
    ```

  - ### 3.1- AAA
    AAA
    ```javascript
    ```
