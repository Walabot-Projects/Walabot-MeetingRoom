This is an Alexa server for "meeting room" app using Walabot and Alexa. 
---

## Questions you can ask Alexa ##
* Alexa, meeting room
* Alexa, search meeting room for 3 people
* Alexa, ask meeting room how many people are in the yellow room
* Alexa, ask meeting room if the yellow room is free/available

## Getting started ##
 * Go to the repo folder
 * Run `python main.py` 
 * Run `ngrok http 5000`
 * Copy the URL output from the previous step and use it in the configuration tabe at https://developer.amazon.com.
 
## Testing without Walabot##
 * Go to repo folder
 * Run `import json, socket`
 * Run `s = socket.socket()`
 * Run `s.connect(("127.0.0.1", 9999))`
 * Run `s.send(json.dumps({"name": "yellow", "number_of_people": 0, "max_people": 10}).encode('UTF-8'))`
