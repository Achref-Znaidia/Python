import json

class Basics(object):
    def __init__(self):
        pass
        
    def printjsonnodes():
        with open("config.json","r") as file:
            data = json.load(file)
            iterations = len(data.get("event"))
            print(iterations)
            for node in data.get("event"):
                print(node)
        file.close()


    def removejsonnodes():
        with open("config.json", "r+") as file:
            data = json.load(file)
            data.get("event").clear()
            file.seek(0)
            file.truncate()
            json.dump(data,file)
        file.close()

    def revertjsonnodes():
        with open("config.json", "r+") as file:
            data = {"event": [{"message": "kernel","status": "yes"},{"message": "audit","status": "yes"},{"message": "sysl","status": "yes"},{"message": "journal","status": "yes"}]}
            file.seek(0)
            file.truncate()
            json.dump(data,file)
        file.close()



Basics.printjsonnodes()
Basics.removejsonnodes()
Basics.printjsonnodes()
Basics.revertjsonnodes()
Basics.printjsonnodes()