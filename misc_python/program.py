#!/usr/local/bin/python3

message = ("Liverpool are champions")
print(message)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
print()

print("f strings")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
message1 = (f"Hello, {full_name.title()}!")
print(message1)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'Python   '
favorite_language1 = '   JavaScript'
clean_fl = favorite_language.rstrip()
clean_fl1 = favorite_language1.lstrip()

print(f"{clean_fl} & {clean_fl1}")

name1 = "Kevin"
print(f"Hello {name1}, would you like to learn Python today?")
print(name1.lower())
print(name1.upper())
print(name1.title())
print()

author = "Albert Einstein"
string = 'once said, A person who never made a mistake never tried anything new.'
print(f'{author} once said, "A person who never made a\n mistake never tried anything new.')
print(id(author))

b = 2
b += 2
print(b)

six = 2 + 2 + 2
six *= -6
print(six)

half = 2 * 0.25
print(half)
other_half = 1.0 - half
print(other_half)
f = 4 < 5
print(f)

cold = True
rain = False
day = cold and rain
print(day)

one = "one"
another_one = "1.0"
last_one = "one 1"
print(float(six))

x, y, z = 0, 1, 2
print(x, y, z)
print()
print("____Lists___")

bicycles = ["trek", "specialized", "redline", "cannondale"]
print(bicycles)

print(bicycles[0])
print(bicycles[1].title())
print(f"My first bicycle was a {bicycles[1].title()} model")


motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[1] = 'ducati'
print(motorcycles[1].title())
print(motorcycles)


motorcycles.append('yamaha')
motorcycles.insert(1, 'notamotorcycle')
print(motorcycles)
del motorcycles[0]
popped = motorcycles.pop()
print(f"The last motorcycle that I owned was a {popped.title()}")
removed = 'notamotorcycle'
motorcycles.remove(removed)
print(f"I removed the {removed} bike, because it's not a real motorcycle")
print(motorcycles)

cars = ['bmw', 'volvo', 'ford', 'audi']
cars.sort() #permanent sort
print(cars)
cars.sort(reverse=True) #permanent sort
print(cars)
print(sorted(cars)) #temporary sort
print(cars)

cars.reverse()
print(cars)
print(len(cars))
print(cars[-1])

print("________Lists/Looping________")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait for your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show.")

for value in range(1, 8):
    print(value)

for values in range(9+1):
    print(values)

numbers = list(range(0,14,3))
print(numbers)

squares = []
for value in range(1, 10):
    square = value**2
    squares.append(square)
print(squares)

#slightly more concise method
squares1 = []
for value in range(1, 10):
    squares1.append(value**2)
print(squares1)

print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehensions
squares2 = [value**2 for value in range(1,21)]
print(squares2)

for value in range(21):
    print(value)
million = [value for value in range(1, 1000001)]
print(min(million))
print(max(million))
print(sum(million))

for value in range(1,20,2):
    print(value)

list3s = []
for value in range(3,31,3):
    list3s.append(value)
print(list3s)
list3 = []
for value in range(1,11):
    list3.append(value**3)
for lis in list3:
    print(lis)

listcube = [value**3 for value in range(1,11)]
print(listcube)

print("_____Slicing a list________\n")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[::2])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n________Tuples__________")
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

my_tuple = (4,) #also a valid tuple with one entry but must include comma

dimensions = (400, 50)

print("____________If_____________-")

cars = ['audi', 'volvo', 'bmw', 'ford']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again\n")

requested_toppings = ['mushrooms', 'onions', 'green peppers', 'pineapple']
if 'pineapple' in requested_toppings:
    print("Yep, pineapple are in the list\n")

if 'pepperoni' not in requested_toppings:
    print("Nope, pepperoni is not in the list\n")

age = 16
if age > 17:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Please register as soon as you turn 18\n")

ages = 12
if ages < 4:
    print("Your admission cost is $0\n")
elif ages <= 18:
    print("Your admission cost is $25\n")
else:
    print("Your admission cost is $40\n")

alien_color = 'red'
if alien_color == 'green':
    print("You have just earned 5 points!\n")
elif alien_color == 'yellow':
    print("You have just earned 10 points!\n")
elif alien_color == 'red':
    print("Your have just earned 15 points!\n")

age1 = 48
if age1 < 2:
    print("Person is a baby")
elif age1 <4:
    print("Person is a toddler")
elif age1 < 13:
    print("Person is a kid")
elif age1 <20:
    print("Person is a teenager")
elif age1 < 65:
    print("Person is an adult")
else:
    print("Person is an elder")

favorite_fruit = ['apple', 'banana', 'pineapple', 'peach']
if 'apple' in favorite_fruit:
    print("You really like apples\n")
if 'peach' in favorite_fruit:
    print("You really like peaches\n")
if 'limes' not in favorite_fruit:
    print("I guess you don't like limes\n")

for requested in requested_toppings:
    if requested == 'green peppers':
        print("Sorry, we're out of green peppers right now.")
    else:
        print(f"Adding {requested}.")
print("Finished making your pizza!\n")

requested1 = []
if requested1:
    for requested_top in requested1:
        print(f"Adding {requested_top}")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requestedd_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requestedd_topping in requestedd_toppings:
    if requestedd_topping in available_toppings:
        print(f"Adding {requestedd_topping}")
    else:
        print(f"Sorry, we don't have {requestedd_topping}")
print("Finished making your pizza\n")

user_names = ['mary', 'kfb', 'april', 'admin', 'ellen']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Hello {user_name}, would you like to see a status report?")
        else:
            print(f"Hello {user_name}, thank you for logging in again.")
else:
    print("There are no users registered in this system!")
print("\n")

new_users = ['kfB', 'john', 'sean', 'steph', 'ellen']

if new_users:
    for new_user in new_users:
        if new_user.lower() in user_names:
            print(f"The user name {new_user} is already taken")
        else:
            print(f"The user name {new_user} can be used")
print("Done!\n")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number2 in numbers_list:
    if number2 == 1:
        print(f"{number2}st\n")
    elif number2 == 2:
        print(f"{number2}nd\n")
    elif number2 == 3:
        print(f"{number2}rd\n")
    else:
        print(f"{number2}th\n")
print("All done!!!")
