import os
userinput = input("Please enter your Path with double backslashes ")
os.remove(userinput)
print(f"File '{userinput}' was successfully removed")