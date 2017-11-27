# Meeting Room #
This app helps you find a free meeting room around the office.
It's an example of an integration between Walabot and Alexa.

## How it works

### 1. Connect a Walabot to a RPi and install both on the door header 

### 2. Run the server
 * Go to the repo folder
 * In the server folder, edit the `DB_PATH` variable in the `config.py` file to be the server location
 * Run `python main.py` 
 * Run `ngrok http 5000` (you'll need to download ngrok first)
 * Copy the URL output from the previous step and use it in the configuration tab at https://developer.amazon.com.

### 3. Run client 
* Make sure that on the `meeting_room_client.py` you have the server's IP confiugred
* Run `meeting_room_client.py`on RPi

Once that's done, it means that the number of people in the room is constantly streamed to the server


### 4. Create the Alexa APP
We have an Alexa app that we developed.

TODO - need to find a way to make it public and the server IP dynamic.


## Questions you can ask Alexa ##
* Alexa, meeting room
* Alexa, search meeting room for 3 people
* Alexa, ask meeting room how many people are in the yellow room
* Alexa, ask meeting room if the yellow room is free/available

 ## Testing without Walabot ##
 * Go to repo folder
 * Run `python`
 * Run `import json, socket`
 * Run `s = socket.socket()`
 * Run `s.connect(("127.0.0.1", 9999))`
 * Run `s.send(json.dumps({"name": "yellow", "number_of_people": 0, "max_people": 10}).encode('UTF-8'))`
 * For adding other rooms with different configuration please repeat the previous step using different parameters
