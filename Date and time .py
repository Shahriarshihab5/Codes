import datetime

a=datetime.datetime.now()
print(a)

b=datetime.date.today()
print(b)

print(a.strftime("%a"))  # %a :Weekday,short version
print(a.strftime("%A"))  # %A :Weekdat,Full version
print(a.strftime("%w"))  # %w :Weekday as a number 0-6,0 is Sunday
print(a.strftime("%W"))  #%d  :Day of month 01-31
print(a.strftime("%b"))  #%b  :month name short version
print(a.strftime("%B"))  #%B  :month name full version
print(a.strftime("%m"))  #%m  :month name as number
print(a.strftime("%y"))  #%y  :year short version,without century
print(a.strftime("%Y"))  #%Y  :year,full version
print(a.strftime("%H"))  #%H  :Hour 00-23
