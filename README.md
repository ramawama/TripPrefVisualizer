# TripPrefVisualizer &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) 
> Additional information or tag line

A developer's guide to getting started!

## Installing / Getting started

1. Download Node.Js: https://nodejs.org/en/download

2. Download Python 3.12.2 and/or add to PATH: https://www.python.org/downloads/

3. Download Pipenv
```shell
    pip install --user pipenv
``` 

- Next, navigate to the client directory in a new terminal and download all the dependencies for the front-end
```shell
cd ./client
npm install
```
> This installs all the necessary Node.js packages listed in package.json and package-lock.json.
- 
4. Initialize the frontend and backend
- In the client directory, run
```shell
npm run dev
```

- In your terminal, change the directory to server then:
    * For windows type :
```shell
pipenv run python server.py
``` 
    * For MAC type :
```shell
pipenv run python3 server.py
``` 

Here is a beetle for good luck! 
```shell
  \         /         
   `-.`-'.-'
   ,:--.--:.
  / |  |  | \
   /\  |  /\
   | `.:.' |
```

## Developing 

### What to do with bugs
```shell
                      _                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [bug] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        
Squash them!!
```
- Create a detailed issue on GitHub including how to replicate and potential causes/fixes.
