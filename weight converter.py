unit=input("Enter the unit(lbs/kg): ")
weight=float(input("Enter your weight:  "))

if unit=="lbs":
    result=weight*0.45
    print(f"Your weight is {round(result,2)} kgs")
elif unit=="kg":
    result=weight/0.45
    print(f"Your weight is {round(result,2)} lbs")
else:
    print("Invalid unit" )
