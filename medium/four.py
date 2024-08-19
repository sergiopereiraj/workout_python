"""
Conversor de Unidades:
Escribe una función que convierta entre diferentes unidades de medida 
(por ejemplo, de metros a pies, de kilogramos a libras, etc.).

"""
class Converter:

    @staticmethod
    def fromMetreToFoot(x):
        foot = 3.28084
        return x * foot
    
    @staticmethod
    def fromFootToMetre(x):
        metre = 0.3048
        return x * metre
    
    @staticmethod
    def fromFahrenheitToCelsius(x):
        celsius = (x - 32)* 5 / 9
        return celsius
    
    @staticmethod
    def fromCelsiustoFahrenheit(x):
        fahrenheit = (x * (9/5)) + 32
        return fahrenheit
    
def main():
    while True:
        print("\n Choise a method:")
        print("1: From Metre to Foot")
        print("2: From Foot to Metre")    
        print("3: From Fahrenheit to Celsius")
        print("4: From Celsius to Fahrenheit")
        print("5: Exit")
    
        choice = input("Insert number: ")

        if choice == "1":
            value = float(input("Value in metre: "))
            result = Converter.fromMetreToFoot(value)
            print(f"{value} are {result} foot")
        elif choice == "2":
            value = float(input("Value in foot: "))
            result = Converter.fromFootToMetre(value)
            print(f"{value} are {result} metres")
        elif choice == "3":
            value = float(input("Value in Fahrenheit: "))
            result = Converter.fromFahrenheitToCelsius(value)
            print(f"{value} are {result} ° Celsius")
        elif choice == "4":
            value = float(input("Value in Celsius: "))
            result = Converter.fromCelsiustoFahrenheit(value)
            print(f"{value} are {result} ° Fahrenheit")
        elif choice == "5":
            print("See you!!!")
            break
        else:
            print("Invalid Election")

if __name__ == "__main__":
    main()