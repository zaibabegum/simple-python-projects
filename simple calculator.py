num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
print("which operaton do you want?")
operator = input(" enter either +,-,* or / :")
if operator == "+" :
    print(num1,operator,num2,"=",num1+num2)
elif operator == "-":
    print(num1,operator,num2,"=",num1-num2)
elif operator == "*":
    print(num1,operator,num2,"=",num1*num2)
elif operator == "/" :
    print(num1,operator,num2,"=",num1/num2)
else:
    print("invalid operator")