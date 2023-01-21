import datetime
#Given a moment, determine the moment that would be after a gigasecond has passed.
#A gigasecond is 10^9 (1,000,000,000) seconds.
def add(moment):
    new_date = moment + datetime.timedelta(0,10**9)
    return new_date
