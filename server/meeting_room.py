"""
Export The flask app that will communicates with alexa.
"""


from flask import Flask
from flask_ask import Ask, statement
from tinydb import Query

from DBHandler import DBHandler as TinyDB
from config import ROOMS_DATA_TABLE, DB_PATH, NUMBER_OF_PEOPLE_FIELD, ROOM_FIELD, ROOMS_NAMES_LIST
from utils import check_if_room_exists

app = Flask(__name__)
ask = Ask(app, '/')
db = TinyDB(DB_PATH, default_table=ROOMS_DATA_TABLE)
room = Query()


def get_free_rooms(requested_number_of_people=0):
    """
    Get all the available rooms from the DB that answers the requested_number_of_people argument limitation.
    :param requested_number_of_people: The amount of people that will occupy the room, if it's 0 so there is no
        consideration in this parameter.
    :type requested_number_of_people: C{int}
    :return: All the available rooms from the db
    :rtype: C{str}
    """
    free_rooms = db.search((room.number_of_people == 0) & (requested_number_of_people <= room.max_people))
    free_rooms = [free_room[ROOM_FIELD] for free_room in free_rooms]
    if not free_rooms:
        return
    return ",".join(free_rooms)


@ask.intent('FindARoomIntent', mapping={'requested_number_of_people': 'RequestedNumberOfPeople'},
            convert={"requested_number_of_people": int})
def find_me_a_room(requested_number_of_people):
    """
    The handler for the FindARoomIntent, it will return all the available rooms that are in the db.
    :param requested_number_of_people: The amount of people that will occupy the room.
    :type requested_number_of_people: C{int}
    :return: The statement with all the available rooms.
    :rtype: C{flask_ask.statement}
    """
    try:
        free_rooms = get_free_rooms(requested_number_of_people)
        return statement("Sorry, there are no available rooms for {0} people at the moment."
                         .format(requested_number_of_people)) if free_rooms is None else get_correlate_statement(free_rooms)
    except TypeError:
        return statement("Sorry, I didn't get it.")


@ask.intent("IsRoomFreeIntent", mapping={'room_name': 'Room'})
@check_if_room_exists
def is_a_room_free(room_name):
    """
    The handler for the IsRoomFreeIntent, it will return if a certain room is available or not.
    :param room_name: The room's name to check if its available or not.
    :type room_name: C{str}
    :return: The statement corresponding to if the room given in the argument is available or not, if there is no
        room with this name then returning a statement that says it.
    :rtype: C{flask_ask.statement}
    """
    room_row = db.get(room.name == room_name)
    if room_row is None:
        return statement("I'm sorry, I am not getting information from the {0} room. Please check if Wala-bot"
                         "is installed there.".format(room_name))
    if room_row[NUMBER_OF_PEOPLE_FIELD] == 0:
        return statement("The {0} room is now available.".format(room_name))
    return statement("The {0} room is not available at the moment.".format(room_name))


def get_correlate_statement(free_rooms):
    """
    Get the statement according to the free_rooms argument, it could be one room or more.
    :param free_rooms: The available rooms string.
    :type free_rooms: C{str}
    :return: The statement.
    :rtype: C{flask_ask.statement}
    """
    if len(free_rooms.split(",")) == 1:
        return statement("Sure, the {0} room is now available.".format(free_rooms))
    free_rooms_list = free_rooms.split(",")
    last_room = free_rooms_list[-1]
    free_rooms_list.remove(last_room)
    return statement("Sure, the {0}, and {1} rooms are now available.".format(",".join(free_rooms_list), last_room))


@ask.intent("HowManyPeopleIntent", mapping={'room_name': 'Room'})
@check_if_room_exists
def how_many_people_in_room(room_name):
    """
    Check how many people are the in the given room name.
    :param room_name: The room_name to check how many people in it.
    :type room_name: C{str}
    :return: The answer with the number of people that's are in the room.
    :rtype: C{flask_ask.statement}
    """
    if room_name not in ROOMS_NAMES_LIST:
        return statement("There is no such room named {0}".format(room_name))
    room_row = db.get(room.name == room_name)
    if room_row is None:
        return statement("I'm sorry, I am not getting information from the {0} room. Please check if Wala-bot"
                         "is installed there.".format(room_name))
    if room_row[NUMBER_OF_PEOPLE_FIELD] == 1:
        return statement("There is currently {0} person in the {1} room"
                         .format(room_row[NUMBER_OF_PEOPLE_FIELD], room_name))
    return statement("There are currently {0} people in the {1} room"
                     .format(room_row[NUMBER_OF_PEOPLE_FIELD], room_name))


@ask.launch
def welcome_to_free_rooms():
    """
    Return the welcome message to our skill.
    :return: The welcome message to our skill
    :rtype: C{flask_ask.question}
    """
    free_rooms = get_free_rooms()
    if free_rooms is None:
        return statement("Sorry, there are no available rooms at the moment.")
    return get_correlate_statement(free_rooms)
