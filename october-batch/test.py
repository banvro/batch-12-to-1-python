# from datetime import date

# zx = date.today()

# print(zx)

from datetime import datetime

# zx = datetime.now()

# yr = zx.minute

# print(yr)

# zx = "2000-07-11"
# new_date = datetime.strptime(zx, "%y-%m-%d")


from datetime import datetime

# date_str = '2023-02-28'
#  Example 1: Integer instead of string
date_int = "20230301"
date_obj = datetime.strptime(date_int, '%Y%m%d')

print(date_obj)