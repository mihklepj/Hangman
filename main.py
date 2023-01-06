from Controller import Controller


class Hangman:

    def __init__(self):
        Controller().main()


if __name__ == '__main__':
    # TODO read commandline db name
    # TODO error when wrong letter entered twice
    Hangman()
