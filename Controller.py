from tkinter import simpledialog
from GameTime import GameTime
from Model import Model
from View import View, generate_leaderboard


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)
        self.gametime = GameTime(self.view.lbl_time)  # Create gametime object

    def main(self):
        self.view.main()

    def click_new(self):
        self.view.btn_new['state'] = 'disabled'
        self.view.btn_cancel['state'] = 'normal'
        self.view.btn_send['state'] = 'normal'
        self.view.char_input['state'] = 'normal'
        self.view.change_image(0)  # Image change w/ index
        self.model.start_new_game()  # Start new game
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text='Wrong letters: 0', fg='black')
        self.view.char_input.focus()  # Cursor in input
        self.gametime.reset()
        self.gametime.start()

    def click_btn_cancel(self):
        self.gametime.stop()
        self.view.btn_new['state'] = 'disabled'
        self.view.btn_cancel['state'] = 'normal'
        self.view.btn_send['state'] = 'normal'
        self.view.char_input['state'] = 'normal'
        self.view.char_input.delete(0, 'end')
        self.view.change_image(len(self.model.image_files) - 1)

    def click_button_send(self):
        self.model.get_user_input(self.view.userinput.get().strip())
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text=f'Wrong letters: {self.model.counter}. {self.model.get_all_user_chars()}')
        self.view.char_input.delete(0, 'end')
        if self.model.counter > 0:
            self.view.lbl_error.configure(fg='red')  # Font color
            self.view.change_image(self.model.counter)  # Image change after error
        self.is_game_over()

    def is_game_over(self):
        if self.model.counter >= 11 or '_' not in self.model.user_word \
                or self.model.counter >= (len(self.model.image_files) - 1):
            self.gametime.stop()
            self.view.btn_new['state'] = 'disabled'
            self.view.btn_cancel['state'] = 'normal'
            self.view.btn_send['state'] = 'normal'
            self.view.char_input['state'] = 'normal'
            player_name = simpledialog.askstring('GAME OVER', 'What\'s your name?', parent=self.view)
            self.model.set_player_name(player_name, self.gametime.counter)
            self.view.change_image(len(self.model.image_files) - 1)

    def click_btn_leaderboard(self):
        popup_window = self.view.create_popup_window()
        data = self.model.read_leaderboard_file_contents()
        generate_leaderboard(popup_window, data)
        self.view.create_all_buttons()
