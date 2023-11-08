##########################################################
# Comma Code
# create a function 
# take list value as an argument
# return a string 
# the string should be separated by comma and space AND 
# inserted before the last item.
#
# Example:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# this should return 'apples, bananas, tofu, and cats'
##########################################################
spam = ["cat", "dog"]

#take in a list
# return a string with all of the list items seperated by commas, put and before the last word"
def addAnd(theList):
    try:
        count = 0
        while count < len(theList) - 1:
            print(theList[count] + ",")
            count += 1

        if (len(theList) != 1):
            print("and " + theList[-1])
        else:
            print(theList[-1])
    except IndexError:
        print("Something went wrong. Check that your list is correct.")

addAnd(spam)