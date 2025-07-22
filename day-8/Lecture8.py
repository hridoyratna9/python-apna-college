# class Student:
#     name = "Hridoy"

# s1 = Student()
# print(s1.name)


# s2 = Student()
# print(s2.name)


# class Car():
#     model = "BMW"
#     color = "White"

# car = Car()
# print(car.model)   
# print(car.color)   


#Constructor
# class Student:
#     name = "Hridoy"
#     def __init__(self):
#         print(self)
#         print("Adding new student in Database..")

# s1 = Student()
# print(s1.name)


# s2 = Student()
# print(s2.name)


# class Student:
#     def __init__(self,fullname):
#         self.name = fullname
#         print("Adding new student in Database..")

# s1 = Student( "Hridoy")
# print(s1.name)
# s2 = Student( "Arjun")
# print(s2.name)



# class Student:
#     college_name = "Govt.BC"
#     name = "Anonymous"  #class attr
#     def __init__(self,fullname):
#         self.name = fullname #obj attr > class attr
#         print("Adding new student in Database..")

# s1 = Student( "Hridoy")
# print(s1.name)

#Practice Question
# class Student:
#     def __init__(self,name,mark1,mark2,mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
    
#     def average(self):
#         return (s1.mark1 + s1.mark2 + s1.mark3)/3


# s1 = Student("Hridoy",76,68,69)
# print(s1.name,"\nThe average mark of 3 subjects : ", s1.average())




#Practice Question : Solve
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def average(self):
#         sum =0
#         for val in self.marks:
#             sum += val
#         #return sum / 3
#         print(self.name,"\nThe average mark of 3 subjects : ", sum/3)


# s1 = Student("Hridoy",[76,68,69])
# s1.average()



#Static Methods
# class Student:
#     @staticmethod   #Without decorator thiss method given an error
#     def hello():
#         print("Hello Hridoy Ratno..")

# s1 = Student()
# s1.hello()



#Practice Question
class Account:
    def __init__(self,bal,acc):
        self.account_no = acc
        self.balance = bal
    
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("BD. ",amount,"was debited")
        print("Total balance = ", self.get_balance())
    #credit method
    def credit(self,amount):
        self.balance += amount
        print("BD. ",amount,"was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(17543654,22111123)
acc1.debit(2354)
acc1.credit(554)