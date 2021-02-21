#!/usr/bin/python
from database import *
import json
import argparse
import requests

"""
   - Functions:

      :@loadString
      :@getTypeStorage
      :@getTokens
      :@TelegramAPI
      :@Args
      
"""
Argparser = argparse.ArgumentParser()

try:
    Config = open("config.json","r").read()
except:
    print( "[-] Error -> We Did Not Find -> 'config.json' [-] " )


""" - Load String from File """
def loadString():
    return json.loads(Config)


""" 
   @func: -> getTypeStorage
   @param: -> None
   @decription: -> Get Types of Storge  
"""
def getTypeStorage():
    if loadString()['Type'] == 'db':
       return True
    else:
       return False


"""
   @func:  -> getTokens()
   @param: -> None
   @description: get token from 'config.js' to deal with telegram api 
"""
def getTokens():
    if loadString()['api_token']:
       return loadString()['api_token'] , loadString()['chat_id']
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
    Argparser.add_argument('-add',help="-a islamicazkar.txt")
    Argparser.add_argument('-get', help="-get start ")
    Argparser.add_argument('-random','--random' , help=" --random start ")
    Argparser.add_argument('-sendmessage','--sendmessage' , help="'--sendmessage start' | we will send message to chat id  ")
    return Argparser.parse_args()



def main():
    try:
       getArgparser = Args()
       if getArgparser.add or getArgparser.add == "file":            
          ReadingFile = open("islamicazkar.txt" , "r" , encoding="UTF-8").read()
          
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
               with open("db/IslamicAzkar.json" , "r" , encoding="UTF-8") as ISLAMICAZKAR:
                    READINGISLAMICAZKAR = ISLAMICAZKAR.read()
                    RandomNumber = random.randint( 0 , 274 ) # You Should Change this number if you add new data
                    JSONLOADS = json.loads(READINGISLAMICAZKAR)
                    categoryAzkar = JSONLOADS[RandomNumber]['category']
                    zekrionAzkar = JSONLOADS[RandomNumber]['zekr']
                    PatternWords = f"{categoryAzkar}\n\n{zekrionAzkar}" 
                    TelegramAPI(getTokens()[0] , getTokens()[1] , PatternWords)
       elif getArgparser.get:
            print(getAllData())

    except:
       print(" [-] Try again [-] ")

if __name__ == '__main__':
   main()

