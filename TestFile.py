import datetime
#print('Hello World!')
todayDate = datetime.datetime.today()
userName = input('What is your name? ')
if userName.lower() == 'andrew gage':
    userName = 'Hemmorgage'
elif userName.lower() == 'ben abayev' or 'benjamin abayev':
    userName = 'Denis(on) deez nuts'
elif userName.lower() == 'elisha horowitz':
    userName = 'Elish Navidad'
print(f'Hello {userName}, today is {todayDate:%A, %B %d, %Y}!')