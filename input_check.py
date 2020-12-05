def input_check():
    num = int(input("Give me a number: "))
    if num > 10 and num < 20:
        print("Yay! {} is between 10 and 20".format(num))
    else:
        print("BOO! {} is not between 10 and 20".format(num))

input_check()
