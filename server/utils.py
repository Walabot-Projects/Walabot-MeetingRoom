from functools import wraps

from flask_ask import statement

from config import ROOMS_NAMES_LIST


def check_if_room_exists(func):
    """
    A decorator for checking if a room exists.
    :param func: The function to wrap.
    :type func: C{function}
    :return: The wrapping function
    :rtype: C{function}
    """

    @wraps(func)
    def wrapping_func(room_name):
        """
        Check if the room exists before doing the function.
        :param room_name: The room's name check if it exists.
        :type room_name: C{str}
        :return: The wrapped function return value
        :rtype: C{any}
        """
        if room_name not in ROOMS_NAMES_LIST:
            return statement("There is no such room named {0}".format(room_name))
        return func(room_name)

    return wrapping_func
