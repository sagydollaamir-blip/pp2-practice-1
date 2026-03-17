#Example 1: Remove the file "demofile.txt":
import os
os.remove("demofile.txt")

#Exapmle 2: Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#Example 3: Remove the folder "myfolder":
import os
os.rmdir("myfolder")