import datetime
#print('Hello World!')
todayDate = datetime.datetime.today()
userName = input('What is your name? ')
print(f'Hello {userName}, today is {todayDate:%A, %B %d, %Y}!')