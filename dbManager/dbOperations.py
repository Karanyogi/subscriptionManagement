import datetime

from dbManager.dbConnector import connect
from datetime import timedelta

def getLastestPlanEndDate(userId):
    dbQuery = "select enddate from public.subscription \
     where enddate>= '" + str(datetime.date.today()) + "' order \
    by enddate desc limit 1;"
    curOBJ = connect()
    curOBJ.execute(dbQuery)
    data = curOBJ.fetchall()
    if len(data) != 0:
        return data[0][0]
    return None

def getPlanValadity(planId):
    dbQuery = "select valadity from public.subscriptionname \
    where id = " + str(planId) + ";"
    curOBJ = connect()
    curOBJ.execute(dbQuery)
    data = curOBJ.fetchall()
    return data[0][0]

def createNewSusbcriptionPlan(userId, planId, lastPlanEndDate):
    planValadity = getPlanValadity(planId)
    planStartDate = datetime.date.today()
    if lastPlanEndDate:
        planStartDate = lastPlanEndDate + timedelta(days = 1)
    dbQuery = "insert into public.subscription(startdate, enddate, \
     subscriptionnamefkey, userfkey) values('" + str(planStartDate) +"',  \
      '" + str(planStartDate + timedelta(days = planValadity))  + "', \
    " + str(planId) + ", " + str(userId) + ");"
    curOBJ = connect()
    curOBJ.execute(dbQuery)
    return {"startdate": str(planStartDate),
    "enddate": str(planStartDate + timedelta(days = planValadity)),
    "planId": planId,
    "userId": userId
    }

def getAllSubscriptions(userId):
    # get all subscriptions for this user, we will have to use subscriptionName(plan) table
    # to get valadity and plan name(if we want to show on UI), we can use foreignkey constraint for this
    dbQuery = "select a.planname, a.valadity, b.startdate, b.enddate from public.subscription as b \
    inner join public.subscriptionname as a on(a.id = b.subscriptionnamefkey) \
    where b.userfkey = " + str(userId) + ";"
    curOBJ = connect()
    curOBJ.execute(dbQuery)
    data = curOBJ.fetchall()
    finalList = []
    for item in data:
        finalList.append(
            {
                'planName': item[0],
                'valadity': item[1],
                'startDate': item[2],
                'endDate': item[3]
            }
        )
    return finalList

def getEndingSubscriptions(window):
    dbQuery = "select userfkey from public.subscription \
    where enddate<= '" + str(datetime.date.today() + timedelta(days = window)) + "' \
    and enddate>= '" + str(datetime.date.today()) + "';"
    curOBJ = connect()
    curOBJ.execute(dbQuery)
    data = curOBJ.fetchall()
    userKeyList = []
    for item in data:
        userKeyList.append(item[0])
    return userKeyList