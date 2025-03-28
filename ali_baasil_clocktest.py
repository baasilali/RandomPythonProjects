# Baasil ALi
# 12 / 14 / 2022
#
# This program will create a clock that outputs both military
# and AM/PM outputs.

import re

class Clock:
    def __init__(self, time):
        self.time = time
        # Extract hours, minutes and AM/PM from time string
        if "a.m." in time or "p.m." in time:
            # AM/PM time
            (hours, minutes, am_pm) = re.split(r"\s+", time)
            (hours, minutes) = hours.split(":")
            if am_pm.lower() == "p.m.":
                if hours == "12":
                    hours = "12"
                else:
                    hours = str(int(hours) + 12)
            else:
                if hours == "12":
                    hours = "00"
        else:
            # Military time
            (hours, minutes) = time.split(":")
        self.hours = int(hours)
        self.minutes = int(minutes)

    def __add__(self, other):
        # Add two clock objects
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours + minutes // 60
        minutes %= 60
        hours %= 24
        return Clock("{:02d}:{:02d}".format(hours, minutes))

    def __sub__(self, other):
        # Subtract two clock objects
        minutes = self.minutes - other.minutes
        hours = self.hours - other.hours + minutes // 60
        minutes %= 60
        hours %= 24
        return Clock("{:02d}:{:02d}".format(hours, minutes))

    def __str__(self):
        return self.time



def main():
    while True:
        # Prompt user for time inputs
        time = input("Enter military time and AM/PM time, separated by a comma, or just press ENTER to quit: ")
        if not time:
            # Quit if user didn't enter anything
            break
        (time1, time2) = time.split(",")
        # Create clock objects
        clock1 = Clock(time1)
        clock2 = Clock(time2)
        print("You entered", clock1, "and", clock2)
        # Add and subtract clock objects
        sum_time = clock1 + clock2
        diff_time = clock1 - clock2
        print("The sum of the times is", sum_time)
        print("The difference of the times is", diff_time)

main()
