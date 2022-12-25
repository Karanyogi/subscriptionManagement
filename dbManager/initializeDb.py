from dbManager.dbConnector import connect

def initializeTestDB():
    # here I am not following single responsiblity principle since it is test project, ideally we should
    # create each table in separate function
    tableCreationQuery = "CREATE TABLE public.subscriptionName( \
    id SERIAL PRIMARY KEY, \
    planName varchar(32), \
    valadity int \
    );CREATE TABLE public.user( \
        id SERIAL PRIMARY KEY, \
        name varchar(32) \
    ); \
    CREATE TABLE public.subscription( \
        id SERIAL PRIMARY KEY, \
        subscriptionNameFKey int, \
        userFKey int, \
        CONSTRAINT subscriptionNameKey\
        FOREIGN KEY(subscriptionNameFKey)\
        REFERENCES public.subscriptionName(id)\
        ON DELETE SET NULL,\
        CONSTRAINT userKey\
        FOREIGN KEY(userFKey) \
        REFERENCES public.user(id)\
        ON DELETE SET NULL,\
        startDate date,\
        endDate date\
    );"
    currObj = connect()
    currObj.execute(tableCreationQuery)
