#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 10:33
# @Author  : zhouchong
# @Site    : 
# @File    : DialogflowWebhookRequest.py
# @Software: PyCharm

import  json
import  re


class DialogflowWebhookRequest():

    def __init__(self):
        self.responseId = ''
        self.queryText = ''
        self.originalDetectIntentRequest = ''
        self.intent = ''
        self.intentName = ''
        self.parameters = {}
        self.session = ''


    def load(self,text):
        requestJSON = json.loads(text)
        self.responseId = requestJSON['responseId']
        session = requestJSON['session']
        m = re.search('/([^/]*)$',session)
        # 处理 seesion
        if m:
            self.session = m.group(1)

        if 'queryResult' in requestJSON:
            queryResult = requestJSON['queryResult']
            if 'queryText' in queryResult:
                self.queryText = queryResult['queryText']
                if 'intent' in queryResult:
                    self.intent = queryResult['intent']['name']
                    self.intentName = queryResult['intent']['displayName']
            if 'parameters' in queryResult:
                self.parameters = queryResult['parameters']


if __name__ == '__main__':
   request = DialogflowWebhookRequest()
   text = b'{\n  "responseId": "2ad85f17-b11a-4582-83dc-652909d20856-21947381",\n  "queryResult": {\n    "queryText": "I am a teacher",\n    "parameters": {\n      "any": "a teacher"\n    },\n    "allRequiredParamsPresent": true,\n    "fulfillmentText": "i like you",\n    "fulfillmentMessages": [{\n      "text": {\n        "text": ["i like you"]\n      }\n    }, {\n      "payload": {\n        "tts": [{\n          "text": "this have some question,can you answer that?",\n          "lang": "en",\n          "action": {\n            "name": "",\n            "param": {\n            }\n          },\n          "expression": {\n            "name": "smile",\n            "param": {\n            }\n          }\n        }]\n      }\n    }],\n    "intent": {\n      "name": "projects/newagent-fec3e/agent/intents/39adb4b3-a7dc-4a16-bf80-97228df2f181",\n      "displayName": "webhook_test"\n    },\n    "intentDetectionConfidence": 1.0,\n    "languageCode": "en"\n  },\n  "originalDetectIntentRequest": {\n    "payload": {\n      "latitude": 40.707344,\n      "longitude": -74.011137,\n      "sid": "e831d13f-c153-4ede-80ce-d9a670010f0d"\n    }\n  },\n  "session": "projects/newagent-fec3e/agent/sessions/cloudmindsdemo23"\n}'
   request.load(text)
   print(request)