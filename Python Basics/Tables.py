num = ""
while num.lower() != "quit":

    num = input("Enter a number for Table: ")
    if num.lower() == "quit":
        break
    a = input("Enter the range for Table: ")
    if a.lower() == "quit":
        break
    try:
        num = int(num)
        a = int(a)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if a > 0:

        i = 1
        while i < a + 1:
            print(f"{num} x {i} = {num * i}")
            i += 1
    else:

        z = -1
        while z > a - 1:
            print(f"{num} x {z} = {num * z}")
            z -= 1

    num = str(num)
    a = str(a)
