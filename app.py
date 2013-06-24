import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from armageddon import Armageddon
from gui import Ui_mainWindow


class ArmageddonByArrows(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.armageddon = Armageddon()
        QtCore.QObject.connect(self.ui.leftButton, QtCore.SIGNAL("pressed()"), self.move_left)
        QtCore.QObject.connect(self.ui.rightButton, QtCore.SIGNAL("pressed()"), self.move_right)
        QtCore.QObject.connect(self.ui.upButton, QtCore.SIGNAL("pressed()"), self.move_up)
        QtCore.QObject.connect(self.ui.downButton, QtCore.SIGNAL("pressed()"), self.move_down)
        QtCore.QObject.connect(self.ui.leftButton, QtCore.SIGNAL("released()"), self.stop_movement)
        QtCore.QObject.connect(self.ui.rightButton, QtCore.SIGNAL("released()"), self.stop_movement)
        QtCore.QObject.connect(self.ui.upButton, QtCore.SIGNAL("released()"), self.stop_movement)
        QtCore.QObject.connect(self.ui.downButton, QtCore.SIGNAL("released()"), self.stop_movement)
        QtCore.QObject.connect(self.ui.fireButton, QtCore.SIGNAL("clicked()"), self.fire)

    def move_left(self):
        self.armageddon.send_cmd(self.armageddon.LEFT)

    def move_right(self):
        self.armageddon.send_cmd(self.armageddon.RIGHT)

    def move_up(self):
        self.armageddon.send_cmd(self.armageddon.UP)

    def move_down(self):
        self.armageddon.send_cmd(self.armageddon.DOWN)

    def stop_movement(self):
        self.armageddon.send_cmd(self.armageddon.STOP)

    def fire(self):
        self.armageddon.send_cmd(self.armageddon.FIRE)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ArmageddonByArrows()
    myapp.show()
    sys.exit(app.exec_())
