import datetime

class Clock():

    time = None
    minutes_elapsed = 0
    seconds_elapsed = 0

    def __init__(self):
        self.time = datetime.datetime.now().timestamp()


    def reset(self):
        self.minutes_elapsed = 0
        self.seconds_elapsed = 0
        self.time = datetime.datetime.now().timestamp()


    def update_time(self):
        if datetime.datetime.now().timestamp() - self.time > 1:
            self.seconds_elapsed +=1

            if(self.seconds_elapsed == 60):
                self.seconds_elapsed = 0
                self.minutes_elapsed += 1

            self.time = datetime.datetime.now().timestamp()