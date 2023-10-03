while True:
    print("Menu:")
    print("1.Calculate Area")
    print("2.Calculate Perimeter")
    print("3.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1 :
        print("Calculating area...")
    elif choice == 2:
        print("Calculating perimeter...")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice.please try again.")