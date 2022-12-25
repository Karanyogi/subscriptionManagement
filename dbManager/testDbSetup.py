from dbManager.dbConnector import connect

def testConnection():
    currObj = connect()
    currObj.execute('select * from public.user')
    print(currObj.fetchall())
    print("connected....")