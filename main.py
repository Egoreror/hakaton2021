import asyncio
from qasync import QEventLoop, asyncSlot

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QBasicTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtGui import QPixmap
from qt_material import apply_stylesheet

from menuMain import menuMain

import time
import sys
import pandas as pd
from functools import partial

class planApp(menuMain):
    def __init__(self):
        menuMain.__init__(self)

        self.pushButton_grup_0.clicked.connect(partial(self.change_menu, num = 0))
        self.pushButton_grup_0.clicked.connect(partial(self.input_plan, name = '607-11', who = 'stud'))
        self.pushButton_grup_1.clicked.connect(partial(self.change_menu, num = 0))
        self.pushButton_grup_1.clicked.connect(partial(self.input_plan, name = '607-12', who = 'stud'))

        self.pushButton_person_0.clicked.connect(partial(self.change_menu, num = 1))
        self.pushButton_person_0.clicked.connect(partial(self.input_plan, name = 'Фёдоров Д. А.', who = 'teacher'))
        self.pushButton_person_1.clicked.connect(partial(self.change_menu, num = 1))
        self.pushButton_person_1.clicked.connect(partial(self.input_plan, name = 'Дубовик А. О.', who = 'teacher'))
        self.pushButton_person_2.clicked.connect(partial(self.change_menu, num = 1))
        self.pushButton_person_2.clicked.connect(partial(self.input_plan, name = 'Назина Н. Б.', who = 'teacher'))
        self.pushButton_person_3.clicked.connect(partial(self.change_menu, num = 1))
        self.pushButton_person_3.clicked.connect(partial(self.input_plan, name = 'Хадынская А. А.', who = 'teacher'))

        self.label_2.setPixmap(QPixmap("surgulogo.png"))

        self.group_stack = {}
        self.group_stack['понедельник'] = {}
        self.group_stack['вторник'] = {}
        self.group_stack['среда'] = {}
        self.group_stack['четверг'] = {}
        self.group_stack['пятница'] = {}
        self.group_stack['суббота'] = {}
 
        self.group_stack['понедельник']['Корпус'] = [self.label_0_1_1_0, self.label_0_1_4_0, self.label_0_1_7_0, self.label_0_1_10_0, self.label_0_1_13_0, self.label_0_1_16_0, self.label_0_1_19_0, self.label_0_1_22_0]
        self.group_stack['понедельник']['Дисциплина'] = [self.label_0_1_2_0, self.label_0_1_5_0, self.label_0_1_8_0, self.label_0_1_11_0, self.label_0_1_14_0, self.label_0_1_17_0, self.label_0_1_20_0, self.label_0_1_23_0]
        self.group_stack['понедельник']['Преподаватель'] = [self.label_0_1_3_0, self.label_0_1_6_0, self.label_0_1_9_0, self.label_0_1_12_0, self.label_0_1_15_0, self.label_0_1_18_0, self.label_0_1_21_0, self.label_0_1_24_0]

        self.group_stack['вторник']['Корпус'] = [self.label_0_1_1_1, self.label_0_1_4_1, self.label_0_1_7_1, self.label_0_1_10_1, self.label_0_1_13_1, self.label_0_1_16_1, self.label_0_1_19_1, self.label_0_1_22_1]
        self.group_stack['вторник']['Дисциплина'] = [self.label_0_1_2_1, self.label_0_1_5_1, self.label_0_1_8_1, self.label_0_1_11_1, self.label_0_1_14_1, self.label_0_1_17_1, self.label_0_1_20_1, self.label_0_1_23_1]
        self.group_stack['вторник']['Преподаватель'] = [self.label_0_1_3_1, self.label_0_1_6_1, self.label_0_1_9_1, self.label_0_1_12_1, self.label_0_1_15_1, self.label_0_1_18_1, self.label_0_1_21_1, self.label_0_1_24_1]

        self.group_stack['среда']['Корпус'] = [self.label_0_1_1_2, self.label_0_1_4_2, self.label_0_1_7_2, self.label_0_1_10_2, self.label_0_1_13_2, self.label_0_1_16_2, self.label_0_1_19_2, self.label_0_1_22_2]
        self.group_stack['среда']['Дисциплина'] = [self.label_0_1_2_2, self.label_0_1_5_2, self.label_0_1_8_2, self.label_0_1_11_2, self.label_0_1_14_2, self.label_0_1_17_2, self.label_0_1_20_2, self.label_0_1_23_2]
        self.group_stack['среда']['Преподаватель'] = [self.label_0_1_3_2, self.label_0_1_6_2, self.label_0_1_9_2, self.label_0_1_12_2, self.label_0_1_15_2, self.label_0_1_18_2, self.label_0_1_21_2, self.label_0_1_24_2]

        self.group_stack['четверг']['Корпус'] = [self.label_0_1_1_3, self.label_0_1_4_3, self.label_0_1_7_3, self.label_0_1_10_3, self.label_0_1_13_3, self.label_0_1_16_3, self.label_0_1_19_3, self.label_0_1_22_3]
        self.group_stack['четверг']['Дисциплина'] = [self.label_0_1_2_3, self.label_0_1_5_3, self.label_0_1_8_3, self.label_0_1_11_3, self.label_0_1_14_3, self.label_0_1_17_3, self.label_0_1_20_3, self.label_0_1_23_3]
        self.group_stack['четверг']['Преподаватель'] = [self.label_0_1_3_3, self.label_0_1_6_3, self.label_0_1_9_3, self.label_0_1_12_3, self.label_0_1_15_3, self.label_0_1_18_3, self.label_0_1_21_3, self.label_0_1_24_3]

        self.group_stack['пятница']['Корпус'] = [self.label_0_1_1_4, self.label_0_1_4_4, self.label_0_1_7_4, self.label_0_1_10_4, self.label_0_1_13_4, self.label_0_1_16_4, self.label_0_1_19_4, self.label_0_1_22_4]
        self.group_stack['пятница']['Дисциплина'] = [self.label_0_1_2_4, self.label_0_1_5_4, self.label_0_1_8_4, self.label_0_1_11_4, self.label_0_1_14_4, self.label_0_1_17_4, self.label_0_1_20_4, self.label_0_1_23_4]
        self.group_stack['пятница']['Преподаватель'] = [self.label_0_1_3_4, self.label_0_1_6_4, self.label_0_1_9_4, self.label_0_1_12_4, self.label_0_1_15_4, self.label_0_1_18_4, self.label_0_1_21_4, self.label_0_1_24_4]

        self.group_stack['суббота']['Корпус'] = [self.label_0_1_1_5, self.label_0_1_4_5, self.label_0_1_7_5, self.label_0_1_10_5, self.label_0_1_13_5, self.label_0_1_16_5, self.label_0_1_19_5, self.label_0_1_22_5]
        self.group_stack['суббота']['Дисциплина'] = [self.label_0_1_2_5, self.label_0_1_5_5, self.label_0_1_8_5, self.label_0_1_11_5, self.label_0_1_14_5, self.label_0_1_17_5, self.label_0_1_20_5, self.label_0_1_23_5]
        self.group_stack['суббота']['Преподаватель'] = [self.label_0_1_3_5, self.label_0_1_6_5, self.label_0_1_9_5, self.label_0_1_12_5, self.label_0_1_15_5, self.label_0_1_18_5, self.label_0_1_21_5, self.label_0_1_24_5]

        self.teach_stack = {}
        self.teach_stack['понедельник'] = {}
        self.teach_stack['вторник'] = {}
        self.teach_stack['среда'] = {}
        self.teach_stack['четверг'] = {}
        self.teach_stack['пятница'] = {}
        self.teach_stack['суббота'] = {}

        self.teach_stack['понедельник']['Корпус'] = [self.label_1_1_1_0, self.label_1_1_4_0, self.label_1_1_7_0, self.label_1_1_10_0, self.label_1_1_13_0, self.label_1_1_16_0, self.label_1_1_19_0, self.label_1_1_22_0]
        self.teach_stack['понедельник']['Дисциплина'] = [self.label_1_1_2_0, self.label_1_1_5_0, self.label_1_1_8_0, self.label_1_1_11_0, self.label_1_1_14_0, self.label_1_1_17_0, self.label_1_1_20_0, self.label_1_1_23_0]
        self.teach_stack['понедельник']['Преподаватель'] = [self.label_1_1_3_0, self.label_1_1_6_0, self.label_1_1_9_0, self.label_1_1_12_0, self.label_1_1_15_0, self.label_1_1_18_0, self.label_1_1_21_0, self.label_1_1_24_0]

        self.teach_stack['вторник']['Корпус'] = [self.label_1_1_1_1, self.label_1_1_4_1, self.label_1_1_7_1, self.label_1_1_10_1, self.label_1_1_13_1, self.label_1_1_16_1, self.label_1_1_19_1, self.label_1_1_22_1]
        self.teach_stack['вторник']['Дисциплина'] = [self.label_1_1_2_1, self.label_1_1_5_1, self.label_1_1_8_1, self.label_1_1_11_1, self.label_1_1_14_1, self.label_1_1_17_1, self.label_1_1_20_1, self.label_1_1_23_1]
        self.teach_stack['вторник']['Преподаватель'] = [self.label_1_1_3_1, self.label_1_1_6_1, self.label_1_1_9_1, self.label_1_1_12_1, self.label_1_1_15_1, self.label_1_1_18_1, self.label_1_1_21_1, self.label_1_1_24_1]

        self.teach_stack['среда']['Корпус'] = [self.label_1_1_1_2, self.label_1_1_4_2, self.label_1_1_7_2, self.label_1_1_10_2, self.label_1_1_13_2, self.label_1_1_16_2, self.label_1_1_19_2, self.label_1_1_22_2]
        self.teach_stack['среда']['Дисциплина'] = [self.label_1_1_2_2, self.label_1_1_5_2, self.label_1_1_8_2, self.label_1_1_11_2, self.label_1_1_14_2, self.label_1_1_17_2, self.label_1_1_20_2, self.label_1_1_23_2]
        self.teach_stack['среда']['Преподаватель'] = [self.label_1_1_3_2, self.label_1_1_6_2, self.label_1_1_9_2, self.label_1_1_12_2, self.label_1_1_15_2, self.label_1_1_18_2, self.label_1_1_21_2, self.label_1_1_24_2]

        self.teach_stack['четверг']['Корпус'] = [self.label_1_1_1_3, self.label_1_1_4_3, self.label_1_1_7_3, self.label_1_1_10_3, self.label_1_1_13_3, self.label_1_1_16_3, self.label_1_1_19_3, self.label_1_1_22_3]
        self.teach_stack['четверг']['Дисциплина'] = [self.label_1_1_2_3, self.label_1_1_5_3, self.label_1_1_8_3, self.label_1_1_11_3, self.label_1_1_14_3, self.label_1_1_17_3, self.label_1_1_20_3, self.label_1_1_23_3]
        self.teach_stack['четверг']['Преподаватель'] = [self.label_1_1_3_3, self.label_1_1_6_3, self.label_1_1_9_3, self.label_1_1_12_3, self.label_1_1_15_3, self.label_1_1_18_3, self.label_1_1_21_3, self.label_1_1_24_3]

        self.teach_stack['пятница']['Корпус'] = [self.label_1_1_1_4, self.label_1_1_4_4, self.label_1_1_7_4, self.label_1_1_10_4, self.label_1_1_13_4, self.label_1_1_16_4, self.label_1_1_19_4, self.label_1_1_22_4]
        self.teach_stack['пятница']['Дисциплина'] = [self.label_1_1_2_4, self.label_1_1_5_4, self.label_1_1_8_4, self.label_1_1_11_4, self.label_1_1_14_4, self.label_1_1_17_4, self.label_1_1_20_4, self.label_1_1_23_4]
        self.teach_stack['пятница']['Преподаватель'] = [self.label_1_1_3_4, self.label_1_1_6_4, self.label_1_1_9_4, self.label_1_1_12_4, self.label_1_1_15_4, self.label_1_1_18_4, self.label_1_1_21_4, self.label_1_1_24_4]

        self.teach_stack['суббота']['Корпус'] = [self.label_1_1_1_5, self.label_1_1_4_5, self.label_1_1_7_5, self.label_1_1_10_5, self.label_1_1_13_5, self.label_1_1_16_5, self.label_1_1_19_5, self.label_1_1_22_5]
        self.teach_stack['суббота']['Дисциплина'] = [self.label_1_1_2_5, self.label_1_1_5_5, self.label_1_1_8_5, self.label_1_1_11_5, self.label_1_1_14_5, self.label_1_1_17_5, self.label_1_1_20_5, self.label_1_1_23_5]
        self.teach_stack['суббота']['Преподаватель'] = [self.label_1_1_3_5, self.label_1_1_6_5, self.label_1_1_9_5, self.label_1_1_12_5, self.label_1_1_15_5, self.label_1_1_18_5, self.label_1_1_21_5, self.label_1_1_24_5]


        self.clear_stud()
        self.clear_teach()

    def clear_stud(self):
        for i in self.group_stack:
            for j in self.group_stack[i]:
                for l in self.group_stack[i][j]:
                    # print(l)
                    ft = l.text()
                    font = QtGui.QFont()
                    font.setPointSize(11)
                    l.setFont(font)
                    # if ft == 'TextLabel':
                    l.setText(' ')

    def clear_teach(self):
        for i in self.teach_stack:
            for j in self.teach_stack[i]:
                for l in self.teach_stack[i][j]:
                    # print(l)
                    ft = l.text()
                    font = QtGui.QFont()
                    font.setPointSize(11)
                    l.setFont(font)
                    # if ft == 'TextLabel':
                    l.setText(' ')

    def change_menu(self, num):
        self.stackedWidget.setCurrentIndex(num)

    def input_plan(self, name, who):
        # g607_11 = pd.read_excel('project\\plan\\607-11.xlsx')
        # g607_12 = pd.read_excel('project\\plan\\607-12.xlsx')
        all_lesson = pd.read_excel('project\\plan\\all.xlsx')

        self.clear_stud()
        self.clear_teach()
        if who == 'stud':
            for i in range(len(all_lesson)):
                wal = all_lesson.loc[i,]
                if wal['группа'] == name:
                    try:
                        self.group_stack[wal['день']]['Корпус'][int(wal['пара'])-1].setText(wal['кабинет'])
                        self.group_stack[wal['день']]['Дисциплина'][int(wal['пара'])-1].setText(wal['дисциплина'])
                        self.group_stack[wal['день']]['Преподаватель'][int(wal['пара'])-1].setText(wal['преподователь'])
                    except Exception as e:
                        print(e)

        elif who == 'teacher':
            for i in range(len(all_lesson)):
                wal = all_lesson.loc[i,]
                if name in wal['преподователь']:
                    print(name, wal['преподователь'])
                    try:
                        self.teach_stack[wal['день']]['Корпус'][int(wal['пара'])-1].setText(wal['группа'])
                        self.teach_stack[wal['день']]['Дисциплина'][int(wal['пара'])-1].setText(wal['кабинет'])
                        self.teach_stack[wal['день']]['Преподаватель'][int(wal['пара'])-1].setText(wal['дисциплина'])
                    except Exception as e:
                        print(e)

def windowLauncher():
    app = QtWidgets.QApplication(sys.argv)
    # apply_stylesheet(app, theme='dark_orange.xml')
    apply_stylesheet(app, team[10])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = planApp()
    w.show()
    
    loop.run_forever()

team = ['dark_amber.xml', # 0
        'dark_blue.xml', # 1
        'dark_cyan.xml', # 2
        'dark_lightgreen.xml', # 3
        'dark_pink.xml', # 4
        'dark_purple.xml', # 5
        'dark_red.xml', # 6
        'dark_teal.xml', # 7
        'dark_yellow.xml', # 8
        'light_amber.xml', # 9
        'light_blue.xml', # 10
        'light_cyan.xml', # 11
        'light_cyan_500.xml', # 12
        'light_lightgreen.xml', # 13
        'light_pink.xml', # 14
        'light_purple.xml', # 15
        'light_red.xml', # 16
        'light_teal.xml', # 17
        'light_yellow.xml'] # 18

if __name__ == '__main__':
    try:
        windowLauncher()
    except Exception as e:
        with open('log.txt', 'a+') as f:
            f.write('\n' + str(time.time) + '--' + str(e))