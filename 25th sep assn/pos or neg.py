try:
    num = float(input("Please enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input. Please enter a valid number.")
