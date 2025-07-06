import os
if(not os.path.exists("Data")):  # This checks if data is created or not if not it will create.
  os.mkdir("Data")
# for i in range(1,4):           # This will create folders inside Data.
#   os.mkdir(f"Data/Day {i}")
# for i in range(1,4):
#   os.rename(f"Data/Day {i}",f"Data/Tutorial {i}")
folders=os.listdir("Data")        # It will print folders name.
# print(folders)                  # You can use for loop or this statement for printing folders.
for i in folders:  
  print(i)                        # It will print folders name.
  print(os.listdir(f"Data/{i}"))  # It will print file name inside folders. "Data" is showing path here.
print("DIRECTORY:",os.getcwd())   # It will show you the path of your directory.
os.chdir("/Windows")              # It is used to change the directory.
print("CHANGED DIRECTORY:",os.getcwd())
# After changing directory no file name inside folders will be viewed.
for i in folders:  
  print(i)                        
  print(os.listdir(f"Data/{i}"))  # This will not work because of changing directory.
# You can study further functionalities on GOOGLE.