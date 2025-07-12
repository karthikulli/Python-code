import random
min_value=int(input("Enter min value: "))
max_value=int(input("Enter max value: "))
user_1_Name=input("Enter user_1 Name: ")
user_2_Name=input("Enter user_2 Name: ")
user_1_count=0
user_2_count=0
for i in range(5):
    user_1=int(input("{} guess the correct number to win: ".format(user_1_Name)))
    user_2=int(input("{} guess the correct number to win: ".format(user_2_Name)))
    random_value=random.randint(min_value,max_value)
    if random_value==user_1:
        user_1_count+=1
    if random_value==user_2:
        user_2_count+=1
if user_1_count>user_2_count:
    print("{} winner".format(user_1_Name))
    print("{} guess {} times correct".format(user_1_Name,user_1_count))
elif user_1_count==user_2_count:
    print("Draw")
else:
    print("{} winner".format(user_2_Name))
    print("{} guess {} times correct".format(user_2_Name,user_2_count))
