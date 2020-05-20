
print("Welcome to unit converter that converts kilometers to miles.")

while True:
    kilometers = float(input("Enter the number of kilometers you wish to convert:"))
    conv_factor = 0.621371

    mi = kilometers * conv_factor
    mi_fin = round(mi, 2)
    print("{0} km equals {1} mi." .format(kilometers, mi_fin))

    answer = input("Would you like to make another conversion?")

    print(answer.lower())

    if answer == "No":
        print("Thank you for using converter.")
        break
    elif answer == "no":
        print("Thank you for using converter.")
        break
    else:
        print("Great!")
