# TripPrefVisualizer &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm)
> Additional information or tag line

A brief description of your project, what it is used for.

## Installing / Getting started
1. Get the backend working:
* Download Pipenv
```shell
    pip install --user pipenv
``` 

* Test the backend
    * In your terminal, change the directory to flask-server then:
    * For windows type :
    ```shell
    pipenv run python server.py
    ``` 
    * For MAC type :
    ```shell
    pipenv run python3 server.py
    ``` 

2. Get the frontend working:
* Download Node.Js: https://nodejs.org/en/download
    * Verify that Node.js and npm are installed by opening a command prompt and running the following commands
    ```shell
    node -v npm -v
    ``` 
* Open another terminal (make sure that the backend server is still running)
    * cd to client
    * In your terminal, write:
    ```shell
    npm start
    ``` 
    * You should now see "Member 1, Member 2, and Member 3"


