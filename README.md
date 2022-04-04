# SSJ Distributed DataBase System

## About The Project

his is a project where we implement a simple distributed database using the master-slaves arquitecture with a single leader.

### Usage

#### Client CLI
1. Set up a python virtual enviroment
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install project Dependencies
    ```sh
    pip install -r requirements.txt
    ```
3. Run client (see example)
    ```sh
    python client.py --create Eafit Sistemas Telematica "La mejor clase del mundo" "Vamos a sacar 5.0"
    ```
You are ready to go.
You can run `--help` tag to find more about the app

Usage: client.py [OPTIONS] DATABASE TABLE KEY [VALUES]...

Arguments:
  DATABASE     Database to make the request  [required]
  TABLE        Table to make the request  [required]
  KEY          Key for value  [required]
  [VALUES]...  Values for Write operations

Options:
  --create / --no-create          [default: no-create]
  --read / --no-read              [default: no-read]
  --update / --no-update          [default: no-update]
  --delete / --no-delete          [default: no-delete]
  
#### Server (Database Interface)
1. Set up a python virtual enviroment
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install project Dependencies
    ```sh
    pip install -r requirements.txt
    ```
3. Run server
    ```sh
    python database_selector.py
    ```
    
#### Master and Slave Database
1. Set up a python virtual enviroment
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install project Dependencies
    ```sh
    pip install -r requirements.txt
    ```
3. Run server
    ```sh
    python server.py
    ```
    
### References
- https://realpython.com/python-sockets/
- https://elvex.ugr.es/decsai/information-systems/slides/32%20Data%20Access%20-%20NoSQL.pdf
- https://www.acens.com/wp-content/images/2014/02/bbdd-nosql-wp-acens.pdf
- https://es.wikipedia.org/wiki/Base_de_datos_distribuida
