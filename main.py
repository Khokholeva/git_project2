import sqlite3

import sys
import csv

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        result = self.cur.execute("""SELECT * FROM Coffee""").fetchall()
        result.sort()
        for i, a in enumerate(result):
            for j, elem in enumerate(a):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))

        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())