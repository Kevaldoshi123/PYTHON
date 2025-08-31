#Function: what is function ? = group of statements

#(1) default = empty()
#(2) prameterised =
#(3)return
#(4)recursive
#(5)anonymous or lamba

#def = define


#default fuction

'''
def sample():
    print("hello")
    print("hello")
    print("hello")
    print("hello")

sample()        
'''

'''
def add():
    num1 = int(input("Enter first number:- "))
    num2 = int(input("Enter second number:-"))
    print(num1 + num2)

add()
''' 

#parameterised
'''
def multi(a,b):      
    print(a * b)

multi(5,90)
'''

'''
def greater(num1,num2):
    if(num1 > num2):
        print("num1 is greater ")
    else:
        print("num2 is greater")

greater(10,2)
'''
#function with default arguments

'''
def show(a,b=0,c=0): #if we define a value of  'b'  then any variable declare should also we define
    print("value of a = ",a)
    print("value of b = ",b)
    print("value of c = ",c)
    
show(5,12)
'''

# return :
'''
def add(a,b):
    result = a + b
    return result

ans = add(5,90)
print(ans * 2)

and2 = add(3,20)
print(and2 * 5)
'''


#
'''
def greater(num1,num2):
    if(num1 > num2):
        return num1
    else:
        return num2

ans = greater(12,13)
print(ans)
'''

#



#hello and hi he print hoga kyu ki return ke baad jo bhi likha hai vo aage hoga he nhi

'''
def display():
    print("Hello")
    print("hi")
    return 7
    print("Thank you")

display()
'''

'''
#self calling fucntion
def show():
    print("I am show function")

def display():
    show()

display()
'''


#recursive : self calling fucntion
#num = 10
'''
def display():
    display()

display()

'''


'''
def summation(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    return sum

ans = summation(10)
print(ans)
'''


def summation(num):     #num = 1
    if(num == 1):
        return 1
    else:
        return num + summation(num - 1)
    # 10 + 9 + ..... + 1


ans  = summation(31)
print(ans)



'''
def factorial(num):
    if(num == 1):
        return 1
    else:
        return num * factorial(num - 1)


ans = factorial(5)
print(ans)
'''


















