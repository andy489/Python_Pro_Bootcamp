def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

year = 2025
print(f"{year} is {"not " if not is_leap_year(year) else ""}leap")
