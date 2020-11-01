import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**please Drink a Water..!!!!",
            message = "Water is good for health so please do drink it...!",
            app_icon = "/home/husenbeg/notifier/glass.ico",
            timeout = 10
        )
        time.sleep(6)