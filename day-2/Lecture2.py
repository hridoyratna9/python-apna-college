# # #Concatenation
# # # Slicing index in  python
# # # Syntex str[Start_index : End_index ] End_index don't not count
# # str1="Hridoy Ratno"
# # str2=" is a good student"
# # final_str=str1+str2
# # print(final_str)
# # print(len(final_str))
# # print(final_str[2:8])
# # print(final_str[2:len(final_str)])
# # print(final_str[2:]) #[2:last_index]
# # print(final_str[:6]) #[0:6]

# # # Slicing of negative index
# # str3="Apple"
# # print(str3[-5:-2])


# # #String Functions
# # #str.endswith("The last value of str") reeturns true if strings ends with sunstr.abs
# # str4="i am studying Python from apnacollege"
# # print(str4.endswith("ege"))  #return True
# # print(str4.endswith("ega"))   #return False

# # #str.capitalize() ,return Capital value of the first index
# # print(str4.capitalize())
# # print(str4) #when we print 2nd time its not work.but we motify oid str into new str then change the value of str4
# # str4=str4.capitalize()
# # print(str4)

# # #str.replace("value","replaced value")
# # print(str4.replace("o","am"))
# # print(str4.replace("am","was"))

# # #str.find(finding value)
# # print(str4.find("o")) #return first index
# # print(str4.find("from")) 

# # #str.count("value")
# # print(str4.count("from"))
# # print(str4.count("o"))

# #practice 1
# myName=input("Enter your name : ")
# print(len(myName))


#Conditionals Statement(Syntex:if-elif-else)

# light="Green"
# if(light=="red"):
#     print("Stop")
#     print("Don't stop ,you will punish")
# elif(light=="yello"):
#     print("Look /wait")
# elif(light=="Green"):
#     print("Now you can go.")
# else:
#     print("The light does not work.")

# print("This line always run and print. ")

#Student grede 
# marks=int(input("Enter your marks : "))
# if(marks>=90 and marks<=100):
#     print("A")
# elif(marks>=80 and marks<90):
#      print("B")
# elif(marks>=70 and marks<80):
#     print("C")
# elif(marks>=60 and marks<70):
#     print("D")
# elif(marks>=0 and marks<60):
#     print("Fail")
# elif(marks>=-100 and marks<0):
#     print("Fail")
# else:
#      print("The marks is not valid.")

#Practice Question
#even or odd number
# num=int(input("Enter any number : "))

# if(num%2==0 and num!=0):
#     print("Even")
# elif(num%2==1):
#     print("Odd")
# else:
#  print("The number is 0.")


#greatest number find
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))

if(num1>num2 and num1>num3):
    print("The greatest number is : ",num1)
elif(num2>num3):
    print("The greatest number is : ",num2)
else:
    print("The greatest number is : ",num3)
# else:
#     print("All number are equal.That is ",num1)
