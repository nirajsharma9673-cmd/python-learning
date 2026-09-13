import datetime as d

#date 

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

print(t2.days) # it gives the date between them
print(t2.total_seconds()) # it gives the total seconds betn them

# time 
t = d.time()
print(t) # it does not have time zone thats why it gives 000

# syntext (hour , minutes, second, microsecond)
t1 = d.time(9,30,45,10000) # we have created a time 
print(t1) 
print(t1.hour) # it will print only hours 
print(t1.minute)

# if i want date and time togehter 
dt = d.datetime(2020,12,15,9,30,59,100)
print(dt)
print(dt.date()) # we  get onlyy date 
print(dt.time()) # we get only time 
# we cam also use there attribute
print(dt.year)

# we can craete time delta 
tdelta = d.timedelta(days=7)
print(tdelta) # 7 day

print(dt + tdelta)

# also use for h, m, s, ms
t1delta = d.timedelta(hours =45,minutes = 56,seconds = 56)
print(t1delta)

print(dt-t1delta)

print(d.datetime.today()) # it gives local time
print(d.datetime.now())# with this it gives output as per time zone

