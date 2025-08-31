#break: teminate loop
#continue
'''
for i in range(1,51):
    if( i == 5):
        break
    print(i)
#agar me print ko break ke uper daalu toh alag output aayega
'''
'''
for i in range(1,11):
    if(i == 5 or i == 8):
        continue
    print(i)
'''
#prime number or not:
# 1 or self:
# 5 = yes = 1 2 3 4 5 = 1 5 = 2
# 13 = yes = 1 2 3 4 5 6 7 8 9 10 11 12 13 = 1 13 = 2
# 6 = 1 2 3 4  5 6 = 1 2 3 6 = 4
'''
num = 10000
count = 0

for i in range(1,num + 1):  #+1 is liye kyu ki normally less than jata hai jaise(i<)
    if(num % i == 0):  # 5 % 5 == 0
        count = count + 1  #count = 2

print("count",count)

if( count == 2):
    print("the entered number is a prime number!")
else:
    print("The entered number is not a prime number!")
'''




'''
num = 10000
count = 0

for i in range(1,num + 1):  #+1 is liye kyu ki normally less than jata hai jaise(i<)
    if(num % i == 0):  # 5 % 5 == 0
        count = count + 1  #count = 2
    if(count > 2):
        break

print("count",count)

if( count == 2):
    print("the entered number is a prime number!")
else:
    print("The entered number is not a prime number!")
'''



























    
