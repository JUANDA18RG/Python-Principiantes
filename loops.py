# author juan david ramirez
# date 20/07/2023

# for loops
foods = ['apples', 'bread', 'cheese', 'milk', 'bananas', 'graves']

for food in foods:
    if food == "cheese":
        print("you have to buy this")
        break
    print(food)


# for loops
for number in range(1, 8):
    print(number)


# while loops
count = 4

while count <= 10:
    print(count)
    count = count + 1
