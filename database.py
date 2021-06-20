#!/usr/bin/python

"""
   - Functions :
      @insertData() -> add new data to a Database :) 
      @getAllData() -> Get All Data From Database :)
      @getRandomdata() -> Get Random Data From Database :)
      @insertDataQuery() -> Query
      @getAllDataQuery() -> Query
      @getRandomQuery()  -> Query
      
   - Database :
      - Name : Azkar.db
        - Table : IslamBot
                   - cloums:
                     - id -> integer
                     - Azkar -> text
"""
import sqlite3 as db 
import random 

try:
    ConnectionDatabase = db.connect("db/Azkar.db")
    CursorDatabase = ConnectionDatabase.cursor()
    CursorDatabase.execute('''CREATE TABLE IF NOT EXISTS IslamicBot (
                                id INTEGER PRIMARY KEY,
                                Azkar TEXT NOT NULL);''')
    # CursorDatabase.execute("select Azkar from IslamBot order by Random() LIMIT 1 * 2 ;")
    # Fetch = CursorDatabase.fetchone()
    # print(Fetch)
except Exception as Error: 
       raise Error

""" - 'insert' Query -> add new data to a Database """
def insertDataQuery(Data):
    return """INSERT INTO 'IslamicBot' (Azkar)  VALUES ('""" + Data + """');"""

""" 'Select' Query -> Get All Data """
def getAllDataQuery():
    return """select * from IslamicBot;"""

""" 'Select' Query -> Get Random Data """
def getRandomQuery():
    return """ select Azkar from 'IslamicBot' order by Random() LIMIT 1"""


"""
  @func : insertData
  @param : Data -> str
  @decription : -> add new data to a database 
"""
def insertData(Data):
    return CursorDatabase.execute(insertDataQuery(Data))

"""
  @func : -> getAllData
  @param : -> None
  @decription: -> Get All Data From Database :)
"""
def getAllData():
    executeQuery = CursorDatabase.execute(getAllDataQuery())
    return CursorDatabase.fetchall()

#getAllData()

"""
  @func: -> getRandomdata
  @param: -> None
  @decription: -> Get Random Data From Database :)
"""
def getRandomdata():
    CursorDatabase.execute(getRandomQuery())
    Fetch = CursorDatabase.fetchone()
    return Fetch
# insertData("استغفرالله")
# print(getAllData())
 
