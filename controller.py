from PyQt5.QtWidgets import *
from view import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import random


class Controller(QMainWindow, Ui_MainWindow):
    """
    Class that holds the methods of the Rock Paper Scissors game
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Method that holds variables and calls other methods when widget is interacted with
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.radioButton_p.clicked.connect(lambda: self.button_update(0))
        self.radioButton_r.clicked.connect(lambda: self.button_update(1))
        self.radioButton_s.clicked.connect(lambda: self.button_update(2))
        self.enemy_label_2.setText(self.opponents())
        self.enemy_label.setText(self.textEdit_entry2.toPlainText())
        self.button_name.clicked.connect(lambda: self.name())
        self.button_submit.clicked.connect(lambda: self.battle())
        self.enemy_move: str = ''
        self.your_points: int = 0
        self.their_points: int = 0
        self.draw: int = 0

    def opponents(self) -> str:
        """
        Method used to pick a name for your opponent
        :return: str
        """
        enemy = ['Dave', 'Bob', 'Emma', 'Victoria']
        random_enemy = random.choice(enemy)
        return random_enemy

    def battle(self) -> None:
        """
        Method that will check to see if conditions are meet and who wins and loses
        :return: None
        """
        move_options = ['rock', 'paper', 'scissor']
        if self.me_label.text() != '':
            self.info_label.setText('')
        if self.me_label.text() == '':
            self.info_label.setText('What is your name?')
        elif self.radioButton_p.isChecked() is False and self.radioButton_r.isChecked() is False \
                and self.radioButton_s.isChecked() is False:
            self.info_label.setText('Pick Rock Paper or Scissors to play!')
        else:
            self.enemy_move = random.choice(move_options)
            if self.enemy_move == 'rock':
                qpixmap = QPixmap('Project1RPSrock.jpg')
                self.rps_img_enemy.setPixmap(qpixmap)
            elif self.enemy_move == 'paper':
                qpixmap = QPixmap('Project1RPSpaper.jpg')
                self.rps_img_enemy.setPixmap(qpixmap)
            else:
                qpixmap = QPixmap('Project1RPSscissors.jpg')
                self.rps_img_enemy.setPixmap(qpixmap)
            if self.enemy_move == 'rock' and self.radioButton_r.isChecked():
                self.info_label.setText('You tied, pick again!')
                self.draw += 1
                self.draw_label.setText(str(self.draw))
            elif self.enemy_move == 'rock' and self.radioButton_p.isChecked():
                self.info_label.setText('You scored one point!')
                self.your_points += 1
                self.your_points_label.setText(str(self.your_points))
            elif self.enemy_move == 'rock' and self.radioButton_s.isChecked():
                self.info_label.setText('They scored one point!')
                self.their_points += 1
                self.their_points_label.setText(str(self.their_points))
            elif self.enemy_move == 'paper' and self.radioButton_p.isChecked():
                self.info_label.setText('You tied, pick again!')
                self.draw += 1
                self.draw_label.setText(str(self.draw))
            elif self.enemy_move == 'paper' and self.radioButton_s.isChecked():
                self.info_label.setText('You scored one point!')
                self.your_points += 1
                self.your_points_label.setText(str(self.your_points))
            elif self.enemy_move == 'paper' and self.radioButton_r.isChecked():
                self.info_label.setText('They scored one point!')
                self.their_points += 1
                self.their_points_label.setText(str(self.their_points))
            elif self.enemy_move == 'scissor' and self.radioButton_s.isChecked():
                self.info_label.setText('You tied, pick again!')
                self.draw += 1
                self.draw_label.setText(str(self.draw))
            elif self.enemy_move == 'scissor' and self.radioButton_r.isChecked():
                self.info_label.setText('You scored one point!')
                self.your_points += 1
                self.your_points_label.setText(str(self.your_points))
            elif self.enemy_move == 'scissor' and self.radioButton_p.isChecked():
                self.info_label.setText('They scored one point!')
                self.their_points += 1
                self.their_points_label.setText(str(self.their_points))
        if self.their_points > 2 or self.your_points > 2:
            if int(self.your_points) > int(self.their_points):
                self.winnerlabel.setText('You won the RPS Tournament!')
            elif int(self.your_points) < int(self.their_points):
                self.winnerlabel.setText('You lost the RPS Tournament!')


    def name(self) -> None:
        """
        Method used to place your name into a label
        :return: None
        """
        self.me_label.setText(f'{self.textEdit_entry2.toPlainText()}')

    def button_update(self, update) -> None:
        """
        Method used to update your choice of rock paper or scissors
        :param update: int
        :return: None
        """
        if update == 0:
            qpixmap = QPixmap('Project1RPSpaper.jpg')
            self.rps_img_me.setPixmap(qpixmap)
            self.radioButton_r.setChecked(False)
            self.radioButton_s.setChecked(False)
        elif update == 1:
            qpixmap = QPixmap('Project1RPSrock.jpg')
            self.rps_img_me.setPixmap(qpixmap)
            self.radioButton_p.setChecked(False)
            self.radioButton_s.setChecked(False)
        elif update == 2:
            qpixmap = QPixmap('Project1RPSscissors.jpg')
            self.rps_img_me.setPixmap(qpixmap)
            self.radioButton_p.setChecked(False)
            self.radioButton_r.setChecked(False)

    def __str__(self) -> str:
        return f'{self.info_label.text()}'
