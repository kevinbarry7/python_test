one_MPS = 1.94384

if winds == 'unavailable':
    result = True
elif winds == 'calm':
    result = False
elif winds['units'] == 'KT':
    if winds['crosswind'] > maxcross or winds['speed'] > maxwind:
        result = True
    else:
        result = False
elif winds['units'] == 'MPS':
    speed = winds['speed'] * one_MPS
    crosswind = winds['crosswind'] * one_MPS
    gusts = winds['gusts'] * one_MPS
    if speed > maxwind or crosswind > maxcross or gusts > maxwind:
        result = True
    else:
        result = False
return result