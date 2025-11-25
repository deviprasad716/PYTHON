menu={
    "popcorn":300,
    "soda":150,
    "fries":400,
    "samosa":200,
    "pizza":500,
    "burger":350
}

cart=[]
total=0
print("---------MENU---------")
for key ,value in menu.items():
    print(f"{key:10} : ${value}")
print("----------------------")

while True:
    food=input("Select your food item(q to quit): ")
    if food.lower()=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()

for items in cart:
    print(items, end=" ")

    total+=menu[items]

print(f"\nYour total bill is: Rs{total}")







    


