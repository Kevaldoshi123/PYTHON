#class:-

class sample:
    name = "dinchak" # class variable :- same for all object

    def display(self):  #class function
        print("This is display function of sample class")


obj = sample()
print(obj.name)
obj.display()

obj1 = sample()
obj.name = "abcd"
print(obj1.name)


#example:- 

class student:
    def set_name(self):
        self.name = input("Enter a value: ")

    def display(self):
        print("your name: ",self.name)

obj = student()
obj.set_name()
obj.display()


#Example


class receipt:
    def set_bill(self):
        self.amount = int(input("Enter your bill amount :-"))


    def set_discount(self):
        self.discount = int(input("Enter your amount :-"))

    def receipt_show(self):
        dis = self.amount * (self.discount / 100)
        total = self.amount - dis
        print("Your discount is: ",self.discount,"% & the value is : ",total)


person1 = receipt()
person1.set_bill()
person1.set_discount()
person1.receipt_show()
 



















    
