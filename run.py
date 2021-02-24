#!/usr/bin/python
from database import *
import json
import argparse
import requests
import sys
from crontab import CronTab
from pathlib import Path

""" Check which version of python """
if sys.version_info < ( 3 , 0 ) :
    sys.stdout.write(" [ - ] You should have python-version 3.x [ - ] \n")
    sys.exit(1)

def getPath():
    return str(Path(__file__).absolute().parent)

"""
   - Functions:
      :@loadStrings
      :@getTypeStorage
      :@getTokens
      :@TelegramAPI
      :@Args
      
"""
Argparser = argparse.ArgumentParser()

try:
    ConfigPath = getPath() + "/config.json"
    Config = open(ConfigPath,"r").read()
except FileNotFoundError:
    print( "[-] Error -> We Did Not Find -> 'config.json' [-] " )


""" - Load String from Json File """
def loadStrings():
    return json.loads(Config)


""" 
   @func: -> getTypeStorage
   @param: -> None
   @decription: -> Get Types of Storge  
"""
def getTypeStorage():
    if loadStrings()['Type'] == 'db':
       return True
    else:
       return False


"""
   @func:  -> getTokens()
   @param: -> None
   @description: get token from 'config.js' to deal with telegram api 
"""
def getTokens():
    if loadStrings()['api_token']:
       return loadStrings()['api_token'] , loadStrings()['chat_id']
    else: 
       return "[-] Error -> We Did Not Find -> 'API Token' [-] "


""" - Deal With Telegram API """
"""
   @func: TelegramAPI
   @param: api_token -> str , 
           chat_id -> str & int ,
           message -> str
"""
def TelegramAPI( api_token , chat_id , message ):
    api_telegram = "https://api.telegram.org/bot" + api_token + "/sendMessage?chat_id="+ str(chat_id) + "&text=" + str(message)
    sendRequest = requests.get(api_telegram).text
    if sendRequest:return True
    


""" argparse ->  Argparser"""
def Args():
    Argparser.add_argument('-add',help=" -> add new data in database ")
    Argparser.add_argument('-get', help=" -> get all data from database ")
    Argparser.add_argument('-random' , help=" -> get random data from database ")
    Argparser.add_argument('-sendmessage' , help=" -> we will send message to chat id  ")
    Argparser.add_argument('-cronjob' , help=" -> What is cronjob -> used for scheduling tasks  (-cronjob python2) or (-cronjob python3)")
    return Argparser.parse_args()



def main():
    try:
       getArgparser = Args()
       if getArgparser.add or getArgparser.add == "file":  

          IslamicazkarPath = getPath() + "/islamicazkar.txt"          
          ReadingFile = open(IslamicazkarPath , "r" , encoding="UTF-8").read()
          
          if insertData(ReadingFile):
             ConnectionDatabase.commit()
             print(" [+] We insert The Azkar to database [+] ")
          else:
             print(" [-] Error -> Remove File Or Change Permissions   :( [-] ")   

       elif getArgparser.random:
            print(getRandomdata())
            
       elif getArgparser.sendmessage:
            if getTypeStorage():
               TelegramAPI(getTokens()[0] , getTokens()[1] , getRandomdata()[0])

            else:
               IslamicJsonPath = getPath() + "/db/IslamicAzkar.json" 
               with open(IslamicJsonPath , "r" , encoding="UTF-8") as ISLAMICAZKAR:
                    READINGISLAMICAZKAR = ISLAMICAZKAR.read()
                    RandomNumber = random.randint( 0 , 274 ) # You Should Change this number if you add new data
                    JSONLOADS = json.loads(READINGISLAMICAZKAR)
                    categoryAzkar = JSONLOADS[RandomNumber]['category']
                    zekrionAzkar = JSONLOADS[RandomNumber]['zekr']
                    PatternWords = f"[ - {categoryAzkar} - ]\n{zekrionAzkar}" 
                    TelegramAPI(getTokens()[0] , getTokens()[1] , PatternWords)

       elif getArgparser.get:
            print(getAllData())
       
       elif getArgparser.cronjob:
            CronJob = CronTab(user='root')
            Job = CronJob.new( command = "/usr/bin/python3 " + getPath() + "/run.py -sendmessage start")
            Job.hour.every(5)
            CronJob.write()

    except:
       print(" [-] Try again [-] ")

if __name__ == '__main__':
   main()
