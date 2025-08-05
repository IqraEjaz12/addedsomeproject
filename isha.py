#
# # print("welcm to the rollercoster")
# # height=int(input("please enter your height in cm"))
# # if height>=120:
# #     print("you can ride")
# #     age=int(input("please enter your age"))
# #     if age>=18:
# #         print("please pay $18")
# #     else:
# #         print("please pay $5")
# # else:
# #     print("you can not ride")
#
#
# # print("welcom to BMI calculator")
# # height=float(input("please enter your height in meters"))
# # weight=float(input("please enter your weight in kg"))
# # BMI=weight/(height**2)
# # print(BMI)
# # if BMI<18:
# #     print("you are under weight")
# # elif BMI<25:
# #     print("you are healthy")
# # elif BMI<30:
# #     print("you are over weight")
# # elif BMI<35:
# #     print("YOU ARE OBESE")
# # else:
# #     print("you are extremely obese")
#
#
# # year=int(input("please enter a year"))
# # if year%4==0:
# #     if year%100==0:
# #         if year%400==0:
# #             print("this is a leap year")
# #         else:
# #             print("this is not a leap year")
# #     else:
# #         print("this is a leap  year")
# #
# # else:
# #     print("this is not a leap year")
#
#
#
#
# # marks=int(input("please enter your marks"))
# #
# # if marks>=80:
# #     cs_marks=int(input("please enter your cs marks"))
# #     maths_marks=int(input("please enter your maths marks"))
# #     phy_marks=int(input("please enter your physics marks"))
# #     if cs_marks>=80:
# #         print("you can get admission in cs")
# #     if maths_marks>=80:
# #         print("you can get admission in maths")
# #     if phy_marks>=80:
# #         print("you  can get admission in physics")
# # else:
# #     print("you are not eligible for admission")
#
#
#
# #
# # print("welcom too python pizza deliveries")
# # size=input("which size do you want?S,M or L")
# # add_pepproni=input("do you want to add pepproni?Y or N")
# # add_cheese=input("do you want to add cheese?Y or N")
# # bill=0
# # if size=="S":
# #     bill=bill+20
# # elif size=="M":
# #     bill=bill+25
# # else:
# #     bill=bill+30
# # if add_pepproni=="Y":
# #     if size=="S":
# #         bill=bill+5
# #     else:
# #         bill=bill+3
# # if add_cheese=="Y":
# #     bill=bill+1
# # print(bill)
#
#
#
#
# # import random
# # random_num=random.randint(0,1)
# # if random_num==1:
# #     print("heads")
# # else:
# #     print("tails")
#
#
# import random
# students=["iqra","saira","esha"]
# random_num=random.randint(0,2)
# print(students[random_num])
# print(students[-1])
# print(len(students)-1)
# students.append("hijab")
# # students[1]="memoona"
# # print(students)
#
#
# # marks=[223,43,987,10]
# # total_marks=0
# # for marks in marks:
# #     total_marks=marks+total_marks
# # print(total_marks)
#
#
# # students_marks = [223, 43, 987, 10]
# # total_elements=0
# # for marks in students_marks:
# #     total_elements=total_elements+1
# # print(total_elements)
# #
# # a = [1,2,3,]
# # b = [5,6,7]
# # c = [8,9,0]
# # d = [a,b,c]
# # print(d[1][1])
#
# # position=input("where do you want to put the treasure")
# # column_no=int(position[0])
# # row_no=int(position[1])
# # d[row_no-1][column_no-1]="x"
# # print(f"{a}\n{b}\n{c}")
# #
# # row1 = ["⬜","⬜","⬜"]
# # row2 = ["⬜","⬜","⬜"]
# # row3 = ["⬜","⬜","⬜"]
# # map = [row1, row2, row3]
# # print(f"{row1}\n{row2}\n{row3}")
# # position = input("Where do you want to put the treasure")
# #
# # column_no = int(position[0])
# # row_no = int(position[1])
# #
# # map[row_no-1][column_no - 1] = 'x'
# # print(f"{row1}\n{row2}\n{row3}")
#
#
#
#
#
# # import random
# # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# #
# # print("Welcome to the PyPassword Generator!")
# # nr_letters= int(input("How many letters would you like in your password?\n"))
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like?\n"))
# # #easy level
# # password=""
# # for char in range(1, nr_letters + 1):
# #     password += random.choice(letters)
# #
# # for char in range(1, nr_symbols + 1):
# #     password += random.choice(symbols)
# #
# # for char in range(1, nr_numbers + 1):
# #     password += random.choice(numbers)
# # print(password)
#
#
#
# # import random
# #
# # rock = '''
# #     _______
# # ---'   ____)
# #       (_____)
# #       (_____)
# #       (____)
# # ---.__(___)
# # '''
# #
# # paper = '''
# #     _______
# # ---'   ____)____
# #           ______)
# #           _______)
# #          _______)
# # ---.__________)
# # '''
# #
# # scissors = '''
# #     _______
# # ---'   ____)____
# #           ______)
# #        __________)
# #       (_

# # game_images = [rock, paper, scissors]
# #
# # user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# # print(game_images[user_choice])
# #
# # computer_choice = random.randint(0, 2)
# # print("Computer chose:")
# # print(game_images[computer_choice])
# #
# # if user_choice >= 3 or user_choice < 0:
# #   print("You typed an invalid number, you lose!")
# # elif user_choice == 0 and computer_choice == 2:
# #   print("You win!")
# # elif computer_choice == 0 and user_choice == 2:
# #   print("You lose")
# # elif computer_choice > user_choice:
# #   print("You lose")
# # elif user_choice > computer_choice:
# #   print("You win!")
# # elif computer_choice == user_choice:
# #   print("It's a draw")
#
#
# #
# # def printfunction():
# #   a = 21
# #   print(f"hi hello {a}")
# #   if a> 20:
# #     print("this is greater than 20")
#
#
# # printfunction()
# #
# # printfunction()
# # printfunction()
# # printfunction()
#
#
#
# def addtwonum(a, b):
#   c = a + b
#   print(f"Sum is {c}")
#
#
def multiply(a, b,c, d):
  e = a * b * c * d
  print(e)
#
#

#
# def multiply(a,b,c,d):
#   e = a * b * c * d
#   return e
#
#
# result = multiply(10,20,30,40)
# print(result)

# def divided (a,b,c):
#   d= a/b/c
#   return d
#
#
# result=divided(10,20,30)
# print(result)



















