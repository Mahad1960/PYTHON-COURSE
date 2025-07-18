from plyer import notification
import time
notification.notify(
    title="Notification!",
    message="Assalam-o-Alaikum Mahad, Kindly Drink Water!",
    app_name="My App",  # Windows uses the name of the executable file so, "PYTHON" will appear here instead of"My App".
    timeout=10          # Duration in seconds the notification stays on screen.
)
time.sleep(3600)      # It will print the msg after 1 hour.
# You can study "TASK SCHEDULER" if you want for further information.