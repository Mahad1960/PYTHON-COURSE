import time # This is built-in module.
text=time.strftime("%H:%M:%S") # You can also use here '' these commas.
print("TIME:",text)
hour=int(time.strftime("%H"))
if(hour>=5 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<17):
    print("Good Afternoon!")
elif(hour>=17 and hour<19):
    print("Good Evening!") 
else:
    print("Good Night!")