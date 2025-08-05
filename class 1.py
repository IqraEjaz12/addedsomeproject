#print("welcom to python programming")

# user_name=input("enter your name")
# fav_colour=input("enter your favourite colour")
# print(user_name+" like "+fav_colour)

# user=input("please enter your name")
# print(f"hello {user}")


# print("This Software is used to enhance the brand name")
# brand_name=input("please enter your brand name")
# random_nmbr=input=("please enter a random nmbr")



# input1=input("please enter the first input")
# input2=input("please enter the second input")
# print(type(input1))
# print(type(input2))

# age=int(input("please enter your age"))
# if age<13:
#     print("you are a chlid")
# if 13<age<18:
#     print("you are a teen")
# if age>18:
#     print("you are adult")


# print("welcom to BMI calculator")
# weight_kg=float(input("please enter your age in kg"))
# height=float(input("please enter your height in meters "))
# BMI=weight_kg/(height**2)
# if BMI<18:
#     print(f"your BMI is {BMI};you are under weight")
# elif 18<=BMI<25:
#     print(f"your BMI is {BMI};you are healthy")
# elif 25<=BMI<30:
#     print(f"your BMI is {BMI};you are over weight")
# elif 30<=BMI<35:
#     print(f"your BMI is {BMI};you are obese")
# else :
#     print(f"your BMI is {BMI};you are extremely obese")

# print('''
#
#
#
#
#  ''')
#
print("wlcome to save the drowning child mission!")
print("a child is drowning in the river!")
print("you don't know how to swim,but you want to help him.")
choice1=input('do you shout for help or try to jump in?if you shout for help type "shout"if you try to jump type "jump"\n').lower()
if choice1=="shout":
    choice2=input('you shout for help.a nearby fisherman hears you and comes running\n do you guide the fisherman to the spot or try to get closer yourself?\n if you guide the fisherman type"guide"if you try to get closer type"closer"\n').lower()
    if choice2=="guide":
        print("the fisherman throws a rope to the child and pulls him out.you saved the child!")
    elif choice2=="closer":
         choice3=input('you got too close and slipped!now you are also in danger.you found a floating log.do you try to float using a log or call the child to swim to you?\n if you try to float by log type"log"and if you try to call the child type"call"\n').lower()
         if choice3=="log":
             print("you grab a floating log and reach the child.with the help of log you succeed in saving the child.you win!")
         else:
             print("the child could't know how to swim.the child was lost.game over.")
    else:
        print("there was no any other option.the time was lost and the child could't be saved")

else:
    print("you don't know how to swim and jump in. you are struggling.the child could not be saved.game over.")
#





