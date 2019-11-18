# first start of python learning   -----------> literal comments
''' ---> Bulk comments
Author: Dharani Bolineni
Learning python code to learn.
'''

#hello world
print("hello")
print("helloworld")

# with ''
print('welcome to python world')

# with ,
print('java','python')
print("java","python")


#with break line charector
print("happy Learning \n\nWelcome python")

#variable
A=10                    # A and B are identifiers
B='Dhrani'
print(A,B)

#assign in order
x,y,z=10,20,30           # same as x=10 y=20 z=30
print(x)
print(y)
print(z)
# Note: variable are nothing but reserved memeory locatiaon to store value. this means that when you create a varaible you reserve some space in memory.
# memory allocation is happens during the running the program.

# data type: What kind of data is whether it is mutable or immutable
# In python there are 2 types of data types: mutable and immutable data type.
# immutable are Numbers, String, Tuples.(data can't be changed) example 121-->cann't change to 3
# mutable are List, Dictionaries, Sets.( data can be changed)

# Numerical --> int(signed Integers), Complex numbers, float(Real Number)
#           --> python represtns numbers in multiple ways
#           --> Binary, octal, Hexadecimal

P=10
Q=10.65
R=10+6j
S=5+4j

print(P,Q,R)
print(S-R)

# String : set of charactors represented in "" or ''
# python doesn't have char

#tuple is a fixed list that are separated by comma and enclosed by parenthesis.
# have obhjects of differnt datatypes unlike Array's in 'C'
# example
list=(5,6,7)
print("print tuple")
print(list)
# read individual element of the tuple using index
print("print individual element of the tuple using index")
print(list[0])
print(list[1])
print(list[2])
#print(list[3])   # error as tuple index out of range
#can not assign the already initialized

# example
# list[0]=10
# print(list[0])   typeerror: 'tuple object doesn't support item assignment

# mutable data types
# 1.List  : same as tuple
#-----------

X=[] # empty lsit
X=[1,2,3.15,'sample']
print(X)
print(X[1])

# but can be updated
X[1]='Change 2nd element'
print(X)

# example 2
Y =[[10,20,40],44,'third element',(2,4,5)]
print(Y[0][1])

# note: tuples are faster then list
# tuples are used for constants eg pi list of countries.
# list id enclosed in [] and tuples are enclosed in ()

#2: Dictionaries: it's readable with key value pairs Ver={'key1':value1,'key2:value2.....}
#type1
G={'Age':24,'Name':'Johon'}
print(G['Age'])
#type2
G=[24,'John']
print(G[0])

# type1 is more readable then type2
#note: dictionaries are with in dictionaries and can have arrays in the dictionaries
K={'Age':24,'Name':'Johon','jobs':[],'cities':{},'t':True,'v':False}
print(K)

# Set is unordered collection of items. Every element is unique. A set is created by placing all the items(elements) dinside curly bracess{}, separated by comma.
# set has to be unique
# even set is assigned with duplicates that will not print or assign to the set variable.

 # S = {1, 2, 3,1}
 # print(S)

#**********************************************************************************************************************************************************
#                                                                    Python Operators
#***********************************************************************************************************************************************************
''' 
1. Arithmetic :addition(+), subractor(-), multiplication(*), division(/), modulus(%), Exponent(a**b),Floor Division(a//b)
2. Assignment:(shorthand notation) +=,-+,*=,/=,**=,//=
3. Comparison:(==,!=,>,<,>=,<=) give result has True or False 
4. Logical (and, or,not) and gives lower value, or give me greater value, not a gives False
        a and b --> compare and convert it into binary and print the output.( which is binaray logic)
5. Bitwise   --> AND(a&b),OR (a|b),XOR (a^b),NOT (a~b),LeftShift (a<<),RightShift(a>>)
6. Identity  --> is,is not --> returns True or False
7. Membership  --> in means variable present within the set of sequence (returns True) otherwise it returns False (used in list , dictionaries, tuple )
                   not in  means variable not present within the set of sequence (returns True) otherwise it returns False (used in list , dictionaries,tuple )
'''
a,b=2,3
a+=b
print(a)

#prints results in True or False (this are keywords not strings)
print(a==b)
print(a!=b)
print(a>b)


# logical operator
ab,pq=2,3
print(ab and pq)  # output is 3
print(ab or pq)  # output is 2
print(not ab)
print(not 0)
print(not 1)
print(ab or False)   # output is 2
print(ab or True)    # output is 2

# Identity operator
c=5
d=4
print(5 is not 4)
print(c is d)


today='wednesday'
yoga_day='Wednesday'
print(today is yoga_day)    # VERBOSE means easy to read like english

# membership operator
Ab=[1,2,3,4,15,'learn!']
print('learn!' in Ab)    # in means check the member of
print('learn!' not in Ab) # not in means checks not member of

# membership with dictionaries
Pk={'Age':24,'Name':'john','jobs':[],'cities':{}}
print('age' in Pk)
print('Age' in Pk)
#print(Pk['age'])

#*******************************************************************************************************************************************************
#                                                                     Conditional Statement
#********************************************************************************************************************************************************
'''
   if --> same as if condition
   Elif  --> same as else if condition
   Else
no {} is used it used indentation  for set of code inside the block
'''
#if - elif - else
X1=12
Y1=12
if(X1<Y1):
    print("X1 is less then Y1")
    print("ON line 183")
elif(X1>Y1):
    print("X1 is greater then Y!")
    print("ON line 186")
else:
    print("X1 is equals to Y1")

# if- else
A1=30
if(A1<10):
    print("Less than 10")
if(10<=A1<=25): # between
    print("In between 10 and 25")
else:
    print("Greater than 25")

# nested if condition
B1=30
if(B1<100):   #Parent
    print("nested:Less than 100")
    if(100<=B1<=250): # between
        print("nested:In between 10 and 25")
    else:
        print("nested:Greater than 25")


#*******************************************************************************************************************************************************
#                                 Loop statement : to execute a statement for n number of times.
#********************************************************************************************************************************************************
'''
while loop 
For loop
Nested loop

'''

#while performs until the expresion is false
#while expression:
#    statements
#example
count=0;
while(count<=5):
    print(count)
    count+=1

print("Good bye")

#example
rank=5
while(rank!=12):
    print("Rank is", rank)
    rank+=1

# for loop it iterates over a range
# range is list, tuple (collection)
fruits=['Banana','Apple','Grapes']
for fruit in fruits:
    print(fruit)

list1=[1,2,3,'python']
for l1 in list1:
    print(l1)

#Factorial of a number in python
#Factorial=n(n-1)(n-2)....1
fact=1
num=7
if num<0:
    print("factorial doesn't exits for negitive numbers")
elif num==0:
    print("The factorial f 0 is 1")
else:
    for i in range(1, num + 1):
        fact=fact*i
    print("The factorial of ",num," is ",fact)


#Nested Loop
#example1:
count=1
for i in range(10):
    print(str(i)*i)
    for j in range(0,i):
        count=count+1

#example2:
day='Thursday'
while day=='Thursday':
    for i in[1,2,3,4]:
        print('walk')
    day = 'wednessday'


#**********************************************************************************************************************************************
#                                               Loop Control Statement
#**********************************************************************************************************************************************
'''
break statement: Terminate from the loop and transfer execution to the statement immediately following the loop
contiue statement: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating. 
pass statement: is required syntactically but you do not want any command or code to execute
'''
#pass: skip execution of that itration and go to next itration
for name in ['apple','baby','child','Doll']:
    # ... Use pass to ignore contents of block.
    if name =="baby":
        pass
    else:
        print(name)
#continue: skip execution of that itration and go to next itration
for i in range(1,10):#['A','B','C','D','E']:
    if(i==5):
        continue
    print(i)
#break: break the loop all together.
















