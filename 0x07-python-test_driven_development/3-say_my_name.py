""" say_my_name """


def say_my_name(first_name, last_name=""):

    """ prints My name is <first name> <last name>

    Args:
        first_name (str): The first name to be printed
        last_name (str): The second name to be printed

    Returns:
        My name is <first name> <last name>

    """
    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("first_name must be a string")

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
