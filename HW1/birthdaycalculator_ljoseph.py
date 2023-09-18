# Lohgan Joseph
# ID: 2038027

# Input the current day
print('Birthday Calculator\nCurrent day')
m1 = int(input('Month: '))
d1 = int(input('Day: '))
y1 = int(input('Year: '))

# Input your birthday
print('Birthday')
m2 = int(input('Month: '))
d2 = int(input('Day: '))
y2 = int(input('Year: '))
years = y1-y2-1
if(m2<m1):
    years+=1
elif(m1==m2):
    if(d2<d1):
        years+=1
if(m1==m2 and d1==d2):#printing happy Birthday if current day is their birthda
    print('Happy Birthday')
print('You are '+str(years)+" years old.")