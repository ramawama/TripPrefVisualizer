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
4. Install dependencies
    * First, make sure you are in the server folder in TripPrefVisualizer, then put this in your command line 
```shell
pipenv install
```
> This will be used to automatically create and manage a virtualenv!

- Next, navigate to the client directory and download all the dependencies for the front-end
```shell
cd ./client
npm install
```
> This installs all the necessary Node.js packages listed in package.json and package-lock.json.

5. Initialize the frontend and backend
- In the client directory, run
```shell
npm run dev
```
> This will run the next.js app in development mode, so all changes made in the code will be immediately reflected on the page

- In a **new** terminal, navigate to the server directory then:
* For windows type :
```shell
pipenv run python server.py
```

* For MAC type :
```shell
pipenv run python3 server.py
``` 

6. Enjoy!
- There should now be two local hosts running, one for the backend and one for the front.

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
