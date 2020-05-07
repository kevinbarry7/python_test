import introcs

def first_vowl(s):

    result = len(s)

    if introcs.find_str(s, 'a') > -1:
        return introcs.find_str(s, 'a')
    if introcs.find_str(s, 'e') > -1:
        return introcs.find_str(s, 'e')
    if introcs.find_str(s, 'i') >= 0:
        return introcs.find_str(s, 'i')
    if introcs.find_str(s, 'o') >= 0:
        return introcs.find_str(s, 'o')
    if introcs.find_str(s, 'u') >= 0:
        return introcs.find_str(s, 'u')
    if introcs.find_str(s, 'y') > 0:
        return introcs.find_str(s, 'y')
    return result


place = first_vowl('sss')
print(place)
