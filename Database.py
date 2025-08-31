import mysql.connector as mysql

conn = mysql.connect(
    user="root",
    host="localhost",
    password="",
   database="keval" # data base selection
    )

if(not conn):
    print("Not connected")
else:
    print(conn)

que = conn.cursor()


#database create :-
'''
que.execute("create database keval")
'''

# show all database:-
'''
que.execute("show database")
for i in que:
    print(i)
'''
# create table :-
'''
que.execute("create table student(id int,name varchar(56),fees float)")
'''

# show tables

'''
que.execute("show tables")
for i in que:
    print(i)
'''

# insert data into table :-
'''
que.execute("insert into student values(1,'admin',345.7)")
conn.commit()
'''

#select all data from tables
'''
que.execute("select * from student")
for i in que:
    print(i)
'''























