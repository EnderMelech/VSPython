import datetime
#print('Hello World!')
todayDate = datetime.datetime.today()
userName = input('What is your name? ')
if userName.lower() == 'andrew gage':
    userName = 'Hemmorgage'
elif userName.lower() == 'ben abayev' or userName.lower() == 'benjamin abayev':
    userName = 'Denis'
elif userName.lower() == 'elisha horowitz':
    userName = 'Hor'
elif userName.lower() == 'ethan weiss':
    userName = 'my lord and savior'
print(f'Hello {userName}, today is {todayDate:%A, %B %d, %Y}!')