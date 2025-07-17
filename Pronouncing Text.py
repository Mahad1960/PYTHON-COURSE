import win32com.client   # "pywin32" to install it.
# Create voice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")
name = input("Enter your name: ")
speaker.Speak(f"Hello,{name}")