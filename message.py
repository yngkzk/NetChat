import json

class Message():
    time = 0
    text = ''
    type = ''
    senderName = ''  
    senderIP = ''
    receiverName = ''
    receiverIP = ''
    

    def __init__(self, jsonstring): # '{"time": "03-10-2023", ....}'
        data = json.loads(jsonstring)
        self.time = data.get('time', 0)
        if "senderIP" in data:
            self.senderIP = data['senderIP']
        if "senderName" in data:
            self.senderName = data['senderName']
        if "text" in data:
            self.text = data['text']
        if "receiverIP" in data:
            self.receiverIP = data['receiverIP']
        if "receiverName" in data:
            self.receiverName = data['receiverName']
        if "type" in data:
            self.type = data['type']
    
    def toJson(self):
        data = {}
        data['time'] = self.time
        data['text'] = self.text
        data['type'] = self.type
        data['senderIP'] = self.senderIP
        data['senderName'] = self.senderName
        data['receiverIP'] = self.receiverIP
        data['receiverName'] = self.receiverName
        return json.dumps(data)
    
if '__main__' == __name__:
    msg = Message('{"text":"sender_name","time":50}')
    print(msg.toJson())


