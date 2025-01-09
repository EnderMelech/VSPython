# READING
readFile = open('testRead.txt','w') #for writing
L = ["This is New York City \n", "This is Jerusalem \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
readFile.write("Hello World! \n")
readFile.writelines(L)
readFile.close()  # to change file access modes

readFile = open("testRead.txt", "r+") #for reading and writing

print("Output of Read function is ")
print(readFile.read())
print()

# seek(n) takes the file handle to the nth byte from the beginning.
readFile.seek(0)

print("Output of Readline function is ")
print(readFile.readline())
print()

readFile.seek(0)

# To show difference between read and readline
print("Output of Read(12) function is ")
print(readFile.read(12))
print()

readFile.seek(0)

print("Output of Readline(12) function is ")
print(readFile.readline(12))

readFile.seek(0)
# readlines function
print("Output of Readlines function is ")
print(readFile.readlines())
print()
readFile.close()

# WRITING
writeFile = open("testWrite.txt", "w+")

for i in range(3): 
    name = input("Enter the name of the employee: ")
    writeFile.write(name)
    writeFile.write("\n")
writeFile.seek(0)
print(writeFile.read())
writeFile.close()

print("Data is written into the file.")

writeFile = open("testWrite.txt", "w+")
lst = []
for i in range(3):
    name = input("Enter the name of the employee: ")
    lst.append(name + '\n')

writeFile.writelines(lst)
writeFile.seek(0)
print(writeFile.read())
writeFile.close()
print("Data is written into the file.")