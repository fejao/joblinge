![Joblinge Express Logo](logo_joblinge_express.png?raw=true "Joblinge Express logo")

[![License GLP3](https://img.shields.io/badge/license-GPL3-red.svg)](LICENSE.md)
[![HitCount](http://hits.dwyl.io/fejao/joblinge/express.svg)](http://hits.dwyl.io/fejao/joblinge/express)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/fejao/joblinge/issues)

Express
===============
Examples with Express
_____________________________________________

- ## 1- CRUD Operations
  - Create
  - Read
  - Update
  - Delete

- ## 2- Specify an endpoint
  Retrieve information from an endpoint, for example: (http://mycompany.com/api/customers)

- ## 3- HTTP Methods
  All *HTTP* methods with it's action

  **Method** | **Action**
  ----|----
  *GET* | Retrieve data
  *POST* | Create data
  *PUT* | Update data
  *DELETE* | Delete data

  - ### 3.1- Retrieve data
    How can we fetch data

    - #### 3.1.1- Retrieve all
      Request:
      ```
      GET /api/customers
      ```
      Response:
      ```
      [
        { id: 1, name: 'Bruno'},
        { id: 2, name: 'Andres'},
        ...
      ]
      ```

    - #### 3.1.2- Retrieve Single
      For *retrieving* a single request, we should parse something to identify the information searched, in this case, the **id** from the costumer
      Request
      ```
      GET /api/customers/1
      ```
      Response:
      ```
      { id: 1, name: 'Bruno'}
      ```

  - ### 3.2- Update data
    For *updating* information we also need to specify it, in this case also using the **id** form the customer
    Request:
    ```
    PUT /api/customers/1
    { name: 'Martin'}
    ```
    Response:
    ```
    { id: 1, name: 'Martin'}
    ```

  - ### 3.3- Delete data
    For *deleting* information we also need to specify it, in this case also using the **id** form the customer
    Request:
    ```
    PUT /api/customers/1
    ```
    Response:
    ```
    ??? -> you can return something or not
    ```

  - ### 3.4- Create data
    For creating data/information we need to parse the values that are needed for creating it, in this case, sending the **name** of the customer
    Request:
    ```
    POST /api/customers
    { name: 'Frida'}
    ```
    Response:
    ```
    { id: 3, name: 'Frida'}
    ```
