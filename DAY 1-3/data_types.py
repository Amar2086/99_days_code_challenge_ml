x=10
y=20 #integer
print(x,y)
decimal=23.34 #float
print(decimal)
complex_number=4+5j #complex Number
print(complex_number)
sky=True
print(sky)
cpc_event='99 days code challenge' #string
print(cpc_event)
#access the string elements
print(cpc_event[2])
print(cpc_event[-2])
print(cpc_event[1])
#let's create a multiline string
print("print a multiline string")
cpc_event='''\n99 
days
code
challenge'''
print(cpc_event)
# now its time for list
list=['Dhaka International University']
print("list value with string ")
print(list)
list=["omar","nafis","tamzid"]
print("list with multiple value")
print(list[0])
print(list[1])
print(list[-1])
#modify the list value 
list[2]="jihad"
print(list[2])
#its time for tuple 
tuple1=('Hello','world')
print(tuple1)
print(tuple1[1])
list1=[1,2,3,4,5]
print(tuple(list1))
tuple1=tuple('hello')
print(tuple1)
tuple2=(1,2,3)
print(tuple2 +tuple1)
tuple3=(tuple2,tuple1)
print(tuple3)
# print(tuple3[2]) does not work
tuple4=([1,2,3,4,5,6])
print(tuple4[2])# this time it works
#set data type in python
set1=set("dhaka international University")
#set data types with string
print(set1)
set1=set(["omar","jihad","zakaria"])
print(set1)
# print(set1[1]) :it also does not work in this way
