from flask import Flask, request

from dbManager.dbOperations import (getLastestPlanEndDate,
 createNewSusbcriptionPlan,
 getAllSubscriptions)

app = Flask(__name__)

# here authentication can be used in real case

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # get subscription for this user, sorted on end date, get the last element
    # if end_date of latest subscription is < today's date we can start the subscription today
    # else we will add the start date = end date + 1 and end date = new start date + subscriptionPlan.valadity
    
    # in current implementation we don't have to run cron job to update subscription
    # we will just fetch the latest subscription and check if today's date falling between start and end date
    # if this is future subscription we can find current subs using --> today's date>start date and today's date<start date
    try:
        data = request.json
        userId = data["userId"]
        planId = data["planId"]
        latestPlanEndDate = getLastestPlanEndDate(userId)
        successData = createNewSusbcriptionPlan(userId, planId, latestPlanEndDate)
        print(successData)
        response = {
            "responseStatus" : "success",
            "successData" : successData
        }
    except Exception as e:
        print("SERVER ERROR /subscribe \
        Exception during request handling \
        Exception: " + str(e))
        # add alert for notification
        response = {
            "responseStatus" : "fail",
            "message" : "Something went wrong, we are working on it!"
        }
    return response

@app.route('/subscription_list', methods=['POST'])
def subscriptionList():
    try:
        data = request.json
        userId = data["userId"]
        successData = getAllSubscriptions(userId)
        response = {
            "responseStatus" : "success",
            "successData" : successData
        }
    except Exception as e:
        print("SERVER ERROR /subscribe \
        Exception during request handling \
        Exception: " + str(e))
        # add alert for notification
        response = {
            "responseStatus" : "fail",
            "message" : "Something went wrong, we are working on it!"
        }
    return response


if __name__ == '__main__':
    app.run()
