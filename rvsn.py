# S=("ravi kumarCHAmbial is an Are")
# print(S)
# print(S.count("A"))
# print(S.capitalize())
# print(S.endswith(("is","an","are")))
# print(S)
# str = 'xyz\t12345\tabc'
# print(str)
# s = '123'
# print(s.isdecimal())
# print(s.isdigit())
# print(s.isnumeric())
# grocery = 'Milk, Chicken, Bread, Butter'
# print(grocery)
# print(grocery.rsplit(', ', 2))

# T=("ravi kumar","chambial",'python')
# print(T[1].capitalize())
# print(T[::-1])
# print(T)
# print(type(T))

# l=[1,"ravi",2,3,4,5,8,6,7,6]
# print(l[1].capitalize())
# print(l[2::2])
# print(l[::-1])
# l.reverse()
# l.append("a")
# l.insert(3,"b")
# print(l)
# print(l.pop(2))
# l.remove(6)
# print(l.extend(T))
# print(l.index(6,7,9))
# print(l)

# fruits = { 'apple': 'seb', 'orange': 'santra', 'grapes': 'angoor', 'mango':'aam' }
# userinput=input('enter fruit name ')
# print(fruits[userinput])
# print(fruits.get(userinput))

# operator= input("enter operator ")
# firstnumber= int(input("enter first number "))
# secondnumber= int(input("enter second number "))
# if operator=='+':
#     if (firstnumber== 56 and secondnumber == 9):
#         print("77")
#     else:
#         print(firstnumber+secondnumber)

# elif operator=='*':
#     if (firstnumber== 45 and secondnumber == 3):
#         print("555")
#     else:
#         print(firstnumber*secondnumber)


# number=18
# Guess=1
# while(True):
#     InputNumber=int(input("Enter a number "))
#     if InputNumber== 18:
#         print("Game Over. You took {} guesses to complete the game ".format(Guess))
#         break
#     elif Guess==5:
#         print("Game Over.You loose. You have used {} guesses.".format(Guess))
#         break
#     elif InputNumber>number:
#         print("Enter smaller number ")
#         Guess+=1
#     elif InputNumber<number:
#         print("Enter greater numnber ")
#         Guess+=1


# number= int(input("Enter a number "))
# boolean= int(input("Enter 0 or 1 ")) 
# for i in range(number):
#     if boolean==True:
#         print("*"+"*"*i)
#     else:
#         print("*"+"*"*(number-(i+1)))


# f=open("E:\\Rvichambial\\ravi_meal.txt",'r+')
# f.write(" Morning: Juice,fruits \n Noon: Roti, sabji \n evening: egg,momos \n Night: roti, sabji, milk")
# f.seek(0)
# print(f.read())
# f.close()
# f=open("E:\\Rvichambial\\ravi_exercise.txt",'r+')
# f.write(" Morning: running, Yoga, meditation \n Evening: pull ups, push ups, stretching")
# f.seek(0)
# print(f.read())
# f.close()

# f=open("E:\\Rvichambial\\chambial_meal.txt",'r')
# f.write(" Morning: milk,fruits \n Noon: Chawal, Daal, dahi \n evening: golgappe,soup \n Night: roti, sabji")
# f.seek(0)
# print(f.read())
# f.close()
# f=open("E:\\Rvichambial\\chambial_exercise.txt",'r+')
# f.write(" Morning: running, Yoga \n Evening: Gym, stretching")
# f.seek(0)
# print(f.read())
# f.close()

# name=int(input("Choose a number: \n 1 for Ravi \n 2 for Chambial \n"))
# chart=int(input("Choose a number: \n 1 for Meal \n 2 for Exercise \n"))
# if (name==1):
#     if chart==1:
#         meal_time=int(input("Choose a Meal Time: \n 1 for morning \n 2 for noon \n 3 for evening \n 4 for night \n"))
#         if meal_time==1:
#             f=open("E:\\Rvichambial\\ravi_meal.txt",'r')
#             f.seek(0)
#             print(f.readline())
#             f.close()
#         elif meal_time==2:
#             f=open("E:\\Rvichambial\\ravi_meal.txt",'r')
#             f.seek(0)
#             f.readline()
#             print(f.readline())
#             f.close()
#         elif meal_time==3:
#             f=open("E:\\Rvichambial\\ravi_meal.txt",'r')
#             f.seek(0)
#             f.readline()
#             f.readline()
#             print(f.readline())
#             f.close()
#         elif meal_time==4:
#             f=open("E:\\Rvichambial\\ravi_meal.txt",'r')
#             f.seek(0)
#             f.readline()
#             f.readline()
#             f.readline()
#             print(f.readline())
#             f.close()
#     if chart==2:
#         exercise_time=int(input("Choose a exercise Time: \n 1 for morning \n 2 for evening\n"))
#         if exercise_time==1:
#             f=open("E:\\Rvichambial\\ravi_exercise.txt",'r')
#             f.seek(0)
#             print(f.readline())
#             f.close()
#         elif exercise_time==2:
#             f=open("E:\\Rvichambial\\ravi_exercise.txt",'r')
#             f.seek(0)
#             f.readline()
#             print(f.readline())
#             f.close()

# if (name==2):
#     if chart==1:
#         meal_time=int(input("Choose a Meal Time: \n 1 for morning \n 2 for noon \n 3 for evening \n 4 for night \n"))
#         if meal_time==1:
#             f=open("E:\\Rvichambial\\chambial_meal.txt",'r')
#             f.seek(0)
#             print(f.readline())
#             f.close()
#         elif meal_time==2:
#             f=open("E:\\Rvichambial\\chambial_meal.txt",'r')
#             f.seek(0)
#             f.readline()
#             print(f.readline())
#             f.close()
#         elif meal_time==3:
#             f=open("E:\\Rvichambial\\chambial_meal.txt",'r')
#             f.seek(0)
#             f.readline()
#             f.readline()
#             print(f.readline())
#             f.close()
#         elif meal_time==4:
#             f=open("E:\\Rvichambial\\chambial_meal.txt",'r')
#             f.seek(0)
#             f.readline()
#             f.readline()
#             f.readline()
#             print(f.readline())
#             f.close()
#     if chart==2:
#         exercise_time=int(input("Choose a exercise Time: \n 1 for morning \n 2 for evening\n"))
#         if exercise_time==1:
#             f=open("E:\\Rvichambial\\chambial_exercise.txt",'r')
#             f.seek(0)
#             print(f.readline())
#             f.close()
#         elif exercise_time==2:
#             f=open("E:\\Rvichambial\\chambial_exercise.txt",'r')
#             f.seek(0)
#             f.readline()
#             print(f.readline())
#             f.close()    

def rvi(a,*arg):
    print (a)
    print(arg)

# b=["ravi","chambial","kumar","singh"]
rvi("1",*["ravi","chambial","kumar","singh"],"z")
        
