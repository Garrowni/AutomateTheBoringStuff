#################################
# create a function collatz()
# input parameter is number
# if number is even 
#       print number // 2
#       return number // 2
# if number is odd
#       print 3 * number + 1
#       return 3 * number + 1
##################################
def collatz(number):
    while(number != 1):
        #if even
        if number % 2 == 0:
            number = number // 2
            print(number)

        #if odd
        else:
            number = (number * 3) + 1
            print(number)


# User should input a number
try: 
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

collatz(number)
