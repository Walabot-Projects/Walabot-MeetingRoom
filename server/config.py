"""
General configuration for the project.
"""

# DB related config
NUMBER_OF_PEOPLE_FIELD = 'number_of_people'
MAX_PEOPLE_FIELD = "max_people"
ROOM_FIELD = "name"
ROOMS_DATA_TABLE = "rooms_data"
# TODO: To be configured to the db path.
DB_PATH = r"C:\meeting-room-server\free_rooms_db.json"

# Server related config
# TODO: To be configured to the real server's ip and port.
HOST = "127.0.0.1"
PORT = 9999

# General config
UTF_FORMAT = 'UTF-8'
ROOMS_NAMES_LIST = ["yellow", "blue", "green", "purple"]
