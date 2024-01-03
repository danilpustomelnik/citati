from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])

'''Інтерфейс програми'''
# параметри вікна програми
window = QWidget()
window.setStyleSheet('''QWidget{background:#00ffff;}''')
window.setWindowTitle('Цитатник')
window.resize(900, 600)

label1= QLabel('''Один в поле не воробей, туда сюда и сто рублей.
        Напиши свои цитаты.''')

text1=QTextEdit()
text1.setStyleSheet('''QTextEdit{background:#008080;}''')

text2=QLineEdit('')
text2.setStyleSheet('''QLineEdit{background:#008080;}''')

label2= QLabel('Подпиши свои великолепные цитаты (Имя Фамилия)')

b1=QPushButton("Ok")
b1.setStyleSheet('''QPushButton{background:#ff0000;}''')
v=QVBoxLayout()

v.addWidget(label1,alignment=Qt.AlignCenter)
v.addWidget(text1)
v.addWidget(text2)
v.addWidget(label2,alignment=Qt.AlignCenter)

v.addWidget(b1)


window.setLayout(v)

index=0
def babam():
    global index
    info_win=QMessageBox()
    info_win.setWindowTitle('Загрузка цитат')
    info_win.setText('Цитаты загружены, спасибо \n'+text2.text())
    info_win.exec_()
    with open("1.txt", "a",encoding="utf-8") as file:
        file.write("Имя: "+text2.text()+'\n')
        file.write("Цитаты: "+text1.toPlainText()+'\n')




# запуск програми
b1.clicked.connect(babam)
window.show()
app.exec_()