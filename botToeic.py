from skpy import SkypeEventLoop, SkypeNewMessageEvent, Skype
import requests
from datetime import date
import datetime
import json
import random
import os
import numpy as np

#define path
toeicPart1Path = './data/toeicPart1.json'
toeicPart2path = './data/toeicPart2.json'
tokenPath = './config/token'
accountPath ='./config/account.json'

#authen
authAccount = open(accountPath, encoding='utf-8')
account = json.load(authAccount)
username = account.get('username')
password = account.get('password')
Skype(username, password, "./config/token")
print('Bot is already running...')

#get data
part1Data= open(toeicPart1Path, encoding='utf-8')
part1FormatJson = json.load(part1Data)
part2Data= open(toeicPart2path, encoding='utf-8')
part2FormatJson = json.load(part2Data)
da = ["A", "B", "C", "D"]
dad = '1'

class SkypePing(SkypeEventLoop):
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId:
          if "toeic part1" in event.msg.content.lower() or "toeic part 1" in event.msg.content.lower() or "part 1" in event.msg.content.lower() or "part1" in event.msg.content.lower():
            part1Item = random.choice(part1FormatJson)
            audio_url = part1Item.get('audio')
            img_url = part1Item.get('image')
            question_id = part1Item.get('question_id')
            audio_data = requests.get(audio_url).content
            img_data = requests.get(img_url).content
            with open('part1.mp3', 'wb') as handler:
                handler.write(audio_data) # write do dia
            with open('img.png', 'wb') as handler:
                handler.write(img_data) # write do dia
            event.msg.chat.sendMsg('Câu ' + question_id)
            event.msg.chat.sendFile(open("img.png", "rb"), "img.png", "image") #send file
            event.msg.chat.sendFile(open("part1.mp3", "rb"), "part1.mp3", False, True)
            os.remove("img.png") #remove file
            os.remove("part1.mp3") #remove file
          if "p1" in event.msg.content.lower():
            question_id = event.msg.content.lower().split(" ")[1]
            try:
              arr = np.array(part1FormatJson)
              arrTemp = []
              for element in arr:
                if element.get('question_id') == question_id:
                  arrTemp.append(element)
                  break
              answers = arrTemp[0].get('answers')
              event.msg.chat.sendMsg('Câu ' + question_id)
              for i in range(len(answers)):
                if answers[i].get('correct') == '1':
                  event.msg.chat.sendMsg(da[i] + '. ' + answers[i].get('content') + ' (*correct answer)')
                else:
                  event.msg.chat.sendMsg( da[i] + '. ' + answers[i].get('content'))
            except:
              event.msg.chat.sendMsg('syntax: p1 questionId')
          if "toeic part2" in event.msg.content.lower() or "toeic part 2" in event.msg.content.lower() or "part 2" in event.msg.content.lower() or "part2" in event.msg.content.lower():
            part2Item = random.choice(part2FormatJson)
            audio_url = part2Item.get('audio')
            question_id = part2Item.get('question_id')
            audio_data = requests.get(audio_url).content
            with open('part2.mp3', 'wb') as handler:
                handler.write(audio_data) # write do dia
            event.msg.chat.sendMsg('Part 2: Câu ' + question_id)
            event.msg.chat.sendFile(open("part2.mp3", "rb"), "part2.mp3", False, True)
            os.remove("part2.mp3") #remove file
          if "p2" in event.msg.content.lower():
            question_id = event.msg.content.lower().split(" ")[1]
            try:
              arr = np.array(part2FormatJson)
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
            except:
              event.msg.chat.sendMsg('syntax: p2 questionId')
sk = SkypePing(tokenFile=tokenPath, autoAck=True)
sk.loop()