# #list :list is similier to array.But arrays we can store same type of data but list we can store diff types of data
# # student=["Hridoy",222111123,"Kotalipara"]
# # print(student[0])
# # print(student[1])
# # print(student[2])   #Strings are immutable (don't change)
# # print(student)      #lists are mutable (can change)

# # student[0]="Pollob"
# # student[1]=22111124
# # print(student)

# # #slicing : list_name[start_index: end_index]
# # marks=[98,90,45,65,67]
# # print(marks[:2])
# # print(marks[2:4])
# # print(marks[2:])
# # print(marks[-4:-2])
# # print(marks[3:len(marks)])

# #methods
# # list.append()   #adds one elements at the end
# # list.sort()      #sorts in ascending order [1,2,3]
# # list.sort(reverse=True) #sorts indecending order [3,2,1]
# # list.reverse()      #reverses list [3,1,2]
# # list.insert(index,el) #insert element at index

# list=[2,1,3]
# list.append(4)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# # list1=["banana","litchi","Apple","A"]
# # # list1.sort()
# # # print(list1)
# # list1.reverse()
# #  print(list1)


# #Tuples : That's are immutable (not change)
# #The most difference is bracket .. in Tuple,we use first bracket

# tup=(2,5,3,7,9,10)
# print(tup)
# print(tup[4])

# tup1=()         #Empty Tuple
# print(tup1)
# print(type(tup1))

# tup2=(1,)  #Using coma is a good habit of a programmer ..single element divide using a coma
# print(tup2)
# print(type(tup2))

# tup3=(1) #without coma ,the compiler behaves a integer value
# print(tup3)
# print(type(tup3))

# #Tuple Methods
# #tup.index(el)      #return index of the first occurrence
# #tup.count(el)      #counts total occurrences

# # tup4=(3,7,5,9,3,6,9,3,5,3,3)
# # print(tup4)
# # print(tup4.index(7))
# # print(tup4.count(3))

# # #Practice Question 

# # list=[input("First movie : "),input("Second movie : "),input("Third movie : ")]
# # print(list)
# # print(type(list))


# #Palindrome or not 
Palin=[input(),input(),input(),input(),input()]
palin1= Palin.copy()
palin2= palin1.reverse()
# if(Palin==palin2):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

print(Palin)
#print(palin1)
print(palin2)

