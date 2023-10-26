

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) or (year % 4000 == 0):
        return True
    return False



def test_if_year_divided_by_4_but_not_by_100_is_leap_year():
    assert isLeapYear(2004) == True
    assert isLeapYear(2012) == True
    assert isLeapYear(2024) == True


def test_year_divided_by_400_is_leap_year():
    assert isLeapYear(1600) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(2400) == True


def test_year_not_divided_by_4_is_not_leap_year():
    assert isLeapYear(2006) == False
    assert isLeapYear(2018) == False


def test_year_divided_by_100_but_not_by_400_is_not_leap_year():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False


def test_year_divided_by_4_and_4000_is_leap_year():
    assert isLeapYear(4000) == True
    assert isLeapYear(8000) == True