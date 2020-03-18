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
