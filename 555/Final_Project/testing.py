from introcs import RGB



# def mono(image, sepia=False):
#     height = len(image)
#     width = len(image[0])
#
#     if not sepia:
#         for row in range(height):
#             for col in range(width-1):
#                 pixel = image[row][col]
#                 r = pixel.red
#                 g = pixel.green
#                 b = pixel.blue
#                 val = int(r * 0.3 + g * 0.6 + b * 0.1)
#                 pixel.red = val
#                 pixel.green = val
#                 pixel.blue = val
#         return True
#
#     else:
#         for row in range(height):
#             for col in range(width-1):
#                 pixel = image[row][col]
#                 r = pixel.red
#                 g = pixel.green
#                 b = pixel.blue
#                 val = int(r * 0.3 + g * 0.6 + b * 0.1)
#                 pixel.green = int(val * 0.6)
#                 pixel.blue = int(val * 0.4)
#
#         return True


image = [[255, 24, 46, 126], [78, 83, 88, 120], [160, 229, 125, 208], [240, 120, 29, 200],
     [200, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]]

# result = mono(a)
# print(result)
# print(a)
# result = mono(a, True)
# print(result)
# print(a)

#
# a = [elem[::-1] for elem in a][::-1]
# print(a)


# def mono(image, sepia=False):
#     height = len(image)
#     width = len(image[0])
#
#     for row in range(height):
#         for col in range(width):
#             pixel = image[row][col]

# org_list = [1, 2, 3, 4, 5]
#
# new_list = org_list[::-1]
# print(org_list)
# print(new_list)
#
#
# numrows = len(image)
# numcols = len(image[0])
# result = []
# for m in range(numcols):
#     row = []
#     for n in range(numrows):
#         row.append(image[n][m])
#     result.append(row)

    # image1 = [elem[::-1] for elem in image][::-1]
    #
    # if vertical == False:
    #     pass
    #
    #
    # else:
    #     image.reverse()
    #     return True
#
# if vertical == False:
#     reversed(image)
#
# return True
#
# else:
# image.reverse()
#
# return True

numrows = len(image)
numcols = len(image[0])

# for j in range(numrows):
#     for i in range(int(numcols/2)):
#         image[i], image[-(i+1)] = image[-(i+1)], image[i]
#
# print(image)

for i in range(numrows):
    for j in range(numcols):
        image.append([i][j])
print(image)
