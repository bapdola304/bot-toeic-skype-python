from skpy import SkypeEventLoop, SkypeNewMessageEvent, Skype
import requests
from datetime import date
import datetime
import json
from googletrans import Translator
import wikipedia
import random
import feedparser
from gtts import gTTS
import os
import numpy as np

Skype("bapdola304@gmail.com", "Ngohung0", "token")

wikipedia.set_lang("vi")
translator = Translator()

print('Bot are running...')

foo = ['Back', 'Tuyến', 'Đon', 'Nai', 'Vươnq', 'Duck', 'Quâng', 'Hâng']
index = 0
da = ["A", "B", "C", "D"]

def getHeadlines( rss_url ):
    headlines = []
    feed = feedparser.parse( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
    return headlines

class SkypePing(SkypeEventLoop):
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId:
          # print(event.msg.userId)
          # print(event.msg.content)
          # print("----------------")
          global index

          # if "skip" in event.msg.content.lower():
          #   event.msg.chat.sendMsg('.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.')
          # if "tết" in event.msg.content.lower():
          #   d0 = date.today()
          #   d1 = date(2021, 2, 12)
          #   delta = d1 - d0
          #   event.msg.chat.sendMsg('Còn ' + str(delta.days) + ' ngày nữa tới Tết')
          # if "noel" in event.msg.content.lower():
          #   today = date.today()
          #   someday = date(2020, 12, 24)
          #   diff = someday - today
          #   event.msg.chat.sendMsg('Còn ' + str(diff.days) + ' ngày nữa tới Noel')
          # if "corona" in event.msg.content.lower():
          #   response = requests.get('https://tygia.com/app/covid-19/api.json?type=2').text
          #   data1 = json.loads(response)['items']
          #   ketqua = "Bảng xếp hạng:\n"
          #   for x in range(21):
          #     ketqua = ketqua + '--------\n'
          #     ketqua = ketqua + str(data1[x]['type']) + "\n"
          #     ketqua = ketqua + "- " + str(data1[x]['total']) + " trường hợp\n"
          #     ketqua = ketqua + "- " + str(data1[x]['death']) + " tử vong\n"
          #     ketqua = ketqua + "- " + str(data1[x]['recovered']) + " chữa khỏi\n"
          #   event.msg.chat.sendMsg(ketqua)
          # if "dịch:" in event.msg.content.lower():
          #   text = event.msg.content.split(':')
          #   try:
          #     event.msg.chat.sendMsg(translator.translate(text[1].strip(), dest='vi').text)
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "trans:" in event.msg.content.lower():
          #   text = event.msg.content.split(':')
          #   try:
          #     event.msg.chat.sendMsg(translator.translate(text[1].strip(), dest='en').text)
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "định nghĩa:" in event.msg.content.lower():
          #   text = event.msg.content.split(':')
          #   try:
          #     event.msg.chat.sendMsg(wikipedia.summary(text[1].strip()))
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "speak:" in event.msg.content.lower():
          #   text = event.msg.content.split(':')
          #   try:
          #     tts = gTTS(text[1].strip())
          #     tts.save('speak.mp3')
          #     event.msg.chat.sendFile(open("speak.mp3", "rb"), "speak.mp3", False, True)
          #     # os.remove("speak.mp3")
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "話す:" in event.msg.content.lower():
          #   text = event.msg.content.split(':')
          #   try:
          #     tts = gTTS(text[1].strip(), lang='ja')
          #     tts.save('speak.mp3')
          #     event.msg.chat.sendFile(open("speak.mp3", "rb"), "speak.mp3", False, True)
          #     # os.remove("speak.mp3")
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "đọc:" in event.msg.content.lower():
          #   text = event.msg.content.split(':')
          #   try:
          #     tts = gTTS(text[1].strip(), lang='vi')
          #     tts.save('speak.mp3')
          #     event.msg.chat.sendFile(open("speak.mp3", "rb"), "speak.mp3", False, True)
          #     os.remove("speak.mp3")
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "xin phép" in event.msg.content.lower():
          #   event.msg.chat.sendMsg('djt cm ông ' + random.choice(foo))
          # if "ai là" in event.msg.content.lower():
          #   event.msg.chat.sendMsg('Là ông ' + random.choice(foo))
          # if "tại vì sao" in event.msg.content.lower():
          #   event.msg.chat.sendMsg('tại vì... ngu')
          # if "từ vựng" in event.msg.content.lower() or  "word" in event.msg.content.lower():
          #   input_file = open('data.json', encoding='utf-8')
          #   json_array = json.load(input_file)
          #   item = random.choice(json_array)
          #   event.msg.chat.sendMsg(item.get('en') + ': ' + item.get('vi'))
          #   try:
          #     tts = gTTS(item.get('en'))
          #     tts.save('speak.mp3')
          #     event.msg.chat.sendFile(open("speak.mp3", "rb"), "speak.mp3", False, True)
          #     os.remove("speak.mp3")
          #   except:
          #     event.msg.chat.sendMsg('?')
          # if "tin tức" in event.msg.content.lower():
          #   allheadlines = []
          #   hihi = ""
          #   allheadlines.extend(getHeadlines('https://vnreview.vn/feed/-/rss/home'))
          #   for hl in allheadlines:
          #     hihi = hihi + hl + "\n"
          #   event.msg.chat.sendMsg(hihi)
          # if "không làm" in event.msg.content.lower() or  "ko làm" in event.msg.content.lower():
          #   event.msg.chat.sendMsg('ăn đầu buoy`, căn kut\'')
          # # if "hân" in event.msg.content.lower():
          # #   event.msg.chat.sendMsg('Hiện tại Hân đang bận, không thể trả lời tin nhắn.')
          # # if "thì" in event.msg.content.lower():
          # #   event.msg.chat.sendMsg('có cái đầu buoy`')
          # if "cu" == event.msg.content.lower():
          #   event.msg.chat.sendFile(open("images/cu.png", "rb"), "cu.png", "image")
          # if "pokemon" in event.msg.content.lower() or  "pokémon" in event.msg.content.lower():
          #   number = random.randint(1,891)
          #   image_url = "http://assets.pokemon.com/assets/cms2/img/pokedex/detail/" + "{:03d}".format(number) +".png"
          #   img_data = requests.get(image_url).content
          #   with open('pokemon.png', 'wb') as handler:
          #       handler.write(img_data) # write do dia
          #   event.msg.chat.sendFile(open("pokemon.png", "rb"), "pokemon.png", "image") #send file
          #   os.remove("pokemon.png") #remove file
          # if "gửi ảnh" in event.msg.content.lower():
          #   now = datetime.datetime.now()
          #   if now.hour > 18:
          #     event.msg.chat.sendFile(open("images/1.jpg", "rb"), "1.jpg", "image")
          #   else :
          #     event.msg.chat.sendMsg('Tính năng chỉ khả dụng sau 7h tối')

          if "toeic part1" in event.msg.content.lower():
            input_file = open('toeicPart1.json', encoding='utf-8')
            json_array = json.load(input_file)
            item = json_array[index]
            index = index + 1
            if index == len(json_array):
              index = 0
            audio_url = item.get('audio')
            img_url = item.get('image')
            question_id = item.get('question_id')
            audio_data = requests.get(audio_url).content
            img_data = requests.get(img_url).content
            with open('audio.mp3', 'wb') as handler:
                handler.write(audio_data) # write do dia
            with open('img.png', 'wb') as handler:
                handler.write(img_data) # write do dia
            event.msg.chat.sendMsg('Câu ' + question_id)
            event.msg.chat.sendFile(open("img.png", "rb"), "img.png", "image") #send file
            event.msg.chat.sendFile(open("audio.mp3", "rb"), "audio.mp3", False, True)
            os.remove("img.png") #remove file
            os.remove("audio.mp3") #remove file
          if "đáp án" in event.msg.content.lower():
            question_id = event.msg.content.lower().split(" ")[2]
            input_file = open('toeicPart1.json', encoding='utf-8')
            json_array = json.load(input_file)
            arr = np.array(json_array)
            arrTemp = []
            for element in arr:
              if element.get('question_id') == question_id:
                arrTemp.append(element)
                break
            print(arrTemp)
            event.msg.chat.sendMsg('Đáp án câu ' + question_id + ' : ' + arrTemp[0].get('answerCorrect'))
          if "toeic part2" in event.msg.content.lower():
            input_file = open('toeicPart2.json', encoding='utf-8')
            json_array = json.load(input_file)
            item = random.choice(json_array)
            audio_url = item.get('audio')
            question_id = item.get('question_id')
            audio_data = requests.get(audio_url).content
            with open('audio.mp3', 'wb') as handler:
                handler.write(audio_data) # write do dia
            event.msg.chat.sendMsg('Part 2: Câu ' + question_id)
            event.msg.chat.sendFile(open("audio.mp3", "rb"), "audio.mp3", False, True)
            os.remove("audio.mp3") #remove file
          if "p2" in event.msg.content.lower():
            question_id = event.msg.content.lower().split(" ")[1]
            print(question_id)
            input_file = open('toeicPart2.json', encoding='utf-8')
            json_array = json.load(input_file)
            arr = np.array(json_array)
            arrTemp2 = []
            for element in arr:
              if element.get('question_id') == question_id:
                arrTemp2.append(element)
                break
            list_anwser = arrTemp2[0].get('answers')
            for i in range(len(list_anwser)):
              if i == 0:
                event.msg.chat.sendMsg('Question: ' + list_anwser[i].get('content'))
              else:
                if list_anwser[i].get('correct') == '1':
                  event.msg.chat.sendMsg( da[i-1] +  '. ' + list_anwser[i].get('content') + '(*answer correct*)')
                else:
                  event.msg.chat.sendMsg( da[i-1] +  '. ' + list_anwser[i].get('content'))
sk = SkypePing(tokenFile="token", autoAck=True)
sk.loop()