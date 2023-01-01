import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://github.com/Jnanesh12/jna-mdisc-sesrch-bita-bot okk && cd okk && pip3 install -U -r requirements.txt && nohup gunicorn app:app & python3 main.py &")
