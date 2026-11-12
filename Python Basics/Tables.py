num = ""
while num.lower() != "quit":

    num = input("Enter a number for Table: ")
    a =input("Enter the range for Table: ")
    if num.lower() == "quit" or a.lower() == "quit":
        break
    a = int(a)
    num = int(num)
    i = 1
    while i < a + 1:
        print(f"{num} x {i} = {num * i}")
        i += 1
    num = str(num)

