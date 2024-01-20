import sqlite3
import os
from dotenv import load_dotenv
class DatabaseConnector:
    def __init__(self):
        load_dotenv()
        self.databaseFile = os.getenv("DATABASE")
        
    def Connect(self):
        try:
            conn = sqlite3.connect(self.databaseFile)
            print("DB connect success")
            return conn
            
        except sqlite3.Error as e:
            print("SQLite error:", e)
            return None
        
    def GetDiscordToken(self):
        conn = self.Connect();
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("select value from Secrets where name = 'DiscordToken';")
                print(cursor)
                token = cursor.fetchone()[0]
                return token
            except sqlite3.Error as e:
                print("SQLite error: ", e)
                return None
            finally:
                conn.close()
        