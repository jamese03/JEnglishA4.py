#James English 
#Assignment 4 

import sys
import os
import re

print("Running Script")
print("")

clear = open('SearchOutput.txt', 'w')
clear.write("")
clear.close()



if len(sys.argv) < 3:
  print("Not enough arguments entered")
  print("Script exiting")
  sys.exit()


#Checking to see if user chose -v option
if sys.argv[1] == '-v':
  print("-v argument entered")
  print("")
#If -v is entered, all arguments will be shifted one
  count=0
  pattern = sys.argv[2]
  file = sys.argv[3:]
  if len(sys.argv) > 3:
    print("Correct syntax")
  else:
    print("Incorrect Syntax for -v argument script exiting")
    sys.exit()
  print("")
  for x in file:
    if os.path.isfile(x):
      print("The file", x, "exists!")
    else: 
      print("The file", x, "doesn't exist!")
      sys.exit()
      print("")
  print("")
  for x in file:
   matches=[]
   for x in (sys.argv[3], "r"):
     if re.findall(pattern, x):
       count = count + len(re.findall(pattern,x))
       matches.append(x)


   print(sys.argv[3] + " contains " + pattern + " " + str(count) + " times")
   output = open("SearchOutput.txt", "a")
   print(sys.argv[3] + " contains " + pattern + " " + str(count) + " times", file=output)       
   print(*matches, sep='\r', file=output)
   sys.argv = sys.argv[1:]

 
#The else will run when the 2nd argument isn't -v
else:
  pattern = sys.argv[1]
  file = sys.argv[2:]
  array = [file]
  if len(sys.argv) > 2:
    print("Correct syntax used")
  print("")
  for x in file:
    if os.path.isfile(x):
      print("The file", x, "exists")
    else:
      print("The file", x, "doesn't exist")
      sys.exit()
      print("")
  print("")
  count = 0
  open('SearchOutput.txt', 'w').close()
  for x in file:
    searchfile = open(x, "r")
    for line in searchfile:
      if pattern in line:
        count += 1
    output = open('SearchOutput.txt', 'a')
    output.write("%s contains %s %s times \n" % (x, pattern, count))
    output.close()
    searchfile.close()
  print("Total number of matches is ", count)
  print("See SearchOutput.txt for more details")

