try:
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter a valid integer.")