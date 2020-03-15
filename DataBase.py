import sqlite3


class DataBase:
    def __init__(self, databaseName):
        self.databaseName = databaseName
        self.conn = sqlite3.connect(self.databaseName)
        self.cursor = self.conn.cursor()  # allows python code to execute SQL statements
        print ('connected to... ', self.databaseName)

    def Cursor(self):
        return self.cursor

    def Conn(self):
        return self.conn
