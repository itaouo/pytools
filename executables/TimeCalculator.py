from datetime import datetime

from lib.TextColor import TextColor

class CalculateDifferenceTime:
    def execute(self):
        start_time_str = input("Enter the start time (HH:MM): ")
        end_time_str = input("Enter the end time (HH:MM): ")

        start_time = datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.strptime(end_time_str, "%H:%M")

        time_difference = end_time - start_time
        hours, minutes = divmod(time_difference.seconds, 3600)
        minutes = minutes // 60

        print(TextColor().green(f"The time difference is {hours} hours and {minutes} minutes."))

class CalculateTotalTime:
    def execute(self):
        input_time_str = "00:00"
        sum_hour = 0
        sum_minute = 0

        while True:
            input_time_str = input("Enter the time (HH:MM): ")
            try:
                start_time = datetime.strptime(input_time_str, "%H:%M")
            except Exception as e:
                break
            sum_minute += start_time.minute
            temp_hour = sum_minute // 60
            sum_minute %= 60
            sum_hour += start_time.hour + temp_hour

        print(TextColor().green(f"Total times are {sum_hour} hours {sum_minute} minutes.\n"))
