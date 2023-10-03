a = int(input("enter a value"))
count = 0
for i in range(2,a):
    if(a%i==0):
        count = count+1
        break
    if(count==0):
        print("the given number is prime number")
    else:
        print("the given number is not prime number")