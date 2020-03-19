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

