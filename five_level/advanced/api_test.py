"""
import requests


empleados = "https://api.hcmfront.com/v1/employee/"


headers = {
    'Authorization': 'Token ec55ee1783949d07d0f257a5ea05816c9613112e6a38031db5909fcbbd22eab3', 
    'Content-Type': 'application/json',
}

e = requests.get(empleados, headers=headers)


def name_id (x:list):
    new_list = []
    for i in x:
        n = i["name"]
        n2 = i["last_name"]
        n3 = i["second_last_name"]
        n3 = i["identification_number"]
        n4 = i["position_data"]["name"]
        new_list.append(n)
        new_list.append(n2)
    return new_list

#l = [(i["name"],i["last_name"],i["position_data"]["name"]) for i in one]
"""
n = int(input("¿Cual es la cantidad de horas pedagogicas diarias?: "))

def total_pago (x:int):
    pago_semana = (6400 * x)*3
    return int((pago_semana * 4) * 0.87)

pasaje_mes = (1600 * 3) * 4

total_retorno = int(total_pago(n) - pasaje_mes)
print(f"Total pasaje: {pasaje_mes}")
print(f"Total pago, con descuento impuesto: {total_pago(n)}")
print(f"Total que voy a recibir: {total_retorno}")