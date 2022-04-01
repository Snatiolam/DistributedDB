import yadb

HOST = "127.0.0.1"

myConnection = yadb.connect(HOST, 'MyOtherDB')
myTable = myConnection.get("Siata")

# myTable.put("pruebas", ["apple", "banana", "cherry"])
# myTable.put("care monda", "Shiiii")
# myTable.get("key1")
myTable.delete("pruebas", "value 1")
# myTable.update("key1", "old val", "new val")

myTable.close()