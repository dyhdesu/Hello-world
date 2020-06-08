# 引入日历模块
import calendar

# 输入指定年月
years = int(input("输入年份: "))
month = int(input("输入月份: "))

# 显示日历
print(calendar.month(years, month))