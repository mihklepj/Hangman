import glob


class Model:

    def __init__(self):
        self.database_name = 'databases/hangman_words_ee.db'  # Database with words
        self.image_files = glob.glob('images/*.png')  # All hangman files
        # New game
        self.new_word = None  # Random word from database
        self.user_word = []  # User found letters
        self.all_user_chars = []  # Any letters user entered incorrectly
        self.counter = 0  # Error counter
        self.player_name = 'UNKNOWN'
        self. leaderboard_file = 'leaderboard.txt'
        self.score_data = []  # Leaderboard file contents