0. Install forunes
```
sudo apt install fortunes fortunes-ru
```

1. Install Python3 and virtualenv
```
sudo apt install python3 python3-virtualenv
```

Alternate you may also use pip:
```
sudo pip3 install virtualenv
```

2. Make virtual enviroment
```
mkdir fortune_bot
cd fortune_bot
virtualenv venv -p python3
``` 

3. Go into virtual enviroment
```
source venv/bin/activate
```

4. Install pip install aiogram (into virtual enviroment)
```
pip install aiogram
```

5. Go to https://web.telegram.org and connect to @BotFathr
```
/start
/newbot
```
Copy HTTP API token

6. Create `secret_bot.py` like `secret_bot_example.py`

7. Run `./start_bot.sh`


