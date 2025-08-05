 # print('''
 #       __
 #      S()S
 #      .mm.
 #    _//)(\\
 #    \//##/_\
 #     /####\
 #    /######\as
 #    `"'"'"'`
 # ''')
# print("Welcom to Rescue Mission:daughter!")
# print("You are a father,enjoying a quite evening at home.your daughter has been kidnapped.You are her only hope.")
# print("Suddenly your phone rings.It is an unknown number.you answer the call.\n A distorted voice speaks:we have your daughter.\n Do not call the police.if you do,she dies.\nThey tell you they want money,and will call back with instructions. ")
# choice1=input('In the next call stranger asked:What do you do?if you agree to their demand type"agree"and If you try to call the police type"call"\n').lower()
# if choice1=="agree":
#     choice2=input('A thought hits you:what if they do not release her even after getting the money?Now the next decision:call CID or just wait for next call\n if you decide to call CID type"cid"and if you decide to wait for the next call type"call"\n ').lower()
#     if choice2=="cid":
#         choice3=input('You express your fear to CID that they might not release yor daughter even after getting the money.\n The CID assure you they will proceed with extreme caution,setting up a secret operation to try and track the kidnappers and secure your daughter.\nCID has two approaches first approach is cooperate with a controlled money drop- use the exchange as a trap for the kidnappers\n and the second approach is tracing the kidnappers mobile number to track them\nif you choose the first approach type"exchange"and if you choose the second approach type"track"\n').lower()
#         if choice3=="track":
#             print("CID does not succeed in its efforts about tracing the call.Game Over")
#         elif choice3=="exchange":
#             choice4=input('This is high_risk,high_reward strategy.As you approach the location with the cid team secretly positioned,the kidnappers voice comes through on a burners phone:\nThe location is now changed.The  CID team leader quickely assess the situation.\nnow the cid team has two options if cid team stick to original plan at the first location type"original"\n if the cid team moves to next location type "next"\n ' ).lower()
#             if choice4=="original":
#                 print("The kidnappers are now in the next location.The opportunity to catch them was lost.\nYour daughter remains missin.Game Over.")
#             else:
#                 print("CID trapped and caught the kidnappers,and you saved your daughter.You win!")
#         else:
#             print("you don't give any appropriate direction.you lost your daughter.Game Over")
#     elif choice2=="call":
#         choice3=input('You follow the kidnappers every command and start trying to arrange the money,praying for your daughter\'s safety.\nif you give them money type "money"and if you failed in arranging the money type"fail"\n').lower()
#         if choice3=="money":
#             print("you drop the money at the described place by the kidnappers but they do not realse your daughter.Your daughter is lost.Game over.")
#         else:
#             print("you lost your daughter.Game Over. ")
#     else:
#         print("you choose a option which does not exist.you neither prepare the money nor contact CID.Your daughter is lost.Game Over.")
# else:
#     print("you call the police.As soon as line connects you hear a laugh on the other end of the call.\nGame over.Your daughter is lost.")
# #


# marks = int(input("Please enter your marks. "))
# csMarks = int(input('Please enter your cs marks: '))

# if marks >= 80 or csMarks >= 90:
#     print("Admission granted")
# else:
#     print("try next time.")

# print(not False)



# print("arslan")
# input("hello")
# print("arslan yousaf")
# a = 25
# b = 10
# c = a % b
# print(c)
#
# a = int("123")
# print(type(a))


# num = input("Please enter two digit number: ")
# a=int(num[0])
# b=int(num[1])
# c=a+b
# print(c)

# import random
#
# rand_num = random.randint(0,1)
# if rand_num==1:
#     print("heads")
# else:
#     print("tails")


# sairamath = 99
# sairaurdu = 88
#
#
# sairamarks = [99,98,77,34,90]
# iqramarks = [88,67,88,99,23]
import random
# students=["Iqra","Saira","Esha","Tuba","Zoha"]
# random_nmbr =random.randint (0,4)
# print(students[random_nmbr])
# print(random.choice(students))

# print(students[-1])
# print(len(students) - 1)



# students.append("hijjab")
# students.extend(["hijjab", "noor"])
# students[2] = "mishal"
#print(students)


# students=["Iqra ","Saira ","Hamna ","yousma "]
# students.append("Laraib")
# students.extend(["Amna","Masfa"])
# students[2]="Javeria"
# print(students)


# names=["Iqra","Saira","laraib","Javeria"]
#
# for name in names:
#     print(name)
#     print(name+" Tooba")
# print(name)


# student_marks=[45,55,87,98,24,53,62]
# total_marks=0
# for marks in student_marks:
#     total_marks=total_marks+marks
#     print(total_marks)

# total_element=0
# for marks in student_marks:
#     total_element=total_element+1
#     print(total_element)

# total=sum(students_marks)
# num_of_students=len(students_marks)
# average_marks=total/num_of_students
# print(average_marks)





# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     print(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
# print(average_height)





#
# students_marks= [23,54,76,8,99,7,23,33,55,44,33]
# search_item=input("please enter a item you want to search")
# search_item_as_int=int(search_item)
# if search_item_as_int in students_marks:
#     print(f"search item is:{search_item}")
# else:
#     print("search item is not present in the students_marks list")


# students_marks= [23,54,76,8,99,7,23,33,55,44,33]
# if marks in students_marks:




# students_marks= [23,54,76,8,99,7,23,33,55,44,33]
# max_value=max(students_marks)
# print(max_value)
# min_value=min(students_marks)
# print(min_value)

# students_marks= [23,54,76,8,99,7,23,33,55,44,33]
# sum = 0
# count = 0
# for a in students_marks:
#     sum = sum + a
#     count = count + 1
#
# print(sum)
# print(count)

#
students_marks= [23,54,76,8,99,7,23,33,55,44,33]
highest_value = 0
for marks in students_marks:
    if marks > highest_value:
        highest_value = marks
print(f"The highest value is {highest_value}")

# students_marks= [23,54,76,8,99,7,23,33,55,44,3]
# lowest_value=10000000000000000000
# for marks in students_marks:
#     if marks<lowest_value:
#         lowest_value=marks
# print(lowest_value)

# students_marks= [23,54,76,8,99,7,23,33,55,44,33]
# search_value = int(input("Please enter the value you want to search"))
# is_exist = False
# for marks in students_marks:
#     if search_value == marks:
#         is_exist = True
#
#
# if is_exist:
#     print("Value exist in the list")
# else:
#     print("Value not Exist in the list")



# students_marks= [23,54,76,8,99,7,23,33,55,44,33]


# total_num = 0
# for num in range(1,101):
#     print(num)
#     total_num += num
#
# total_num=0
# for num in range(2,101,2):
#     print(num)
#     total_num +=num
# print(total_num)

# total_num=0
# for num in range(1,101,2):
#     print(num)
#     total_num +=num
# print(total_num)


# FizzBuzz
# for num in range(1,101):
#    if num % 3 == 0 and num % 5 == 0:
#           print("FizzBuzz")
#    elif num%3==0:
#         print("Fizz")
#    elif num%5==0:
#          print("Buzz")
#    else:
#           print(num)



# students_marks= [23,54,76,23,8,99,7,23,33,55,33,44,33]
# count=0
# search_item=23
# for marks in students_marks:
#     if search_item==marks:
#      count=count+1
# print(count)



# print('''
#
#
#                     ____...------------...____
#                _.-"` /o/__ ____ __ __  __ \o\_`"-._
#              .'     / /                    \ \     '.
#              |=====/o/======================\o\=====|
#              |____/_/________..____..________\_\____|
#              /   _/ \_     <_o#\__/#o_>     _/ \_   \
#              \_________\####/_________/
#               |===\!/========================\!/===|
#               |   |=|          .---.         |=|   |
#               |===|o|=========/     \========|o|===|
#               |   | |         \() ()/        | |   |
#               |===|o|======{'-.) A (.-'}=====|o|===|
#               | __/ \__     '-.-'    __/ \__ |
#               |==== .'.'^'.'.====|
#           jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
#               `""""-""""""""""""""""""""""""""-""""`
#
#
# ''')
#


# def abc():
#     print("this is function abc")
#     print("this also include in function")
#
#
#
# abc()
# abc()
# abc()

# def control():
#     print("this is a function in python language")
#     print("hello world")
# control()
# control()


# def python():
#     print("hello world")
#     print("I am a python programmer")
# python()
# python()

#
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# #Write your code below this line 👇
#
# choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")