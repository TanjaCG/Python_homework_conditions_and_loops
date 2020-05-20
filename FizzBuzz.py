print("Select a number between 1 and 100: ")
num = int(input(""))

for num in range(num, 100):
    if num % 15 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("buzz")
        continue
    else:
        print(num)
