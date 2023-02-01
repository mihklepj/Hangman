import os.path

from Controller import Controller
from sys import argv  # Käsurea lugemiseks


class Hangman:

    def __init__(self):
        Controller(db_name).main()


if __name__ == '__main__':
    # TODO read commandline db name
    # TODO Enter as Send
    # TODO check if leaderboard file exists
    db_name = None
    if len(argv) == 2:
        if os.path.exists(argv[1]):
            db_name = argv[1]  # new db name from command line
    Hangman()
