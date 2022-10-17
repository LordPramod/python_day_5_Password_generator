# student_heights = input("Enter The list of studen heights").split()
# for i in range(0,len(student_heights)):
#     student_heights[i] = int(student_heights[i])
# total_height = 0
# for height in student_heights:
#     total_height += height
# no_of_student = 0
# for students in student_heights:
#     no_of_student += 1
# average_height = total_height / no_of_student
# print(f"{average_height} Is The Average Height")
# Fizz Buzz
# for n in range(1, 101):
#     if n % 3 ==0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 ==0:
#         print("Fizz")
#     elif n % 5 ==0:
#         print("Buzz")
#     else:
#         print(n)
print("Welcome ro the PyPassword Generator")
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U' ,'V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1', '2', '3', '4', '5', '6', '7', "8", "9", "0" ]
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', "+"]
no_of_letter = int(input("How many letter you want in your password?\n"))
no_of_numbers = int(input("How many number you want in your password?\n"))
no_of_symbols = int(input("How many symbol you want in your password?\n"))
password_list = []
for n in range(1, no_of_letter + 1):
    password_list += random.choice(letters)
for n in range(1, no_of_numbers + 1):
    password_list += random.choice(num)
for n in range(1, no_of_symbols + 1):
    password_list += random.choice(symbols)
random.shuffle(password_list)
password = ""
for char in password_list:
    password = password + char
print(f"Your Password is :{password}")
