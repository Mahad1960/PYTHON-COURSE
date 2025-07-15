import os
files=os.listdir("CLUTTERED FOLDER")  # You can also write "." instead of "CLUTTERED FOLDER" which means the current directory.
i=1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"CLUTTERED FOLDER/{file}",f"CLUTTERED FOLDER/{i}.jpg")
        i+=1