
'''
#constructor :-
                -> it is a special type of fucntion when object or instance is created this function called
                automatically

                class ClassName:
                       def  __init__(self):
                             .code

                    obj = ClassName()
'''

'''
class student:

    def __init__(self):    #default constructor
        self.name = input("Enter your name :")

    def display(self):
        print("name is : ",self.name)

obj = student()
obj.display()
'''

'''
    -> paramaterised constructor :-


               class ClassName:
                         def __init__(self,n):
                                  ...code

                        obj = className("abcd")

'''
'''
class student:
                def __init__(self,name):
                        self.name = name
                        
                def display(self):
                        print("name is: ",self.name)


obj = student("abcd")
obj.display()
'''


#destructor :-


class student:
    def __init__(self,name):
        self.name = name
        
    def display(self):
       print("Name is :",self.name)

    def __del__(self): #default destructor
        print("object was deleted !")


obj = student("abcd")
obj.display()


'''
del obj
'''













       






























