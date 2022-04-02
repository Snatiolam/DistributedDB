import yadb

HOST = "127.0.0.1"

myConnection = yadb.connect(HOST, 'MyOtherDB')
myTable = myConnection.get("Siata")

myTable.put("radio", ["apple", "banana", "cherry"])
# myTable.put("care monda", "Shiiii")
# myTable.delete("pruebas", "value 1")
# lista = myTable.get("care monda")
#print(lista)
#print(lista) 
#myTable.update("pesero", ["rojo", "azul", "morado"])

myTable.close()
