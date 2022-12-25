import psycopg2

conn = None

def config():
    #ideally we should take these variables from env
    configs = {
        "database":"postgres",
        "host":"localhost",
        "user":"",
        "password":"",
        "port":"5432"
    }
    return configs

def connect():
    print("connecting to db...")
    global conn
    try:
        if conn:
            return conn.cursor()
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        conn.autocommit = True
        return cur
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
