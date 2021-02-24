<br />
<p align="center">
  <a href="https://t.me/IslamicAzkarBot">
    <img src="https://i.ibb.co/ZMp3t7P/51d3aa97c980e088ea4f42f1278fbd7c.png" alt="Logo" width="50%" height="50%">
  </a>

  <h3 align="center"> [ Islamic Azkar - Telegram Bot ] </h3>

  <p align="center">
    Islamic Azkar Telegram Bot , The bot sends "zikr" every 5 hours and if you add it to your group,it will send this kind of message every day
    <br />
    <a href="https://www.python.org/downloads/"><strong> Download Python »</strong></a>
    <br />
    <a href=""https://github.com/x0xman/IslamicAzkarBot/issues">Report Bug</a>
    <a href="https://github.com/x0xman/IslamicAzkarBot/pulls">Request Feature</a>
  </p>
</p>

## Islamic Azkar - Telegram Bot
[+] Islamic Azkar Telegram Bot , The bot sends "zikr" every 5 hours and if you add it to your group,it will send this kind of message every day 

## Installation :rocket:
   `git clone https://github.com/x0xman/IslamicAzkarBot.git`

## requirements :
   - python3
   - install libraries in python  : `pip install -r requirements.txt`
   - You must run this command : `python3 run.py -cronjob python3`
   - change `api_token` in `config.json` to your "token"
   - change `chat_id` in `config.json` to your "chat_id"
   - change `Type` in `config.json` to `json` or `db`
       ##### If you put it `db` we will deal with the database `db/Azkar.db` #####
        * deal with `db/Azkar.db` :
          ```
            {
              "api_token":"YourApiToken",
              "chat_id":"YourChatid",
              "Type":"db"
            }
          ```
       ##### And if you put it `json` we will deal with json file `db/IslamicAzkar.json`
        * deal with `db/IslamicAzkar.json` :
           ```
              {
                  "api_token":"YourApiToken",
                  "chat_id":"YourChatid",
                  "Type":"json"
              }
           ```
## Usage : 
  ```
   python run.py -sendmessage start
   python run.py -add islamicazkar.txt
   python run.py -random start
   python run.py -get start
  ```
## Options : 
  ```
    usage: run.py [-h] [-add islamicazkar.txt] [-get start] [-random start] [-sendmessage start]

    optional arguments:
      -h, --help            show this help message and exit
      -add ADD              -> add new data in database (You should make sure to add "islamicazkar.txt")
      -get GET              -> get all data from database
      -random               -> get random data from database
      -sendmessage          -> will send message to chat id
  ```
