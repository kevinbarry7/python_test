
import pytz
from dateutil.parser import *
import datetime
from pytz import *


def str_to_time(timestamp, tz=None):

    try:
        result = parse(timestamp)
        if result.tzinfo is None and tz is None:
            return result
        elif result.tzinfo is None and type(tz) == str:
            time1 = pytz.timezone(tz)
            e = time1.localize(result)
            return e
        elif result.tzinfo is not None and tz is None:
            return result
        elif result.tzinfo is None and tz is not None:
            g = result.replace(tzinfo=tz)
            return g
        elif result.tzinfo is not None and tz is not None:
            h = result.replace()
            return h
    except ValueError:
        return None
    
    
def daytime(time, daycycle):

    try:
        res = parse(time)

        print(type(res))
        time = res
        print(type(time))
        tz_cycle = daycycle['timezone']
        print(tz_cycle)
        if time.tzinfo is not None:
            year1 = time.strftime('%Y')
            print(year1)
            date1 = time.strftime('%m-%d')
            print(date1)
            sunrisetime = daycycle[year1][date1]['sunrise']
            print(sunrisetime)
            sunsettime = daycycle[year1][date1]['sunset']
            print(sunsettime)
            y = year1 + '-' + date1
            y1 = datetime.datetime.strptime(y, '%Y-%m-%d')
            y3 = datetime.datetime.strptime(sunrisetime, '%H:%M').time()
            y2 = datetime.datetime.combine(y1, y3)
            x = y2.isoformat()

            y4 = datetime.datetime.strptime(sunsettime, '%H:%M').time()
            y5 = datetime.datetime.combine(y1, y4)
            x1 = y5.isoformat()
            back_sunrise = str_to_time(x, tz_cycle)
            print(back_sunrise)
            back_sunset = str_to_time(x1, tz_cycle)
            print(back_sunset)

            if back_sunrise < time < back_sunset:
                return True
            else:
                return False
        elif res.tzinfo is not None:
            print('TZ')
            back1 = str_to_time(time, tz_cycle)
            print(back1)
            year1 = res.strftime('%Y')
            print(year1)
            date1 = res.strftime('%m-%d')
            print(date1)
            sunrisetime = daycycle[year1][date1]['sunrise']
            print(sunrisetime)
            sunsettime = daycycle[year1][date1]['sunset']
            print(sunsettime)
            z = year1 + '-' + date1
            z1 = datetime.datetime.strptime(z, '%Y-%m-%d')
            z3 = datetime.datetime.strptime(sunrisetime, '%H:%M').time()
            z2 = datetime.datetime.combine(z1, z3)
            w = z2.isoformat()

            z4 = datetime.datetime.strptime(sunsettime, '%H:%M').time()
            z5 = datetime.datetime.combine(z1, z4)
            w1 = z5.isoformat()
            back_sunrise1 = str_to_time(w, tz_cycle)
            print(back_sunrise1)
            back_sunset1 = str_to_time(w1, tz_cycle)
            print(back_sunset1)
            if back_sunrise1 < back1 < back_sunset1:
                return True
            else:
                return False
    except KeyError:
        return None


daycycle = {
    "city": "Ithaca",
    "state": "New York",
    "latitude": "076-29W",
    "longitude": "42-26N",
    "timezone": "America/New_York",
    "2015": {
        "01-01": {
            "sunrise": "07:35",
            "sunset": "16:44"
        },
        "01-02": {
            "sunrise": "07:36",
            "sunset": "16:45"
        },
        "01-03": {
            "sunrise": "07:36",
            "sunset": "16:45"
        }
    }
}

times = [('2015-06-05T07:00:00', True, True), ('2015-06-05T17:00:00', True, True),
         ('2015-10-31T06:00:00', False, True), ('2015-10-31T17:00:00', True, False),
         ('2015-11-17T07:00:00', True, True), ('2015-11-17T17:00:00', False, False),
         ('2015-12-11T07:00:00', False, True), ('2015-06-05T17:00:00', True, True),
         ('2016-11-01T07:00:00', True, True), ('2016-11-01T17:00:00', False, False),
         ('2017-11-17T07:00:00', False, True), ('2017-11-17T17:00:00', False, False),
         ('2018-06-05T07:00:00', True, True), ('2018-06-05T17:00:00', True, True),
         ('2018-11-15T07:00:00', True, True), ('2018-11-15T17:00:00', False, False),
         ('2019-11-15T07:00:00', True, True), ('2019-11-15T17:00:00', False, False)]



# CHECK THE TEST CASES
day = daytime('2015-01-02T07:38:00', daycycle)
print(day)


day = daytime('2015-01-01T07:34:00-05:00', daycycle)
print(day)


# input = '2016-05-12'
# result = str_to_time(input)
# print(result)
#
# input = '16:23'
# result = str_to_time(input)
# print(result)
#
# input = '16:23-4:00'
# result = str_to_time(input)
# print(result)
#
# input = '2016-05-12T16:23-4:00'
# result = str_to_time(input)
# print(result)
#
# input = '2016-05-12T16:23'
# correct = parse(input + '-4:00')
# print(correct)
# result = str_to_time(input, correct.tzinfo)
# print(result)

# input = '2016-05-12T16:23'
# central = 'America/Chicago'
# correct = timezone(central).localize(parse(input))
# print(type(correct))
# result = str_to_time(input, central)
# print(result)
# input = '2016-05-12T16:23'
# correct = parse(input + '-5:00')
# print(correct)
# offset = parse(input + '-4:00')
# print(offset)
# result = str_to_time(input + '-5:00', offset)
# print(result)

# date1 = time.strftime('%m-%d')
# year = time.strftime('%Y')
# tz_cycle = daycycle['timezone']
# print(tz_cycle)
# sunrisetime = daycycle[year][date1]['sunrise']
# print(sunrisetime)
# sunsettime = daycycle[year][date1]['sunset']
# y = year + '-' + date1
# y1 = datetime.datetime.strptime(y, '%Y-%m-%d')
# y3 = datetime.datetime.strptime(sunsettime, '%H:%M').time()
# y2 = datetime.datetime.combine(y1, y3)
# x = y2.isoformat()

# if sunsettime == ' ':
#     return None
# else:
#     res = str_to_time(x)
#     return res