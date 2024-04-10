from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *
app = QApplication([])
main_win = QWidget()
glob = True
a = [['Взломщик компьютерных программ','Как называется человек — фанат компьютерных игр','«Мозг» компьютера'],
['Хакер','Геймер','Процессор'],
['Програмист','Хакер','Видеокарта'],
['Взломщик','Програмист','Материнская плата'],
['Геймер','админестратор','Жесткий диск']]
text = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
button1 = QRadioButton('2005')
button2 = QRadioButton('2010')
button3 = QRadioButton('2015')
button4 = QRadioButton('2020')
answer = [button1,button2,button3,button4]
def ask(question,right_ansver,wrong1,wrong2,wrong3):
    shuffle(answer)
    answer[0].setText(right_ansver)
    answer[1].setText(wrong1)
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)
    text.setText(question)
    return answer
point = 0
r = 0
ask(a[0][0],a[1][0],a[2][0],a[3][0],a[4][0])

def test():
    global r
    global glob
    if 'Ответить' == button5.text():
        if answer[0].isChecked():
            if a[1][r] == answer[0].text():
                winer()
            else:
                not_winer()

        elif answer[1].isChecked():
            if a[1][r] == answer[1].text():
                winer()
            else:
                not_winer()
        elif answer[2].isChecked():
            if a[1][r] == answer[2].text():
                winer()
            else:
                not_winer()
        elif answer[3].isChecked():
            if a[1][r] == answer[3].text():
                winer()
            else:
                not_winer()
        else:
            not_winer()
        show_result()
        button5.setText('Следующий')
    else:
        if r < 2:
            r += 1
        else:
            text4.setText(str(point))
            p.show()
            d.hide()
            q.hide()
            button5.hide()
            text.hide()
            glob = False
        ask(a[0][r],a[1][r],a[2][r],a[3][r],a[4][r])
        if glob:
            button5.setText(text2)
            show_question()
            button5.setText('Ответить')
        
def show_question():
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)
    q.hide()
    d.show()
def show_result():
    d.hide()
    q.show()
def winer():
    global point
    text3.setText('Правильно!')
    point += 1
def not_winer():
    text3.setText('Не правильно!')

main_win.setWindowTitle('Определитель победителя')
text2 = 'Ответить'
text3 = QLabel('Правильно или неправельно?')
text4 = QLabel(str(point))
text5 = QLabel('Число набраных очков')

button5 = QPushButton(text2)

RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

q = QGroupBox()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line7 = QVBoxLayout()
line5.addWidget(text3,alignment = Qt.AlignCenter)
line6.addWidget(text4,alignment = Qt.AlignCenter)
line7.addLayout(line5)
line7.addLayout(line6)
q.setLayout(line7)
q.hide()

p = QGroupBox()
line8 = QHBoxLayout()
line9 = QHBoxLayout()
line10 = QVBoxLayout()
line8.addWidget(text5,alignment = Qt.AlignCenter)
line9.addWidget(text4,alignment = Qt.AlignCenter)
line10.addLayout(line8)
line10.addLayout(line9)
p.setLayout(line10)
p.hide()


d = QGroupBox()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line_3 = QVBoxLayout()
line4 = QVBoxLayout()
line2.addWidget(button1,alignment = Qt.AlignCenter)
line2.addWidget(button2,alignment = Qt.AlignCenter)
line3.addWidget(button3,alignment = Qt.AlignCenter)
line3.addWidget(button4,alignment = Qt.AlignCenter)
line1.addWidget(text,alignment = Qt.AlignCenter)
line_3.addLayout(line1)
line_3.addWidget(q)
line4.addLayout(line2)
line4.addLayout(line3)
d.setLayout(line4)
line_3.addWidget(p)
line_3.addWidget(d)
line_3.addWidget(button5,alignment = Qt.AlignCenter)
main_win.setLayout(line_3)




button5.clicked.connect(test)
main_win.show()
app.exec()