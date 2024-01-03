import json

data = {
    'id':'001',
    'nombre':'pepe'
}

with open("archivo.json","w") as archivo:
    json.dump(archivo,archivo, indent=2)
    
with open("archivo.json","r") as leer:
    json.dump(archivo,archivo, indent=2)
    
    print(json.load(leer))
    
print(archivo.closed)
print(archivo.name)
print(archivo.encoding)