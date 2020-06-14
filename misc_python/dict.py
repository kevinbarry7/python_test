print("dict.py")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
print(alien_1)
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

alien_1['color'] = 'yellow'
print(alien_1)

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position']}")

alien_2 = {'color': 'red', 'points': 0}
print(alien_2)
del alien_2['color']
print(alien_2)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")
print(f"Jen's favorite language is {favorite_languages['jen'].title()}")

person = {
    'first name': 'mary',
    'last name': 'flynn',
    'age': 54,
    'city': 'drumshanbo',
}

print(person)

favorite_number = {
    'kevin': 7,
    'april': 1,
    'meg': 4,
    'sean': 89,
}

print(favorite_number)
print("\n")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# for key.value in user_0.items():
#     print(f"Key: {key}")
#     print(f"Value: {value}")
#     print("\n")
