"""
Conversión de tipo en matrices dispersas:
Dado un array esparcido (sparse array) donde la mayoría de los elementos son ceros, 
convierte los elementos no nulos en cadenas que representen sus valores binarios.
Entrada: [0, 3, 0, 5, 0, 8]
Salida: [0, "11", 0, "101", 0, "1000"]
"""
entrada = [0, 3, 0, 5, 0, 8]
def become_to_binary(x:list):
    new_list = []
    for i in range(len(x)):
        if x[i] != 0:
            new_list.append(bin(x[i])[2:])
        elif x[i] == 0:
            new_list.append(x[i])
    return new_list

print(become_to_binary(entrada))