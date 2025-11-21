operator=input("Enter your operator(+ - * /): ")

num1=float(input("Enter your 1st number: "))
num2=float(input("Enter your 2nd number: "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("INVALID Operator")