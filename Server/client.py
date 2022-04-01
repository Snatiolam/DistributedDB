import yadb

HOST = "127.0.0.1"

myConnection = yadb.connect(HOST, 'dddddd')
myTable = myConnection.get("ddd")

# myTable.put("pruebas", ["apple", "banana", "cherry"])
# myTable.put("care monda", "Shiiii")
# myTable.get("key1")
#myTable.delete("pruebas", "value 1")
myTable.update("pesero", ["rojo", "azul", "morado"])

myTable.close()