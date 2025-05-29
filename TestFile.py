# print('Hello World!')

# variable='Hello'
# print(f'{variable} World!')

# import datetime
# todayDate = datetime.datetime.today()
# userName = input('What is your name? ')
# print(f'Hello {userName}, today is {todayDate:%A, %B %d, %Y}!')

#     # Open function to open the file "MyFile1.txt"
#     # (same directory) in append mode (able to write in it) and
# file1 = open("MyFile1.txt","a")
#     # store its reference in the variable file1
#     # and "MyFile2.txt" in D:\Text in file2 (w+ means you can read and write in it)
# file2 = open(r"D:\Text\MyFile2.txt","w+")

# #File_object.read([n])

# for i in range(0,13,3):
#     print(i)
L=[]
print(L)
L.append(6)
print(L)
L.append(9)
print(L)
M=[10,11,8,6,9]
L.extend(M)
print(L)
for x in L:
    print(x)
print(L[0])
print(str(L)[1:-1])
for i in range(len(L)):
    print(L[i])
print(L)