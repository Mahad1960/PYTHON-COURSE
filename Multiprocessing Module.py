# In Parallel means, running multiple things at the same time, instead of one after the other.
import concurrent.futures  # Only "concurrent" will not work here.
import multiprocessing     # For 1st Method.
import concurrent          # For 2nd Method
import os
import requests
# You can use this code for any document like jpg,png,pdf etc.
def download_file(url,name):
    response=requests.get(url)
    if(not os.path.exists("MULTIPROCESSING FOLDER")):  # This checks if data is created or not if not it will create.
       os.mkdir("MULTIPROCESSING FOLDER")
    open(f"MULTIPROCESSING FOLDER/{name}.jpg","wb").write(response.content)  # If there is any other file just make changes in this line.
# "wb" means "write binary" mode, needed for images or any non-text files.
# ".write(response.content)", this writes the binary image data into the file.
# The below line is important for "Multiprocessing".
# 1st METHOD:
# if __name__ == "__main__":  # Without this guard, your program may crash, hang, or restart processes infinitely on Windows.
#     url="https://picsum.photos/200/300"
#     x=[]
#     for i in range(1,6):  # Every time i run it, new "jpj" file will appear. 
#         a=multiprocessing.Process(target=download_file,args=[url,i])  # It will run your program in parallel.
#         a.start() # "a.start" launches the process immediately.
#         x.append(a)
#     for p in x:
#         p.join()  # "join" makes sure the main program waits until all processes are finished.
# 2nd METHOD:
if __name__ == "__main__":  
    url="https://picsum.photos/200/300"
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(1,6)]
        l2=[i for i in range(1,6)]
        result=executor.map(download_file,l1,l2)