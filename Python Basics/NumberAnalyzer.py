num =  ""
while True:
    num =  input("Enter a number(Type Quit to exit): ")
    if num.lower() == "quit":
        print("Exiting the program.")
        break
    
    try:
        num = int(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if num == 0:
        print("Zero")
    elif num > 0:
        if num % 2 == 0:
            print("Positive Even")
        else :
            print("Positive Odd")
    elif num < 0:
        if num % 2 == 0:
          print("Negative Even")
        else :
            print("Negative Odd")