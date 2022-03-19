import time
from plyer import notification
## plyer is a module used to notify a notification in python
## it can be installed via the command :-
## pip install plyer
while True:
    if __name__=='__main__':
        notification.notify(title='Drink water',
                            message='The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.',
                            app_icon='glass.ico')
        time.sleep(60*60)## Sleeping the program for 1 hr to add a delay of 1 hr
##        pythonw main.py runs python in background
