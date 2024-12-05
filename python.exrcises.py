# age = 21
# name = "yonatan"
# print("Age:",age)
# print("Name:", name)

# age = int(input("please enter your age:"))
# age=18
# if age >=18:
#    print ("you are old enogh to drive")
# elif age >=16:
#    print("already there")
# else:
#    print("you are not old enough")      


# number = int(input("please enter your number"))
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# score = int(input("enter your score between 1-100"))
# if 90 <= score <=100:
#     print ("A")
# elif 80 <= score <= 89:
#     print("B")
# elif 70 <= score <= 79:
#     print("C") 
# elif 60 <= score <= 69:
#     print("D") 
# elif score < 60:
#     print("Grade: F")
# else:
#     print("Invalid score entered. Please enter a score between 0 and 100.")


# number=float(input("please enter your number:"))
# if number > 0:
#     print ("positive")
# if number < 0:
#     print ("negative")
# if number == 0:
#     print ("number equals o")        


# age=int(input("please enter your age:"))
# student=input("are you a student? yes/no")
# if age <= 18 or student == "yes": 
#     print("you have a discount")
# else: 
#     age >= 18 or student =="no"
#     print("you have to pay full price")


# for num in range(1,11):
#     print(num)
# for num in range(1,11):
#     if num % 2 == 0:
#         print(num)

# i=0
# for num in range(1,101):
#   i+=num
# print("The sum of numbers from 1 to 100 is:",i)
  

# num=int(input("enter number for multiplication table"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")
    

# colors=["red","green","blue","yellow"]
# for color in colors:
#     print(color)

# num =1
# while num <= 10:
#     print(num)
#     num += 1

import random

# random_number = random.randint(1, 10)

# print("I'm thinking of a number between 1 and 10. Try to guess it!")

# while True:
   
#     guess = int(input("Enter your guess: "))
    
#     if guess < random_number:
#         print("Too low! Try again.")
#     elif guess > random_number:
#         print("Too high! Try again.")
#     else:
#         print(f"Congratulations! You guessed the number {random_number} correctly!")
#         break  
# i=0
# while True:
#    number=int(input("please enter number"))
#    if number < 0:
#       break
#    else:
#     i += number
# print("The sum of all positive numbers entered is:", i)

# def greet():
#      print("hello world")

# greet()     

# def greet(name):
#  print(f"Hello, {name}!")

# greet("yarin")


# def squere(number):
#     return number ** 2
# result = squere(5) 
# print("The square of 5 is:", result)

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result   
# print(factorial(n))

# def calculator(a,b,operator):
#     if operator == 'add':
#         return a + b
#     elif operator == 'subtract':
#         return a - b
#     elif operator == 'multiply':
#         return a * b
#     elif operator == 'divide':
#         if b != 0:
#             return a / b
#         else:
#             return "cannot devide by zero"
#     else:
#         return "invalid operator"  

# print(calculator(10, 5, 'add'))     
# print(calculator(10, 5, 'subtract'))
# print(calculator(10, 5, 'multiply'))  
# print(calculator(10, 5, 'divide'))    
# print(calculator(10, 0, 'divide'))    
   
                  
# x = 10
# y = 5

# sum_result = x + y

# print("Sum:", sum_result)               
# print("Subtraction (x - y):", x - y)    
# print("Multiplication (x * y):", x * y) 
# print("Division (x / y):", x / y)       

# num1=[1,2,3]
# num2=[4,5,6]
# num3=(num1+num2)
# print(num3)
# for x in num2:
#   num1.append(x)
# print(num1)  
# num1.extend(num2)
# print(num1)
    

# import datetime
# with open("journal.txt", "a") as file:
#     print("Welcome to your journal! Type 'exit' to quit.")
#     while True:
#         entry = input("Enter your journal entry: ")
#         if entry == "exit":
#             print("Exiting journal. Your entries have been saved.")
#             break
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         log_entry = f"[{current_time}] {entry}\n"
        
#         file.write(log_entry)
        
#         print("Entry logged successfully.")

# percentage=input("what percent are you? chose what you are between this options:fat,stupid,russian")
# class sukinsak:
#     def __init__(self, fat, russian, stupid="default"):  
#         self.fat = fat
#         self.russian = russian
#         self.stupid = stupid

#     def what_percent(self):
#         print(f"youre 100% because you {self.fat}, {self.russian}, {self.stupid}.")

#     def not_100_percent(self, part="fat"):
#         if part == "fat":
#             print(f"youre 66% because you {self.fat}, {self.russian}.")
#         elif part == "russian":
#             print(f"youre 66% because you {self.fat}, {self.stupid}.")
#         elif part == "stupid":
#             print(f"youre 66% because you {self.stupid}, {self.russian}.")
#         else:
#             print("Invalid part selected.")

# saki1 = sukinsak("fat", "russian", "stupid")
# saki2 = sukinsak("fat", "russian") 
# saki3 = sukinsak("fat", "stupid") 

# saki1.what_percent()      
# saki2.not_100_percent()  
# saki3.not_100_percent()  


# x="yes"
# y="no"
# i=float(33.33)
# percentage_fat=input(f"are you fat: {x}/{y} :")
# percentage_stupid=input(f"are you stupid: {x}/{y} :")
# percentage_ussr=input(f"are you frum ussr: {x}/{y} :")
# if percentage_fat==x and percentage_stupid==x and percentage_ussr==x:
#     print("you are 100%")
# else:
#     if (y) in percentage_fat:
#        print("you are 0%")
#     else: 
#        (x) in percentage_fat
#        print(f"you are {i}") 
#     if (x) in percentage_stupid and percentage_fat==x:
#        print(f"you are {i+i}")   
#     elif (x) in percentage_stupid :
#      print(f"you are {i}")
#     else:
#        print("you are 0%")          
#     if (x) in percentage_ussr and percentage_fat==x:                   
#        print(f"you are {i+i}") 
#     elif (x) in percentage_ussr and percentage_stupid==x:
#        print(f"you are {i+i}")
#     elif (x) in percentage_ussr:
#      print(f"you are {i}")  
#     else:
#        print("you are 0%")      

# #calculator checks if youre 100%
# x = "yes"
# y = "no"
# i = float(33.33)

# # Input from the user
# percentage_fat = input(f"Are you fat: {x}/{y} : ")
# percentage_stupid = input(f"Are you stupid: {x}/{y} : ")
# percentage_ussr = input(f"Are you from USSR: {x}/{y} : ")

# # Initialize the total percentage variable
# total_percentage = 0

# # Check if the user is "fat"
# if percentage_fat == x:
#     total_percentage += i

# # Check if the user is "stupid"
# if percentage_stupid == x:
#     total_percentage += i

# # Check if the user is from the "USSR"
# if percentage_ussr == x:
#     total_percentage += i

# # Print the final accumulated percentage
# print(f"You are {total_percentage + 0.01}%")


