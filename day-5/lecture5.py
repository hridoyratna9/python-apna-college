#loop  :: used to repeat instructions
#while loop
#syntex= while condition : Some work

# while True:
#     print("Hello World!!")  #its a infinite loop

# count=1
# while count<=5:
#     print("Hello Hridoy!!")
#     count +=1
# print(count)


#Practice Question using while loop
#print number from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i +=1

# print("\n")
#print number from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i -=1

#print the multiplication table of a number n

# n=int(input("Enter a num : "))
# i=1
# while i<=10:
#     #mul=n*i
#     print(n,"*",i,"=",n*i)
#     i +=1

#keywords :: Break & Continue

# i=1
# while i<=10:
#     print(i)
#     if(i==4):
#         break
#     i +=1
# print("End of Loop")


# for loop :: used for sequential traversal
# syntex : for el in list 

# nums=[34,66,45,94,32,90]   #list
# for num in nums:
#     print(num)

# print(type(num))   #Depend on last index element. 
# print(type(nums))

# tup=(27.6,48.6,69.7,90.5,94.9,87.4,75.3,50.7,"hridoy",97)
# for val in tup:
#     print(val)
#     print(type(val))

# print(type(val))
# print(type(tup))

#for loop for string
# str="Hridoy Ratno"
# for char in str:
#     print(char)
# else:
#     print("End")

#Parctice Question
# list =[1,4,9,16,25,36,49,64,81,100]
# for square in list:
#     print(square)

# tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x=49
# # ind=0
# for value in tup:
#     if(value==x):
#         print("Number is found.")
#     else:
#         print("Number is not found.")

#range() is very very important. Returns a sequence of number. start value by default 0
# syntex : range(start?,stop,step?) #step means increament or decreament
# "?" means optional

# seq= range(5)   # starting value by  default 0 
# print(seq[0]) 
# print(seq[1]) 
# print(seq[2]) 
# print(seq[3]) 
# print(seq[4]) 
#  print(seq[5])  #print error


# using loop for this seq
# seq=range(10)  #10 is equal to stop condition
# for i in seq:
#     print(i)

#set starting value 
# seq=range(5,10)  #(start , end)
# for i in seq:
#     print(i)

# seq=range(2,10,2)  #(start , end,step)
# for i in seq:
#     print(i)

#practice Question 
# for i in range(1,101):
#     print(i)


# for i in range(100,0,-1):
#     print(i)

#multiplication Table
# n=int(input("Enter a num : "))
# for i in range(1,11):
#     print( n, "*", i,"=",n*i)

#pass Statement  :: null statement

# for i in range(5):
#     pass     #Skip

# print("Donot work range block")

  