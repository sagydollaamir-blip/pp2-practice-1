#Example 1: Open a file and read its content
f = open("demofile.txt")
print(f.read())

#Example 2: Using with statement to open a file
f = open("D:\\myfiles\welcome.txt")
print(f.read())

#Example 3: Using with statement to open a file
with open("demofile.txt") as f:
  print(f.read())

#Example 4: Reading a file line by line
f = open("demofile.txt")
print(f.readline())
f.close()

#Example 5: Reading a file line by line using with statement
with open("demofile.txt") as f:
  print(f.read(5))

#Example 6: Reading a file line by line using with statement
with open("demofile.txt") as f:
  print(f.readline())

#Example 7: Reading a file line by line using with statement
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

#Example 8: Looping through a file object
with open("demofile.txt") as f:
  for x in f:
    print(x)