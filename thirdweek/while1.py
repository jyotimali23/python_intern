while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a valid number!")
    else:
        print("%s squared is %s" % (x, x**2))
        break