import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

ui, _ = loadUiType('ui/gold_calculator.ui')


class GoldCalc(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.calcute_button.clicked.connect(self.calc_gold)
        self.interest_rate.setText('7')
        self.tax_percentage.setText('9')
        self.percentage_wage.setText('0')

        self.interest_rate.textChanged.connect(self.format_input_text)
        self.tax_percentage.textChanged.connect(self.format_input_text)
        self.gold_18_calc.textChanged.connect(self.format_input_text)
        self.percentage_wage.textChanged.connect(self.format_input_text)
        self.ston_money.textChanged.connect(self.format_input_text)
        self.rials_wage.textChanged.connect(self.format_input_text)

    def calc_gold(self):
        # ======================= Inputs======================
        interest_rate_text = self.interest_rate.text().replace(',', '')
        tax_percentage_text = self.tax_percentage.text().replace(',', '')
        gold_18_text = self.gold_18_calc.text().replace(',', '')
        gold_weight_text = self.gold_weight.text()
        percentage_wage_text = self.percentage_wage.text()
        ston_money_text = self.ston_money.text().replace(',', '')
        rials_wage_text = self.rials_wage.text().replace(',', '')

        # Check if any input field is empty
        if not interest_rate_text or not tax_percentage_text or not gold_18_text \
                or not gold_weight_text or not percentage_wage_text:
            QMessageBox.warning(self, "Warning", "لطفا مقادیر ضروری را وارد کنید!")
            return

        try:
            # Convert input values to appropriate data types
            interest_rate = float(interest_rate_text)
            tax_percentage = float(tax_percentage_text)
            gold_18 = int(gold_18_text)
            gold_weight = float(gold_weight_text)
            percentage_wage = int(percentage_wage_text)
            if ston_money_text != '':
                ston_money = int(ston_money_text)
            if rials_wage_text != '':
                rials_wage = int(rials_wage_text)
        except ValueError:
            # If any input value is not a valid number, show an error message
            QMessageBox.warning(self, "Warning", "لطفا مقدار عددی وارد کنید!")
            return

        # ====================calculus========================
        if rials_wage_text == '':
            gold_wage = gold_weight * ((gold_18 * percentage_wage) / 100)
            self.gold_wage_calc.setText("{:,.0f}".format(gold_wage))
        else:
            gold_wage = rials_wage
            self.gold_wage_calc.setText("{:,.0f}".format(gold_wage))
        gold_value = gold_18 * gold_weight
        self.gold_value.setText("{:,.0f}".format(gold_value))
        total_interest = ((gold_value + gold_wage) * interest_rate) / 100
        self.total_interest.setText("{:,.0f}".format(total_interest))
        tax_amount = ((total_interest + gold_wage) * tax_percentage) / 100
        self.tax_amount.setText("{:,.0f}".format(tax_amount))
        if ston_money_text == '':
            total_value = gold_value + gold_wage + total_interest + tax_amount
            self.total_value.setText("{:,.0f}".format(total_value))
        else:
            total_value = gold_value + gold_wage + total_interest + tax_amount - ston_money
            self.total_value.setText("{:,.0f}".format(total_value))

        # def gold_wage(self):

    #     self.gold_18_calc.setText('0')
    #     gold_18 = int(self.gold_18_calc.text())
    #     self.percentage_wage.setText('0')
    #     percentage_wage = int(self.percentage_wage.text())
    #     gold_wage = (gold_18 * percentage_wage) / 100
    #     return gold_wage
    def format_input_text(self):
        sender = self.sender()  # Get the sender of the signal
        if sender.text():
            formatted_text = "{:,.0f}".format(float(sender.text().replace(',', '')))
            sender.setText(formatted_text)


# def main():
#     app = QApplication(sys.argv)
#     window = GoldCalc()
#     window.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()
