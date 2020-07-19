def bad_visibility(visibility, minimum):

    feetpermile = 5280
    if visibility == 'unavailable':
        result = True
    elif visibility['units'] == 'FT':
        minimum = minimum * feetpermile
        if minimum > visibility['minimum']:
            result = True
        else:
            result = False
    elif visibility['units'] == 'SM':
        if minimum > visibility['prevailing']:
            result = True
        else:
            result = False
    return result


def bad_winds(winds, maxwind, maxcross):
    one_MPS = 1.94384
    keys1 = {'speed', 'units', 'gusts', 'crosswind'}
    keys2 = {'speed', 'units', 'gusts'}
    keys3 = {'speed', 'units', 'crosswind'}

    if winds == 'unavailable':
        result = True
    elif winds == 'calm':
        result = False
    else:

        if winds['units'] == 'KT':
            if (winds.keys()) == keys1:
                if winds['crosswind'] > maxcross or winds['speed'] > maxwind or winds['gusts'] > maxwind:
                    result = True
                else:
                    result = False
            elif (winds.keys()) == keys2:
                if winds['speed'] > maxwind or winds['gusts'] > maxwind:
                    result = True
                else:
                    result = False
            elif (winds.keys()) == keys3:
                if winds['crosswind'] > maxcross or winds['speed'] > maxwind:
                    result = True
                else:
                    result = False
        else:
            speed = winds['speed'] * one_MPS
            if (winds.keys()) == keys1:
                crosswind = winds['crosswind'] * one_MPS
                gusts = winds['gusts'] * one_MPS
                if speed > maxwind or crosswind > maxcross or gusts > maxwind:
                    result = True
                else:
                    result = False
            elif (winds.keys()) == keys2:
                gusts = winds['gusts'] * one_MPS
                if speed > maxwind or gusts > maxwind:
                    result = True
                else:
                    result = False
            elif (winds.keys()) == keys3:
                crosswind = winds['crosswind'] * one_MPS
                if speed > maxwind or crosswind > maxcross:
                    result = True
                else:
                    result = False
    return result

def bad_ceiling(ceiling, minimum):
    result = True
    height = 0
    if ceiling == 'unavailable':
        result = True
    elif ceiling == 'clear':
        result = False
    else:
        ceiling_len = len(ceiling)
        for i in range(ceiling_len):
            if 'overcast' or 'broken' or 'indefinite' in ceiling[i]['type'] and ceiling[i]['height'] < height:
                height = ceiling[i]['height']
                if height >= minimum:
                    result = 'False1'
                else:
                    result = 'True1'
            if ceiling[i]['height'] > height:
                height = ceiling[i]['height']
                if height >= minimum:
                    result = False
                else:
                    result = True
    return result


result = bad_ceiling('clear', 500)  # False.
print(result)
result1 = bad_ceiling([{'type': 'overcast', 'height': 200.0, 'units': 'FT'}], 500)  # True
print(result1)
result2 = bad_ceiling([{'cover': 'clouds', 'type': 'broken', 'height': 2000.0, 'units': 'FT'}], 2000)  # False
print(result2)
result3 = bad_ceiling([{'cover': 'clouds', 'type': 'a few', 'height': 1900.0, 'units': 'FT'}, {'cover': 'clouds', 'type': 'broken', 'height': 2900.0, 'units': 'FT'}, {'type': 'overcast', 'height': 3400.0, 'units': 'FT'}], 2000)  # False
print(result3)
result4 = bad_ceiling([{'cover': 'clouds', 'type': 'broken', 'height': 1200.0, 'units': 'FT'}, {'type': 'overcast', 'height': 1800.0, 'units': 'FT'}], 1500)  # returned False, but should have returned True.
print(result4)




# result = bad_winds({'speed': 11.0, 'crosswind': 11.0, 'gusts': 15.0, 'units': 'MPS'},30,20)
# print(result)
# result1 = bad_winds({'speed': 13.0, 'crosswind': 11.0, 'units': 'KT'}, 30, 20)
# print(result1)
# result2 = bad_winds({'speed': 13.0, 'crosswind': 7.0, 'gusts': 31.0, 'units': 'KT'}, 30, 20) # returned False, but should have returned True.
# print(result2)
# result3 = bad_winds('unavailable', 30, 20)
# print(result3)

