import introcs

# s = 'Hello World'
#
# t1 = tuple(s)
# print(t1[:-1])
#
# s2 = str(t1)
# print(s2[:-1])
#
# s3 = introcs.join(t1, ',')
# print(s3)
#
# s4 = introcs.join(t1,'')
# print(s4)
#
# t2 = introcs.split(s)
# print(t2)
#
# t3 = introcs.split(s, 'o')
# print(t3)


# s = 'str tups'
# t1 = tuple(s)
# print(t1)
#
# s2 = str(t1)
# print(s2[1:])
#
# s3 = introcs.join(t1,'-' )
# print(s3)
#
# s4 = introcs.join(t1[4:], '')
# print(s4)
#
# t2 = introcs.split(s)
# print(t2)
#
# t3 = introcs.split(s, 't')
# print(t3)

counter = 0
going = True

while going:
    response = input("Keep going [y/n]? ")
    if response == 'y':
        counter = counter + 1
    elif response == 'n':
        going = False
        print("You answered 'y' " + str(counter) + " times.")
    else:
        print("Answer unclear. Use 'y' or 'n'.")


