#Dictionary & Set
#Di8ctionary Syntex : Key:value
# info={
#     "Key" : "Value",
#     "name":"Hridoy",
#     "Lerning " : "Python",
#     "Cgpa":4.00,
#     "Age": 24,
#     "Adult": True,
#     "marks": 98,
#     "list":["Alu","Tomato","Chatni"],   #Creating list
#     "tuple":("Khuchuri","Salad","bresta")  #Creating Tuple

# }
# print(info["name"])
# info["name"]="Choity"    #Assign new value (Couse mutable)
# info["surname"]="Bosu"   #insert new key:value 
# print(info)
# print(type(info))
# print(info["tuple"])
# print(info["list"])


# #Create empty Dictionary
# null_dic={}
# print(null_dic)
# print(type(null_dic))

# #adding value in null_Dic
# null_dic["Name"]="Puja"
# null_dic["surname"]="Bosu"
# null_dic["education"]="BA 2nd year"
# null_dic["subject"]="english"
# null_dic["college"]="GBC"
# null_dic["home"]="jashore"


# print(null_dic)

#nested dictionary
# student={
#     "name" : "Hridoy Ratno",
#     "sub":{
#         "math":3.75,
#         "C++":3.25,
#         "BEE":3.25,
#         "DiscriteM":3.50,
#         "English":3.00
#     },
#     "Versity":"BSFMSTU"

# }
# print(student)
# print(student["sub"])
# print(student["sub"]["C++"])

# #Methods
# print(len(student))    #Count total number keys 
# print(student.keys())   #count outer keys
# print(list(student.keys()))   #Type cousting : Converted into list
# print(len(list(student.keys())))
# print(student.values())     #return all outer values
# print(list(student.values()))
# print(student.items())   # Return pairs(key:value) that is looked as tuple
# print(list(student.items()))  #type Cousting : tuple to list
# pairs=list(student.items())
# print(pairs[0])    #Print indivisual pairs
# print(student.get("sub"))  
# print(list(student.get("sub")))  
# student.update({"dist":"Jamalpur"})   #Two types of rule declaring update method
# print(student)  
# new_dict={"loca":"Melendha","address":"Gobindhogonj","name" : "Puja"}   #name override not dublicate  
# student.update(new_dict)
# print(student)


#Set nutable but the element of sets are immutable
#Set  :: Each element must be unique and immutable (unordered items)

# collection={2,6,5,7,3,"Puja","world","world",5}   #ignore dublicate value but order don't follow 
# print(collection)
# print(type(collection))
# print(len(collection))    #length also ignore dublicate value


# #empty set
# collection1=set()     
# collection2={}    #empty dictionary
# print(collection1)
# print(type(collection1))
# print(collection2)
# print(type(collection2))


# #Methods
# #set.add(el)   :: add an element
# collection1.add(4)
# collection1.add(7)
# collection1.add(3)
# collection1.add(9)
# print(collection1)    #WE can input string,tuple,int,float.But not list
# collection1.remove(3)
# print(collection1)
# # collection1.clear()
# # print(collection1)
# collection1.pop()    #remove random value.
# print(collection1)

#another methods
#set.union(set2)     #combines both set values & return new
#set.intersection (set2)   #combines common values & return new

# set1={1,2,3}
# set2={2,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1)
# print(set2)

#practice Qestion

dic={
    "table":("a piece of furniture","list of facts & figures "),  #store as a list or tuple
    "act":"a small animal"
}
print(dic)


#Very Very important
value={9,9.0}
print(value)
value1={9,"9.0"}
print(value1)
value2={"9",9.0}
print(value2)

#another Solution
value3={
    ("float",9.0),
    ("int",9)
}
print(value3)