class Controller:
    def __init__(self):
        self.me_label = ''
        self.info_label = ''
        self.radioButton_p = False
        self.radioButton_r = False
        self.radioButton_s = False

    def update_button(self, update):
        if update == 1:
            self.radioButton_p = not self.radioButton_p
            return 'paper button on'
        elif update == 2:
            self.radioButton_r = not self.radioButton_r
            return 'rock button on'
        elif update == 3:
            self.radioButton_s = not self.radioButton_s
            return 'scissor button on'


    def name(self):
        self.me_label = 'Josh'

    def battle(self):
        if self.me_label != '':
            self.info_label = ''
        if self.me_label == '':
            self.info_label = 'What is your name?'
        elif self.radioButton_p is False and self.radioButton_r is False \
                and self.radioButton_s is False:
            self.info_label = 'Pick Rock Paper or Scissors to play!'

    def __str__(self) -> str:
        print(f'{self.info_label}')
        return f'{self.info_label}'
