"""
Runs that functionality of the program, the flask app and the server that communicates with Walabot.
"""

from threading import Thread

from meeting_room import app
from FreeRoomsServer import FreeRoomsServer
from config import HOST, PORT


def main():
    """
    Start the server that communicates with Walabot and the flask app the communicated with Alexa.
    """
    try:
        server = FreeRoomsServer(HOST, PORT)
        free_rooms_server_thread = Thread(target=server.start)
        alexa_server_thread = Thread(target=app.run)

        free_rooms_server_thread.start()
        alexa_server_thread.start()

        free_rooms_server_thread.join()
        alexa_server_thread.join()

    except Exception:
        print("Unknown exception occurred!")
        raise

if __name__ == '__main__':
    main()
