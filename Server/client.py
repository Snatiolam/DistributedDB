import yadb

HOST = "127.0.0.1"

myConnection = yadb.connect(HOST, 'MyDB')
myTable = myConnection.get("Tabla Prueba")
myTable.get("key1")
# myTable.put("key1", "algun dato simple o complejo")
# myTable.delete("key1", "value 1")
# myTable.update("key1", "old val", "new val")
# myTable.close()
myTable.close()