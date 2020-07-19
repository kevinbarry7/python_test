import pytz
from dateutil.parser import *
import datetime
from pytz import *


def daytime(time, daycycle):
    tz_cycle = daycycle['timezone']
    if time.tzinfo is not None:









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
