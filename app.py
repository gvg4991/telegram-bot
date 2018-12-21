import os
import requests
from flask import Flask, request
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route(f"/") #기본값으로 get을 받는것
def hello():
    return "Hello World!"
    
@app.route(f'/{token}', methods=['POST']) #포스트란 방식으로 받음, get과 같이 받을면 ['get'],['post']로 입력
def telegram():
    
    #1. 구조 확인하기
    from_telegram = request.get_json() #dict #telegram이 준 데이터
    print(from_telegram)
    
    #2. 그대로 돌려보내기(메아리)
    if from_telegram.get('message') is not None: #['message']: 키가 없으면 에러, .get('message'): 키 없으면 None으로 나옴
    
        chat_id = from_telegram['message']['from']['id']
        text = from_telegram['message']['text']
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
#    token = os.getenv('TELEGRAM_BOT_TOKE')
#    chat_id = os.getenv('CHAT_ID')
#    text='yo!'
#    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    
    return '', 200 #반환값은 200을 줘야함
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
    