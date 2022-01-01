import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!",
            message ="Drinking Water Helps to Maintain the Balance of Body Fluids.",
            app_icon = "Iconsmind-Outline-Glass-Water.ico",
            timeout=12

        )
        time.sleep(60*60)