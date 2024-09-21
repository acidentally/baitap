# <ins> Question 3: </ins>
## Code a clock function which takes in the current hour and minute, and a number as an argument.
## The hour and minute describes the current time and the number is in minutes
## The function then prints out the time which is 'number' minutes after the given time (hour, minute)

## Example : time_past(8, 30, 30) --> (9, 0)
## Exaplanation : The current time is 8h30, and we have to fast forward 30 minutes, making it 9 o'clock
## Hence (9, 0) as in 9 hours and 0 minutes

def time_past(hour, minute, minute_past) :
    current_time = hour * 60 + minute + minute_past
    current_hour = (current_time // 60) % 24
    current_minute = current_time % 60

    print((current_hour, current_minute))

time_past(8, 30, 30)