from currency_converter import CurrencyConverter
from datetime import date
from datetime import datetime

c = CurrencyConverter()
select_currency = ""

def compare_dates():
    currency_date1 = input("Please input 1st date. (YYYY,MM,DD): ")
    currency_date2 = input("Please input 2nd date. (YYYY,MM,DD): ")
    y1, m1, d1 = map(int, currency_date1.split(','))
    date1_obj = date(y1, m1, d1)

    y2, m2, d2 = map(int, currency_date2.split(','))
    date2_obj = date(y2, m2, d2)

    compare_result = (c.convert(100,select_currency,date = date1_obj))-(c.convert(100,select_currency,date = date2_obj))
    if compare_result > 0:
        print(f"The 1st date currency is more than 2nd date about {compare_result:.2f}" ,select_currency,"Per 100" , select_currency)
    elif compare_result == 0:
        print("Both date currency are the same.")
    else:
        print(f"The 2nd date currency is more than 1st date about {abs(compare_result):.2f}" ,select_currency,"Per 100" , select_currency)


def compare_last():
    currency_date = input("Please input the date you want to compare. (YYYY,MM,DD): ")
    y, m, d = map(int, currency_date.split(','))
    selected_date_obj = date(y, m, d)

    compare_result = (c.convert(100,select_currency,date = selected_date_obj))-(c.convert(100,select_currency))
    if compare_result > 0:
        print(f"The selected date currency is more than lastest rate about {compare_result:.2f}",select_currency,"Per 100" , select_currency)
    elif compare_result == 0:
        print("Both date currency are the same.")
    else:
        print(f"Lastest rate is more than selected date about {abs(compare_result):.2f}",select_currency,"Per 100" , select_currency)



print("Welcome ! Please enter your currency.")
select_currency = (input("Your currency : ")).upper()
print("How do you want to compare about currency? ")
print("1. Compare between two selected dates.")
print("2. Compare between selected date and lastest rate.")
select_compare = int(input("Please input your selection : "))

if select_compare == 1:
    compare_dates()
elif select_compare == 2:
    compare_last()

