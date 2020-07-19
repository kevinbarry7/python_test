

weather = {
            "2017-04-21T08:00:00-04:00": {
                "visibility": {
                    "prevailing": 10.0,
                    "units": "SM"
                },
                "wind": {
                    "speed": 13.0,
                    "crosswind": 2.0,
                    "units": "KT"
                },
                "temperature": {
                    "value": 13.9,
                    "units": "C"
                },
                "sky": [
                    {
                        "cover": "clouds",
                        "type": "broken",
                        "height": 700.0,
                        "units": "FT"
                    }
                ],
                "code": "201704211056Z"
            },
            "2017-04-21T07:00:00-04:00": {
                "visibility": {
                    "prevailing": 10.0,
                    "units": "SM"
                },
                "wind": {
                    "speed": 13.0,
                    "crosswind": 2.0,
                    "units": "KT"
                },
                "temperature": {
                    "value": 57.0,
                    "units": "F"
                },
                "sky": [
                    {
                        "type": "overcast",
                        "height": 700.0,
                        "units": "FT"
                    }
                ],
                "code": "201704210956Z"
            }}
accum = 0
temp = 13.9

for i in weather.keys():
    # print(weather[i]['temperature'])
    x = weather[i]['temperature']['value']
    print(x)
    y = weather[i]['temperature']['units']
    print(y)
    if y == 'F':
        x = 5 * (x - 32)/9.0
        print(x)
    if x >= temp:
        accum = accum + 1
print(accum)
















