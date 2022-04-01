import yadb

HOST = "127.0.0.1"

myConnection = yadb.connect(HOST, 'MyOtherDB')
myTable = myConnection.get("Siata")

myTable.put("pruebxs", ["apple", "banana", "cherry"])
# myTable.get("key1")
# myTable.delete("key1", "value 1")
# myTable.update("key1", "old val", "new val")

myTable.close()