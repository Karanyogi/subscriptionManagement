import time

from notifyUser import notifyUsers
# to notify the user if current plan is about to end

window = 3

while True:
    startTime = int(time.time())
    notifyUsers(window)
    endTime = int(time.time())
    diff = endTime - startTime
    # calculate time for above process then do one day's time - time taken in run
    # this way we are running cron in every 24hr
    if diff< 24*60*60:
        time.sleep(24*60*60-diff)