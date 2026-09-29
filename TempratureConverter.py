def convert():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Enter your choice: "))
    temp = float(input("Enter temperature: "))

    if choice == 1:
        print("Result:", (temp * 9 / 5) + 32, "°F")

    elif choice == 2:
        print("Result:", (temp - 32) * 5 / 9, "°C")

    elif choice == 3:
        print("Result:", temp + 273.15, "K")

    elif choice == 4:
        print("Result:", temp - 273.15, "°C")

    else:
        print("Invalid choice")


convert()