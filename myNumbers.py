# encoding: utf-8
"""
This file deals with parsing phone numbers.
"""


def on_open(fil):
    """
    This method is run on opening a file. It strips the lines and returns them as a list
    :param fil: the file to read
    :return: the lines of the files divided into a list
    """
    with open(fil) as f:
        lst = [l.strip() for l in f]
    print(lst)
    return lst


def on_close(lst, fil):
    """
    This method runs on closing a file. It writes all of the lines of the provided list
    to the file
    :param lst: the list of lines to be written to the file
    :param fil: the file to write to
    :return: None
    """
    with open(fil, "w") as f:
        f.writelines("%s\n" % l for l in lst)
    print(lst)
