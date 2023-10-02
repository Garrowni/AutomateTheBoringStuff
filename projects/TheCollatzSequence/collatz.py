def collatz(number):
    #if number even --> print number // 2 and return value of number // 2
    if number % 2 == 0:
        number = number // 2

    #if odd --> print and return 3 * number + 1
    if number % 2 == 1:
        number = (number * 3) + 1

    print(number)



collatz(2)
