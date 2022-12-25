from dbManager.dbOperations import getEndingSubscriptions

def sendNotificationToUser(userKey):
    #here notification sending code will go
    print("sending notification for subscription ending to user: " + str(userKey))
    return

def notifyUsers(window):
    # we will fetch all the subcriptions those are
    # about to end in some window(let's say 3 days)
    # then we will send notification to all these users
    subsEndingUserList = getEndingSubscriptions(window)
    for userKey in subsEndingUserList:
        sendNotificationToUser(userKey)
