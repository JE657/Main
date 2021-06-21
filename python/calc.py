# import sys
# import PyQt5.QtWidgets as qtw


# class Window(qtw.QWidget):

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Calc By Jank")
#         self.setGeometry(400, 300, 300, 400)

#         self.setLayout(qtw.QVBoxLayout())
#         # self.keypad()

#         self.show()


# def main():
#     app = qtw.QApplication(sys.argv)
#     win = Window()
#     app.exec_()


# main()


number = 1.57837
# print('{0}'.format(number, '.2f'))
print('{0:.2f}'.format(number))
print('%.2f' % number)
