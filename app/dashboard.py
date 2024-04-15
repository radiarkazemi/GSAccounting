import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

from QShamsiCalendarWidget import QShamsiCalendarWidget
from gold_calc import GoldCalc

ui, _ = loadUiType('ui/main_dashbord.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button_handler()
        self.calendar()
        self.digital_clock()
        self.current_price()

        # Set window size to match screen size
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(), screen.height())

        # Center the window on the screen
        self.move(screen.center() - self.rect().center())

    def button_handler(self):
        self.purchase_button.clicked.connect(self.show_message_box)
        self.sales_button.clicked.connect(self.show_message_box)
        self.customer_button.clicked.connect(self.show_message_box)
        self.calculation_button.clicked.connect(self.show_gold_calc)
        self.inventory_button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        QMessageBox.information(self, "Button Clicked", "Button works successfully")

    def calendar(self):
        self.calendar = QShamsiCalendarWidget(1350, 1450)
        self.calendar.setGeometry(10, 40, 330, 245)
        self.window().layout().addWidget(self.calendar)

    def digital_clock(self):
        # Start a timer to update the time display every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Initial display of the current time
        self.update_time()

    def update_time(self):
        # Get the current time
        current_time = QDateTime.currentDateTime()
        # Format the time as HH:MM:SS
        formatted_time = current_time.toString("hh:mm:ss")
        # Set the formatted time to the QLCDNumber
        self.lcdNumber.display(formatted_time)

    def current_price(self):
        self.onse_gold.setText('1,000')
        self.gold_18.setText('1,000')
        self.gold_24.setText('1,000')
        self.used_gold.setText('1,000')
        self.us_dolor.setText('1,000')
        self.emami_coin.setText('1,000')
        self.half_coin.setText('1,000')
        self.quarter_coin.setText('1,000')
        self.eur_europ.setText('1,000')
        self.try_turkey.setText('1,000')
        self.rub_russia.setText('1,000')
        self.bitcoin_us.setText('1,000')
        self.ethereum_us.setText('1,000')
        self.ripple_us.setText('1,000')
        self.cardano_us.setText('1,000')

    # ====================================gold price calc===================
    def show_gold_calc(self):
        self.window_gold_calc = GoldCalc()
        self.window_gold_calc.show()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
