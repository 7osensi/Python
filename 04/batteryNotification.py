#           Author: Hussein Mohamed 
#           Description: Pyhton script show battery notification

import psutil
from plyer import notification

battery = psutil.sensors_battery()

if battery is not None:
    percentage = battery.percent

    notification_title = "Battery Percentage"
    notification_message = f"The current battery percentage is {percentage}%"

    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10
    )
else:
    print("Battery information not available.")

