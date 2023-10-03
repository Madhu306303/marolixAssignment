choice = input("Enter your choice (C to F or F to C): ")
if choice == "C to F":
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius *9/5)+32
        print(f"The temperature in fahrenheit is:{fahrenheit}F")
elif choice == "F to C":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius =(fahrenheit -32)*5/9
        print(f"The temperature in celsius is :{celsius} C")
else:
        print("Invalid choice.Try again.")