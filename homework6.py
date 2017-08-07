
for i in range(1, 101, 1):
    if i % 2 == 0 and i % 3 == 0:
            print (i, "fizzbuzz")
    elif i % 2 == 0:
            print (i, "fizz")
    elif i % 3 == 0:
        print (i, "buzz")
    else:
        print (i, "you're still a number")
