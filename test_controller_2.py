from controller_2 import *


class Test:
    def setup_method(self):
        self.cont = Controller()

    def teardown_method(self):
        del self.cont

    def test_battle(self):
        self.cont.battle()
        assert self.cont.__str__() == 'What is your name?'
        self.cont.name()
        self.cont.battle()
        assert self.cont.__str__() == 'Pick Rock Paper or Scissors to play!'
        self.cont.update_button(1)
        self.cont.name()
        self.cont.battle()
        assert self.cont.__str__() == ''

    def test_update_button(self):
        assert self.cont.update_button(1) == 'paper button on'
        assert self.cont.update_button(2) == 'rock button on'
        assert self.cont.update_button(3) == 'scissor button on'

