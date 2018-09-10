import sqlite3
import datetime

def getTimeStamp():
    return str(datetime.datetime.now()).split('.')[0]



def pushData(vSEARCH, vTIMESTAMP, vDEAL):
    conn = sqlite3.connect('search.db')
    conn.execute("INSERT INTO COMPANY (SEARCH, TIMESTAMP, DEAL ) VALUES ( vSEARCH, vTIMESTAMP, vDEAL )") 
    conn.commit()
    conn.close()
    
def getDealPromo():
    return pass

def  createTable():
    conn = sqlite3.connect('search.db')
    #
    #
    conn.close()
    
    


conn = sqlite3.connect('search.db')
print ("Opened database successfully")


conn.execute('''CREATE TABLE IF NOT EXISTS searchRequests
       (SEARCH           TEXT    NOT NULL,
       TIMESTAMP            TEXT     NOT NULL,
       DEAL       TEXT
       );''')
print ("Table created successfully")

conn.close()




