import requests, json
token='539751659:AAEJZ5PQ1PQeoAEVnWpzqjLzuH23Ib1i-2c' ; chatid='-1001378908039'; userid='9545489'
tgurl = 'https://api.telegram.org/bot'
def inchat(chatid, userid):
r = requests.get(tgurl+token+....)

def sendmsg(chatid, text):
requests.get(tgurl+token+'/sendMessage?chat_id='+chatid+'&text='+text)

if not in chat(chatid, userid):
sendmsg(chatid, "Зин сбежал")
