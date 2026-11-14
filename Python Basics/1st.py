import string
a = "apple is eating a banana and, a mango is delicious!! because it is; sweet and j;uicy"

a = a.translate(str.maketrans('', '', string.punctuation))

splited_a = a.split(" ")
count = 0
i = 0
while i < len(splited_a):
    count = splited_a.count(splited_a[i])
    print(f"{splited_a[i]} : {count}")
    i += 1
