import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re
from time import sleep

while True:
    res = requests.get('https://signate.jp/competitions/162/leaderboard#scoreboard')
    html = res.text

    soup = BeautifulSoup(html, 'html.parser')
    lb_overall = soup.find_all('script')[-8].string
    p = re.compile(r'var minVal = (.*?);')
    m = p.findall(lb_overall)[0]
    print('*'*150)
    print('Execute time: %s' % datetime.now().time())
    print('Best score is: %s' % m)

    lb = json.loads(soup.find_all('competition-leaderboard-component')[0][':ranking-list'])
    for i in range(10):
        name = lb[i]['user']['name']
        score = lb[i]['score_tmp']
        submits = lb[i]['submits']
        score_time = lb[i]['scored_at']
        update_time = lb[i]['updated_at']
        print('Rank %d: name: %s score: %s score_time: %s update_time: %s submits: %s' % (i, name, score, score_time, update_time, submits))
    print('*'*150)
    sleep(1800)
