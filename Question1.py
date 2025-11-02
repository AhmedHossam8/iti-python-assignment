def Celsius_to_Fahrenheit(degree):
    f = degree * (9/5) + 32
    print(f"Degree from Celsius to Fahrenheit = {f} °f")

def Fahrenheit_to_Celsius(degree):
    c = degree - 32 * (5/9)
    print(f"Degree from Fahrenheit to Celsius = {c} °c")

def Celsius_to_Kelvin(degree):
    k = degree + 273.15
    print(f"Degree from Celsius to Kelvin = {k} °k")
    
def Kelvin_to_Celsius(degree):
    c = degree - 273.15
    print(f"Degree from Kelvin to Celsius = {c} °c")

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    while True:
        choice = int(input("Choose conversion (1-4):"))
        degree = float(input("Enter temperature: "))
        if choice == 1:
            if degree < -5 or degree > 60:
                print("Invalid Degree")
            else:
                Celsius_to_Fahrenheit(degree)
                break
        
        elif choice == 2:
            if degree < 23 or degree > 140:
                print("Invalid Degree")
            else:
                Fahrenheit_to_Celsius(degree)
                break
        
        elif choice == 3:
            if degree < -5 or degree > 60:
                print("Invalid Degree")
            else:
                Celsius_to_Kelvin(degree)
                break
        
        elif choice == 4:
            if degree < 268.15 or degree > 333.15:
                print("Invalid Degree")

            else:
                Kelvin_to_Celsius(degree)
                break
        
        else:
            print("Invalid choice")

main()