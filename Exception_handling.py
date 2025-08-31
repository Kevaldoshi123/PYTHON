#Exception Handling:-

# NameError: name 'a' is not defined.
# print(a)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print( 12 + "hello")

#  ZeroDivisionError: division by zero
# print(12/0)

# ValueError: invalid literal for int() with base 10: 'sachin'
# num = int(input("Enter a number:- "))
# print(num)

# IndexError: list index out of range

# mylist = [2,4,6,8,10]
# print(mylist[10])

# try except block:

'''
try:
        a = 12
        print(a)
except NameError:
        print("Please define the variable first.")


print("Thank you")
print("Good night")

'''
'''
try:
        mylist = [10,20,30]
        print(mylist[0])
        print(a)
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))
        print( num1 / num2)
except(ZeroDivisionError,IndexError):
        print("denominator can not be zero")
except ValueError:
        print("Please enter integer value")
except:
        print("something is wrong")


print("Thank you")
'''

#finally block:

'''
try:
    a = 1
    print(a)
except NameError:
    print("Please define the variable first")
finally:
    print("Thank you")

'''
'''
#raise keyword >>

age = int(input("Enter you age:"))

if(age <= 15):
    raise ValueError("Age is below 15")
else:
    print("All is ok")
'''
















