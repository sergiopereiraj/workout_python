"""
Convertir un array de strings en un diccionario:

Dado un array de strings, cada uno en el formato "key:value", 
escribe una función que lo convierta en un diccionario con los tipos de datos adecuados.
Entrada: ["name:John", "age:30", "height:5.8"]
Salida: {"name": "John", "age": 30, "height": 5.8}

"""

entrada = ["name:John", "age:30", "height:5.8"]

def become_to_dict (x:list):
    new_dict = {}
    for i in x:
        key, value = i.split(":")
        
        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():
            value =float(value)
        
        new_dict[key] = value

    return new_dict

print(become_to_dict(entrada))
#print(entrada[0].split(":"))
#print(len(entrada))