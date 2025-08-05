# #day.1
# #simple.1
# #print("Welcome to python programming!\nThis is your first step to becoming a developer.")
#
# #simple.2
# # user_name=input("please enter the user name")
# # fav_colour=input("please enter your favourite colour")
# # print(user_name+" likes "+fav_colour)
#
# #difficult.1
# # print("Hello, what is your name?")
# # name = input("please enter your name")
# # print("Hi " + name)
#
# #difficult.2
# # import random
# # print("welcom to  brand name enhancer")
# # fav_colour=input("please enter your favourite colour")
# # fav_place=input("please enter your favourite place")
# # brand_name=fav_colour+" "+fav_place
# # random_integer=random.randint(1,1000)
# # capitalized_string=brand_name.capitalize()
# # enhanced_brand_name=capitalized_string+str(random_integer)
# # print(enhanced_brand_name)
#
# # day 2
# # simple.1
# # input1=input("please enter the first input")
# # input2=input("please enter the second input")
# # print(type(input1))
# # print(type(input2))
#
# #simple.2
# #BMI calculator
# # weight = float(input("Please enter your weight in kg "))
# # height = float(input("please enter your height in meter "))
# # bmi = weight /  (height ** 2)
# # bmi = int(bmi)
# # print(f"your BMI is {bmi}")
#
# #difficult.1
# # Tip calculator
# # total_bill=int(input("enter your  bill"))
# # tip_percentage=int(input("enter your tip in percentage"))
# # total_person=int(input("enter the total number of persons"))
# # tip_amount=(tip_percentage/100)*total_bill
# # bill_per_person=(total_bill+tip_amount)/total_person
# # print(bill_per_person)
#
# #difficult.2
#
#
#
#
#
#
#
#
#
#
#
# #day.3
# #simple.1
# # nmbr=int(input("please enter a nmbr"))
# # if nmbr%2==0:
# #     print("The nmbr is even")
# # else:
# #      print("The nmbr is odd")
#
# #simple.2
# # age=int(input("please enter your age"))
# # if age<13:
# #      print("you are a chlid")
# # elif 13<=age<=17:
# #       print("you are a teen")
# # else:
# #       print("you are adult")
#
#
# #difficult.1
# # print("welcom to BMI calculator")
# # weight_kg=float(input("please enter your age in kg"))
# # height=float(input("please enter your height in meter "))
# # BMI=weight_kg/(height**2)
# # if BMI<18.5:
# #      print("you are under wight")
# # elif 18<=BMI<25:
# #      print("you are healthy")
# # elif 25<=BMI<30:
# #      print("you are over weight")
# # elif 30<=BMI<35:
# #      print("you are obese")
# # else:
# #      print("you are extremely obese")
#
#
#
# #
# # height = int(input("Please enter your height: "))
# #
# # if height >= 120:
# #     print("Can ride")
# #     age = int(input("Please enter your age: "))
# #     if age > 18:
# #         print("$12 price ")
# #     elif age > 12:
# #         print("$7 price")
# #     else:
# #         print("You have to pay $5")
# # else:
# #     print("can't ride")
#
#
#
#
# print("welcom to python pizza deliveries!")
# size=input("what pizza do you want?S,M,orL")
# add_pepperoni=input("do you want pepperoni?Y or N")
# extra_cheese=input("do you want extra cheese?Y or N")
# bill = 0
#
# if size == "S":
#     bill=bill+15
# elif size=="M":
#     bill=bill+20
# else:
#     bill=bill+25
# if add_pepperoni=="Y":
#     if size=="S":
#         bill=bill+2
#     else:
#         bill=bill+3
# if extra_cheese=="Y":
#     bill=bill+1
# print(f"your final bill is:${bill}")
#
#
#
#
#
#
#
#
#
# print('''
#
#
#                      ____...------------...____
#                 _.-"` /o/__ ____ __ __  __ \o\_`"-._
#               .'     / /                    \ \     '.
#               |=====/o/======================\o\=====|
#               |____/_/________..____..________\_\____|
#               /   _/ \_     <_o#\__/#o_>     _/ \_   \
#               \_________\####/_________/
#                |===\!/========================\!/===|
#                |   |=|          .---.         |=|   |
#                |===|o|=========/     \========|o|===|
#                |   | |         \() ()/        | |   |
#                |===|o|======{'-.) A (.-'}=====|o|===|
#                | __/ \__     '-.-'    __/ \__ |
#                |==== .'.'^'.'.====|
#            jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
#                `""""-""""""""""""""""""""""""""-""""`
#
#  ''')
#
# print("Welcome to the treasure Island")
# print('Your mission is to find the missing treasure')
#
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#    if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#    else:
#         print("You get attacked by an angry Shark. Game Over.")
#
# else:
#     print("You fall into the hole game over ")


