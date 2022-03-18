import calendar
from datetime import time
from datetime import date
from datetime import datetime
from zoneinfo import ZoneInfo


def show_time():
    mytime = time(23, 32, 3)
    print(mytime)
    print(mytime.hour)
    print(mytime.minute)
    print(mytime.second)


def show_date():
    mydate = date.today()
    print(mydate)
    print(mydate.ctime())
    print(mydate.day)
    print(mydate.month)
    print(mydate.year)


def show_datetime():
    print(f"Local time: \t\t{datetime.now()}")
    print(f"Local time in UTC: \t{datetime.utcnow()}")
    print(f"DOB: \t\t\t\t{datetime(2019, 2, 19, 11, 35)}")        # time in UTC

    # UTC time difference
    print(f"Time in LA: \t\t"
          f"{datetime(2019, 2, 19, 11, 35, tzinfo=ZoneInfo('America/Los_Angeles'))}")


def time_diff(start, end):
    age = end - start

    days_in_year = 365             # TODO:
    days_in_month = calendar.monthrange(date.today().year,
                                        date.today().month - 1)[1]

    print(f"{age.days // days_in_year} years, "
          f"{age.days % days_in_year // days_in_month} months "
          f"{(age.days % days_in_year) % days_in_month} days "
          f"{age.seconds // 60 // 60} hours "
          f"{(age.seconds // 60) % 60} mins and "
          f"{age.seconds % 60} sec"
          )
# o/p on 18Mar 01h05 - 3 years, 0 months 27 days 13 hours 30 mins and 11 sec


if __name__ == '__main__':
    # show_time()
    # show_date()
    # show_datetime()

    dob = datetime(2019, 2, 19, 11, 35)         # Sweethearts DOB
    time_diff(dob, datetime.now())
    dob = datetime(1981, 10, 15, 12, 00)        # Mine
    time_diff(dob, datetime.now())
    dob = datetime(1988, 10, 1, 12, 00)         # Hunny
    time_diff(dob, datetime.now())

