from controller import *


def main():
    app = QApplication([])
    window = Controller()
    window.setFixedWidth(1000)
    window.setFixedHeight(700)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
