import typer
from typing import List
import yadb

HOST = "127.0.0.1"

def main(create: bool = False, read: bool = False, update: bool = False, delete: bool = False, database: str = typer.Argument(..., help="Database to make the request"), table: str = typer.Argument(..., help="Table to make the request"), key: str = typer.Argument(..., help="Key for value"), values: List[str] = typer.Argument(None, help="Values for Write operations")):
    myConnection = yadb.connect(HOST, database)
    myTable = myConnection.get(table)
    if create:
        #python client.py --create Siata Estaciones 001 "hola como estas?", "cama"
        if values is None:
            raise typer.Exit('You must provide values for create operation')
        typer.echo("Creating new key")
        typer.echo(key + ": " + str(type(values)))
        values = list(values)
        myTable.put(key, values)
        myTable.close()
    elif read:
        #python client.py --read Siata Estaciones 001
        typer.echo("Reading a key")
        typer.echo(key)
        lista = myTable.get(key)
        typer.echo(lista)
        myTable.close()
    elif update:
        #python client.py --update Siata Estaciones 001 "Estoy muy bien, gracias", "avion", "restaurante"
        if values is None:
            raise typer.Exit('You must provide values for update operation')
        typer.echo("Updating a key")
        values = list(values)
        myTable.update(key, values)
        myTable.close()
    elif delete:
        #python client.py --delete Siata Estaciones 001
        typer.echo("Deleting a key")
        typer.echo(key)
        typer.echo(key + ": " + str(values))
        myTable.delete(key)
        myTable.close()
    else:
        typer.echo("No action selected. Use --help to see the options")



if __name__ == "__main__":
    typer.run(main)