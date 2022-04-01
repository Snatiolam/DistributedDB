import yadb

HOST = "127.0.0.1"

myConnection = yadb.connect(HOST, 'MyOtherDB')
myTable = myConnection.get("Siata")

# myTable.put("pruebas", ["apple", "banana", "cherry"])
# myTable.put("care monda", "Shiiii")
myTable.get("care monda")
#myTable.delete("pruebas", "value 1")
#myTable.update("pesero", ["rojo", "azul", "morado"])

myTable.close()