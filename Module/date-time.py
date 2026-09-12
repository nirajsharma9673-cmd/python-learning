import datetime as d

my_date = d.date(2016, 9, 30) # creating a date 
print(my_date)

today = d.date.today()
print(today) # for today date

#to get day of week we have two mathods 
print(today.weekday()) # monday as 0, sunday as 6
print(today.isoweekday()) # monday as 1, sunday as 7

# timedelta it stores the duration betwenn two days and time
t = d.timedelta(days =7)
# if i want 7 days after date i cn simply add them 
print(today+t)
# if i want before 7 days date 
print(today - t)
# date2 = date1 +/- timedelta
# timedelta  = date 1 +/- date 2
t2 = today - my_date # timedelta we have created
print(t2)