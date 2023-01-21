import datetime

#Given a moment, determine the moment that would be after a gigasecond has passed.
def add(moment):
    new_date = moment + datetime.timedelta(0,10**9)
    return new_date
