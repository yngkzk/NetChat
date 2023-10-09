import json

class Message():
    time = 0 
    senderName = ""
    senderIP = ""
    text = ""
    type = ""
    receiverName = ""
    receiverIP = ""
    

    def __init__(self, jsonString):
        data = json.loads(jsonString)
        if "time" in data:
            self.time = data['time']
        if "senderName" in data:
            self.senderName = data['senderName']
        if "senderIP" in data:
            self.senderIP = data['senderIP']
        if "text" in data:
            self.text = data['text']
        if "type" in data:
            self.type = data['type']
        if "receiverName" in data:
            self.receiverName = data['receiverName']        
        if "receiverIP" in data:
            self.senderName = data['receiverIP']
        
    def toJson(self): 
        data = {}
        data['time'] = self.time 
        data['senderName'] = self.senderName 
        data['senderIP'] = self.senderIP 
        data['text'] = self.text 
        data['type'] = self.type 
        data['receiverName'] = self.receiverName 
        data['receiverIP'] = self.receiverIP 
        return json.dumps(data)

if __name__ == "__main__":
    message = Message('{"text": "sender_name", "time": 50}') 
    print(message.toJson())