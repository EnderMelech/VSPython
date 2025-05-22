print('Hello World!')

variable='Hello'
print(f'{variable} World!')

import datetime
todayDate = datetime.datetime.today()
userName = input('What is your name? ')
print(f'Hello {userName}, today is {todayDate:%A, %B %d, %Y}!')

    # Open function to open the file "MyFile1.txt"
    # (same directory) in append mode (able to write in it) and
file1 = open("MyFile1.txt","a")
    # store its reference in the variable file1
    # and "MyFile2.txt" in D:\Text in file2 (w+ means you can read and write in it)
file2 = open(r"D:\Text\MyFile2.txt","w+")

File_object.read([n])