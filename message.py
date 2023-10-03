import json

class Message():
    time = 0 
    senderName = ""
    text = ""
    type = ""
    receiverName = ""
    

    def __init__(self, jsonString):
        data = json.loads(jsonString)
        if "time" in data:
            self.time = data['time']
        if "senderName" in data:
            self.senderName = data['senderName']
        if "text" in data:
            self.text = data['text']
        if "type" in data:
            self.type = data['type']
        if "receiverName" in data:
            self.receiverName = data['receiverName']
        
    def toJson(self): 
        data = {}
        data['time'] = self.time 
        data['senderName'] = self.senderName 
        data['text'] = self.text 
        data['type'] = self.type 
        data['receiverName'] = self.receiverName 
        return json.dumps(data)

if __name__ == "__main__":
    message = Message('{"text": "sender_name", "time": 50}') 
    print(message.toJson())