# TripPrefVisualizer &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm)
> Additional information or tag line

A developer's guide to getting started!

## Installing / Getting started

1. Download Node.Js: https://nodejs.org/en/download

2. Download Python 3.12.2 and/or add to PATH: https://www.python.org/downloads/

3. Create your virtual envrionment
- in your terminal, go in to the server directory
```shell
cd ./server
```
- write this in your terminal for windows to create and run your venv!
```shell
python -m venv venv
.\venv\Scripts\activate
``` 
-and for MAC
```shell
python -m venv venv
source venv/bin/activate
```

4. Install Dependencies
- Within the venv, download all the required python packages at the correct version using
```shell
pip install -r requirements.txt
```

- Next, navigate to the client directory in a new terminal and download all the dependencies for the front-end
```shell
cd ./client
npm install
```

5. Initialize the frontend and backend
- In the client directory, run
```shell
npm run dev
```

- In your terminal, change the directory to server then:
- For windows type :
```shell
python server.py
``` 
- For MAC type :
```shell
python3 server.py
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
