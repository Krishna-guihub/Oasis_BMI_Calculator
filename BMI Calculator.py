name=input("Enter your name : ")
Age=input("Enter your age : ")
weight= int(input("Enter your weight in pound : "))
height= int(input("Enter your height in inches : "))
BMI  = (weight * 703) / (height * height)
if BMI >0:
    if (BMI<18.5):
        print(name +", you are UnderWeight .")
    elif(BMI<=24.9):
         print(name +", you are normal weight.")
    elif(BMI<=29.9):
        print(name + ", you are overweight ")
    elif(BMI > 34.9):
        print(name +" , you have obese")
    elif(BMI > 39.9):
        print(name +" , you have severely obese")
    else :
        print(name +" , you are morbidly obese ")
else:
    print("Enter valid input")




print(BMI)



