#data structure : tuple  list  set  dictionary

#tuple:


'''
1)   ()
2) different type of data is allowed.
3) order is maintained
4) indexing is allowed
5) duplaicates are also allowed
6) not changable or immutable
'''

# tuple is type of array
'''
tup1 = (2,4,5,6,7,3.3,"keval",True,2,2)

print(tup1)
print(type(tup1))
'''


#index no of 5 = 0
#index no of 10 = 1
'''
tup2 = (5,10,15,20)

print(  tup2[2] )


#positive : 0 to n-1 : left to right
# negative : -1 : right to left

print(tup2[-1])
'''

#slicing:
'''
tup3 = (7,12,21,28,35,42,49)

print( tup3[1:4] )  #start : stop apne ko ek value baad la dena padta, because of indexing

print( tup3[:4])   #0 to 3    indexing

print( tup3[1:])   # 1 to end of array

print( tup3[:])    #if no start and no end toh pura array display kar dega
'''


'''
#it will show error as array cannot be changed ek constant value hogi
tup4 = (5,10,15,20)
tup4[0] = 90
print(tup4)
'''

#brackets are optional in tuple  >>
'''
tup5 = 2,4,6,8,10

print(tup5)
print(type(tup5))
'''


'''
# tuple with single elements:
#agar , nhi diya toh int identify karega
tup6 = (2,)

print(type(tup6))
'''

'''
# loop with tupel:

tup7 = (2,3,6,8,10)

for i in tup7:  # tup he range bun gayi
    print(i)
'''




#List

'''
list:-
  -> it is also a collection of multiple different type of values
         -> list_name = [value,value,value.....]
    place value(index)   ->  0, 1, 2, .....


-> empty:-
     -> list_name = []   | list()

     ->indexing allowed
     -> duplicate allowed
     -> changable
     -> ordered values

     -> access single value :-
         list_name[index]   <- it return the place value

'''

'''
list1 = ["apple", 56, True,56.8,56+8j]
print("list: ", list1)
print("list type is:- ", type(list1))
'''

'''
#single value:-
print("2nd  value:- ", list1[1])
'''

'''
#duplication & ordered:-
list2 = ["apple", "mango", "apple"]
print("duplication:- ", list2)
'''



'''
#change list values:-
list3 = ["apple", "mango", "kiwi", "Santra"]
print("before changing: -", list3)

list3[1] = "watermalon"
print("after changing:- ", list3)
'''


'''
#empty:-
list4= []
print("empty list is:- ", list4)

#empty list function:-
list5 = list()
print("empty list function is:- ", list5)


print()


#len()   # length is no. of elements not counted by index
print("length:- ", len(list3))
'''

'''
#display all values using for loop:- method 1
list6 = ["mango", "apple", "kiwi", "santra", 56, 4, 5 ,67 ,98.4]

for i in range(len(list6)):
    print(list6[i])

print()

#method 2 :- direct access
for i in list6:
    print(i)
 '''

'''
#pre-define function
# append()   it add the entered element in last 

list7 = [1,2,3,4,5]
list7.append(6)
print(list7)
'''
'''
#insert(index, value)   #pura index place he shift kar dega
list7.insert(2,"apple")
print(list7)
'''

''' 
#extends(list):-   ye pura ka pura set last ,me daal dega
list8 = [7,8,9]
list7.extend(list8)
print(list7)
'''
'''
#pop()
list7.pop()   # it removes last value from list
print(list7)
'''
'''
print()

list7.pop(0)  # it can also remove element by index
print(list7)
'''
'''
#del list[index]
del list7[0]    #abhi 0 postion pe 2 hai and vo nikal jayega
print(list7)
'''
'''
#clear()    in short delete 
list7.clear()
print(list7)
'''
'''
#del keyword
del list7
'''




'''
-> set:-
     -> it is also a collection of mutiple different type of values!

     -> syntax:-  set = {value,value,...}
       ->  unordered
       -> indexing
       -> duplication is not allowed
       -> changeble

-> empth :-
          set-name = {value}  |  set()
'''

'''
# unordered
set1 = {"apple",456,True,546.8,56+7j}
print("set :", set1)
'''
'''
#duplication
set2 = {"apple","kiwi","mango","apple"}
print("duplication :",set2)
'''

#indexing not allow:-
#print("indexing : ",set2[0])
'''
#type:-
set3 = {"apple","kiwi","mango","apple"}
print("type : ",type(set3))
'''
'''
#empty:-
set4 = {1}
print("type :",type(set4))

set5 = set()
print("type :", type(set5))
'''

#display all values by for loop


'''
set6 = {"apple","kiwi","mango","pine-apple",67,4,7,8,True}
for i in set6:
    print(i)
'''

'''
# set_namae.add(value):-

set4.add("mazza")
print("add :",set4)
'''

'''
#set_name.update({}) :- method 1
set4.update(set3)
print("update :",set4)
'''

'''
#set_name.update : method 2
set5.update({"kiwi",56,8,5,57,65+5j})
print("update : ",set5)
'''
'''
#set_name(value):-
set5.remove("kiwi")
print("remove :", set5)
'''

'''
# set_name.discard(value):-
set5.discard(65.5j)
print("discard: ",set5)
'''
'''
#pop():- it removes random values
set.pop()
print("pop:",set5)
'''
'''
#clear():-
set5.clear()
print("clear :",set5)
'''
'''
#del keyword :- it deleted whole set
del set5
'''
'''
#idsubset() & issuperset()

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7,8}
print(set1.issubset(set2))
print(set1.issuperset(set2))
'''

'''
#difference:-

set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8}
print(set3.difference(set4))

#symmetric_difference:-  #jo common hai vo nikal ke baki ki values ko print karna
print(set3.symmetric_difference(set4))

#intersection  : jo common hai vohi print karna
print(set3.intersection(set4))

#union  : saab values print karna and repeat vale ko ek he bar karna
print(set3.union(set4))
'''


#dictionary : key value pair
'''
1)  {} done
2) data is stored in key value pair.
3) different type of data is allowed
4) order is maintained
5) indexing is also allowed but on key basis
6) duplicates value are not allowed but not key
7) changeble or mutable.

'''

'''
student1 = {"name":"rohit","age":37,"runs":264}

print(student1)
print(type()student1)

print(student1["name"])
print(student1["age"])
print(student1["runs"])
'''

'''
student2 = {"name":"virat","age":20,"age":35,"rollno:":20}
print(student2)
'''

'''
student3 = {"name":"virat", "age":20, "rollno":7}

student3["rollno"] = 10

print(student3)

student3["mobno"] = 98123

print(student3)
'''

#keys()   values()  items()

'''
student4 = {"name":"virat", "rollno": 18}
print( student4.keys())
print( student4.values())
print( student4.items())
'''


#  for loop woth dictionary:

'''
student4 = {"name":"virat", "rollno": 18}

for i in student4.values():
        print(i)
'''

'''
for k,v in student4.items():
        print(k,"=",v)
'''

#key = must be immutable or not changable = tuple,string,number
#value = anything.

'''
students = { 1:"ross", 2:"joey", 3:["hello","hi"] }
print(students)
'''

#take input form user

'''
mydict = {}

for i in range(3)
        key = input("Enter key: ")
        mydict[key] = input("Enter a value: ")

print(mydict)
'''

#remove()
'''
student = {"name":"rohit","age":20}

for i in range(3):
        key = input("Enter key:")
        mydict[key] = input("Enter a value:")

print(mydict)

'''

#del

'''
student = {"name":"rohit" , "age":20}
del student["name"]
del student["age"]
print(student)
'''

















