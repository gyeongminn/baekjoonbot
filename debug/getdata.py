# api docs : https://solvedac.github.io/unofficial-documentation/#/operations/getProblemById

from bs4 import BeautifulSoup      # 크롤링 사이트의 값을 가져오는 함수
import requests
import json

def get_data(problem):
    url = 'https://solved.ac/api/v3/problem/show?problemId='+str(problem)
    requestData = requests.get(url)
    return json.loads(requestData.content)


def get_icon(level):
    return 'https://d2gd6pc034wcta.cloudfront.net/tier/'+str(level)+'.svg'


print(get_data(13460)['level'])


"""save1 = []   # 관련 값 다 저장하기

url = 'https://solved.ac/search?query=13460'

req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
soup = BeautifulSoup(req.text, "html")  # html에 대하여 접근할 수 있도록


print(soup)
"""

