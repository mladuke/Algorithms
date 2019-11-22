from itertools import islice
from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)
# print every 100 days and 1 year from PYBITES_BORN

def gen_special_pybites_dates():

  from_date = PYBITES_BORN
  anv = PYBITES_BORN + timedelta(days=365)
  while True:
    if (from_date+timedelta(days=100) < anv):
          from_date = from_date + timedelta(days=100)
          yield from_date
    else:
          old_anv = anv
          anv = anv + timedelta(days=365)
          yield old_anv


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))

    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
                datetime(2019, 2, 27, 0, 0)]

    assert dates == expected


test_gen_special_pybites_dates()


''' def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days) '''