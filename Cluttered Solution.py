import os
import shutil
files=os.listdir("CLUTTERED FOLDER")  # You can also write "." instead of "CLUTTERED FOLDER" which means the current directory.
i=1
for file in files:
    if file.endswith(".jpg"):
        old_path=os.path.join("CLUTTERED FOLDER",file)
        new_path=os.path.join("DISCIPLINED FOLDER",f"{i}.jpg")
        # If i write "os.rename" below , the new folder will become new as you want but the other folder will lose it's material.
        shutil.copy(old_path,new_path)  # This will copy files in new folder and the other folder remains same.
        i+=1