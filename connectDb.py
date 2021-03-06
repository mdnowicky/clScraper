from Logger import Logger
import pyodbc

conn_str = (
    "DRIVER={PostgreSQL ODBC Driver(UNICODE)};"
    "DATABASE=clScraper;"
    "UID=postgres;"
    "PWD=postgres;"
    "SERVER=localhost;"
    "PORT=5432;"
    )

def connectDb():
    pyodbc.drivers()
    try:
        #Logger.writeAndPrintLine("Connecting database...", 0)
        return pyodbc.connect(conn_str)
    except:
        Logger.writeAndPrintLine('Unable to connect to the database.', 3)


def disconnectDb(cnxn):
    cnxn.close()