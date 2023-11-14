import io
import sqlite3
import sys
from random import randint

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

game = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>353</width>
    <height>146</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="formLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>351</width>
      <height>141</height>
     </rect>
    </property>
    <layout class="QFormLayout" name="formLayout">
     <item row="0" column="0">
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Ответить</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="lineEdit"/>
     </item>
     <item row="2" column="0">
      <widget class="QLineEdit" name="lineEdit_2">
       <property name="text">
        <string>Слов осталось:</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QLCDNumber" name="lcdNumber"/>
     </item>
     <item row="3" column="0">
      <widget class="QPushButton" name="pushButton_3">
       <property name="text">
        <string>Сдать</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QPushButton" name="pushButton_2">
       <property name="text">
        <string>Начать</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLabel" name="label">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
menu = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>353</width>
    <height>253</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Menu</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="formLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>351</width>
      <height>231</height>
     </rect>
    </property>
    <layout class="QFormLayout" name="formLayout">
     <item row="2" column="0">
      <widget class="QPushButton" name="generatorButton">
       <property name="text">
        <string>Создать</string>
       </property>
      </widget>
     </item>
     <item row="5" column="0">
      <widget class="QLineEdit" name="lineEditcolvo_slov">
       <property name="text">
        <string>Количество слов:</string>
       </property>
      </widget>
     </item>
     <item row="5" column="1">
      <widget class="QSpinBox" name="spinBox"/>
     </item>
     <item row="6" column="0">
      <widget class="QRadioButton" name="radioButton">
       <property name="text">
        <string>выбрать</string>
       </property>
      </widget>
     </item>
     <item row="6" column="1">
      <widget class="QLineEdit" name="lineEdit">
       <property name="text">
        <string>Тема 1: География</string>
       </property>
      </widget>
     </item>
     <item row="7" column="0">
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>выбрать</string>
       </property>
      </widget>
     </item>
     <item row="7" column="1">
      <widget class="QLineEdit" name="lineEdit_2">
       <property name="text">
        <string>Тема 2: История</string>
       </property>
      </widget>
     </item>
     <item row="8" column="0">
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>выбрать</string>
       </property>
      </widget>
     </item>
     <item row="8" column="1">
      <widget class="QLineEdit" name="lineEdit_3">
       <property name="text">
        <string>Тема 3: Общество</string>
       </property>
      </widget>
     </item>
     <item row="9" column="0">
      <widget class="QRadioButton" name="radioButton_4">
       <property name="text">
        <string>выбрать</string>
       </property>
      </widget>
     </item>
     <item row="9" column="1">
      <widget class="QLineEdit" name="lineEdit_4">
       <property name="text">
        <string>Тема 4: Дом</string>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QPushButton" name="recordButton">
       <property name="text">
        <string>Рекорды</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
records_list = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>381</width>
    <height>228</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>0</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Показать рекорды</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>231</width>
      <height>191</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
tabel = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>401</width>
    <height>328</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>10</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Начать</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>279</width>
      <height>279</height>
     </rect>
    </property>
    <property name="maximumSize">
     <size>
      <width>16777213</width>
      <height>16777215</height>
     </size>
    </property>
    <attribute name="horizontalHeaderDefaultSectionSize">
     <number>25</number>
    </attribute>
    <attribute name="horizontalHeaderMinimumSectionSize">
     <number>25</number>
    </attribute>
    <attribute name="horizontalHeaderStretchLastSection">
     <bool>true</bool>
    </attribute>
    <attribute name="verticalHeaderDefaultSectionSize">
     <number>25</number>
    </attribute>
    <attribute name="verticalHeaderMinimumSectionSize">
     <number>25</number>
    </attribute>
    <attribute name="verticalHeaderStretchLastSection">
     <bool>true</bool>
    </attribute>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <row>
     <property name="text">
      <string/>
     </property>
    </row>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
    <column>
     <property name="text">
      <string/>
     </property>
    </column>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>40</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Начать(тест)</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
error = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>181</width>
    <height>47</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>10</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Повторить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
spin_box_value = 0
words = []
database_name = []
corr = False
minutes = 0
seconds = 0


class FilwordMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(menu)
        uic.loadUi(f, self)
        self.recordButton.clicked.connect(self.open_records)
        self.generatorButton.clicked.connect(self.generate)
        self.radioButton.toggled.connect(self.choosing_a_theme_1)
        self.radioButton_2.toggled.connect(self.choosing_a_theme_2)
        self.radioButton_3.toggled.connect(self.choosing_a_theme_3)
        self.radioButton_4.toggled.connect(self.choosing_a_theme_4)
        self.Fildword_list_open = QMainWindow(self)
        self.timer = QTimer(self)

        self.letters_for_table = []
        self.list_of_tems_ids = []
        self.words_for_filword = []
        self.filword = []
        self.info = []

        self.fl = True
        self.is_running = False

    def open_records(self):
        self.Fildword_list_open = FilwordList()
        self.Fildword_list_open.show()

    def generate(self):
        self.Filword_tabel_open = FilwordTabel()
        self.Filword_tabel_open.show()

        global spin_box_value
        if self.spinBox.value() < 11:
            spin_box_value = self.spinBox.value()
        else:
            spin_box_value = (self.spinBox.value()) % 10
        FilwordGame.start_timer(self)

    def choosing_a_theme_1(self):
        database_name.append('database_1.db')

    def choosing_a_theme_2(self):
        database_name.append('database_2.db')

    def choosing_a_theme_3(self):
        database_name.append('database_3.db')

    def choosing_a_theme_4(self):
        database_name.append('database_4.db')


class FilwordTabel(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(tabel)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.generate_2)
        self.pushButton_2.clicked.connect(self.generate_test)
        self.Filword_tabel_open = QMainWindow(self)

        self.letters_for_table = []
        self.list_of_tems_ids = []
        self.words_for_filword = []
        self.filword = []
        self.russian_alphabet = {}
        self.database_name = []
        self.info = []
        self.generation_3()

    def generate_test(self):
        global words
        words = ['таможня', 'демократия', 'сезоны', 'берег']
        filword_test = [['т', 'а', 'м', 'о', 'ж', 'н', 'я', [], 'д', 'с'], [[], [], [], [], [], [], [], [], 'е', 'е'],
                        [[], [], [], [], [], 'б', [], [], 'м', 'з'], [[], [], [], [], [], 'е', [], [], 'о', 'о'],
                        [[], [], [], [], [], 'р', [], [], 'к', 'н'], [[], [], [], [], [], 'е', [], [], 'р', 'ы'],
                        [[], [], [], [], [], 'г', [], [], 'а', []], [[], [], [], [], [], [], [], [], 'т', []],
                        [[], [], [], [], [], [], [], [], 'и', []], [[], [], [], [], [], [], [], [], 'я', []]]
        self.russian_alphabet = {
            1: 'а', 2: 'б', 3: 'в', 4: 'г', 5: 'д', 6: 'е', 7: 'ё', 8: 'ж', 9: 'з', 10: 'и', 11: 'й', 12: 'к', 13: 'л',
            14: 'м', 15: 'н', 16: 'о', 17: 'п', 18: 'р', 19: 'с', 20: 'т', 21: 'у', 22: 'ф', 23: 'х', 24: 'ц', 25: 'ч',
            26: 'ш', 27: 'щ', 28: 'ъ', 29: 'ы', 30: 'ь', 31: 'э', 32: 'ю', 33: 'я'
        }
        for i in range(len(filword_test)):
            for j in range(len(filword_test[i])):
                if str(filword_test[i][j]) == '[]':
                    filword_test[i][j] = self.russian_alphabet[randint(1, 33)]
        for i in range(len(filword_test)):
            for j in range(len(filword_test[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(filword_test[i][j])))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def generate_2(self):
        global words
        global spin_box_value, database_name
        for _ in range(spin_box_value):
            self.letters_for_table.append([])
        for _ in range(spin_box_value):
            self.list_of_tems_ids.append(randint(0, len(database_name) - 1))
        for list_ids in self.list_of_tems_ids:
            conn = sqlite3.connect(f'{database_name[list_ids]}')
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM words')
            row_count = cursor.fetchone()[0]
            conn.close()
            conn = sqlite3.connect(f'{database_name[list_ids]}')
            cursor = conn.cursor()
            id_for_table = randint(0, row_count)
            cursor.execute(f"SELECT word FROM words WHERE id = {id_for_table}")
            result = cursor.fetchone()
            self.words_for_filword.append(result[0])
            conn.close()
        counter = 0
        for word in self.words_for_filword:
            for letter in word:
                self.letters_for_table[counter].append(letter)
            counter += 1
        self.russian_alphabet = {
            1: 'а', 2: 'б', 3: 'в', 4: 'г', 5: 'д', 6: 'е', 7: 'ё', 8: 'ж', 9: 'з', 10: 'и', 11: 'й', 12: 'к', 13: 'л',
            14: 'м', 15: 'н', 16: 'о', 17: 'п', 18: 'р', 19: 'с', 20: 'т', 21: 'у', 22: 'ф', 23: 'х', 24: 'ц', 25: 'ч',
            26: 'ш', 27: 'щ', 28: 'ъ', 29: 'ы', 30: 'ь', 31: 'э', 32: 'ю', 33: 'я'
        }
        for i in range(10):
            self.filword.append([])
            for j in range(10):
                self.filword[i].append([])
        random_value = randint(1, 2)
        if random_value == 1:
            random_row = randint(0, 9)
            cou = 0
            for i in self.letters_for_table[0]:
                self.filword[random_row][cou] = i
                cou += 1
        else:
            random_colum = randint(0, 9)
            cou = 0
            for i in self.letters_for_table[0]:
                self.filword[cou][random_colum] = i
                cou += 1
        self.generation_3()
        for i in range(len(self.filword)):
            for j in range(len(self.filword[i])):
                if str(self.filword[i][j]) == '[]':
                    self.filword[i][j] = self.russian_alphabet[randint(1, 33)]
        for i in range(len(self.filword)):
            for j in range(len(self.filword[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.filword[i][j])))
        words = self.words_for_filword
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def generation_3(self):
        try:
            for word_cords in range(1, len(self.letters_for_table)):
                flag_cnd = False
                random_value = randint(1, 2)
                if random_value == 1:
                    if len(self.words_for_filword[word_cords]) != 10:
                        delta = randint(0, 10 - len(self.words_for_filword[word_cords]))
                    else:
                        delta = 0
                    for _ in range(10000):
                        random_row = randint(0, 9)
                        cou = 0
                        flag = True
                        for _ in self.words_for_filword[word_cords]:
                            if str(self.filword[random_row][cou + delta - 1]) == '[]':
                                pass
                            else:
                                flag = False
                            cou += 1
                        if flag:
                            cou = 0
                            for i in self.words_for_filword[word_cords]:
                                self.filword[random_row][cou + delta - 1] = i
                                cou += 1
                            flag_cnd = True
                        if flag_cnd:
                            break
                else:
                    if len(self.words_for_filword[word_cords]) != 10:
                        delta = randint(0, 10 - len(self.words_for_filword[word_cords]))
                    else:
                        delta = 0
                    for _ in range(10000):
                        random_colum = randint(0, 9)
                        cou = 0
                        flag = True
                        for _ in self.words_for_filword[word_cords]:
                            if str(self.filword[cou + delta - 1][random_colum]) == '[]':
                                pass
                            else:
                                flag = False
                        if flag:
                            cou = 0
                            for i in self.words_for_filword[word_cords]:
                                self.filword[cou + delta - 1][random_colum] = i
                                cou += 1
                            flag_cnd = True
                        if flag_cnd:
                            break
        except Exception:
            print('Ошибка генерации')


class FilwordList(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(records_list)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.correction_2)

    def correction(self):
        global corr
        corr = True

    def correction_2(self):
        try:
            global corr
            if corr:
                for i in range(1, 11):
                    conn = sqlite3.connect('records.db')
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT record FROM records WHERE id = {i}")
                    result = cursor.fetchone()
                    additional_text = f'{i}: {int(result[0]) // 60}:{int(result[0]) % 60}\n'
                    current_text = self.textEdit.toPlainText()
                    self.textEdit.setText(current_text + additional_text)
                    conn.close()
                    # Задаётся текст для textEdit (максимум 10 результатов по времени)
        except Exception:
            pass

class FilwordGame(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(game)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.to_answer)
        self.pushButton_3.clicked.connect(self.end)
        self.Filword_tabel_open = ()
        self.pushButton_2.clicked.connect(self.start_timer)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.Fildword_list_open = FilwordList()

        self.is_running = False
        self.fl = True

        self.time_elapsed = 0
        self.time_str = ''
        self.stop_timer()
        self.x = 1

    def to_answer(self):
        if self.lineEdit.text() in words:
            self.lcdNumber.display(str(len(words) - self.x))
            self.x += 1
        else:
            self.Filword_error_open = Error()
            self.Filword_error_open.show()
            self.lineEdit.setText('')

    def end(self):
        if self.is_running and self.x > len(words):
            self.stop_timer()
            conn = sqlite3.connect('records.db')
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    record TEXT
                )
            """)
            cursor.execute("INSERT INTO records (record) VALUES (?)", (self.time_elapsed,))
            conn.commit()
            conn.close()
        FilwordList.correction(self)
        self.Fildword_list_open = FilwordList()
        self.Fildword_list_open.show()
        # создаётся база данных для рекордов и заканчивается выполнение филворда,
        # чтобы посмотреть свои рекорды и запустить новый филворд нужно запустить заново

    def start_timer(self):
        self.x = 1
        if not self.is_running:
            self.timer.start(1000)  # Запуск таймера с интервалом 1 секунда
            self.is_running = True
        if self.fl is True:
            self.Filword_game_open = FilwordGame()
            self.Filword_game_open.show()
            self.fl = False

    def update_timer(self):
        global minutes, seconds
        self.time_elapsed += 1
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        self.time_str = f"{minutes:02}:{seconds:02}"
        self.label.setText(self.time_str)

    def stop_timer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False


class Error(QDialog):
    def __init__(self):
        super().__init__()
        f = io.StringIO(error)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.error)

    def error(self):
        self.Filword_error_open = Error()
        self.Filword_error_open.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Fildword_2 = FilwordMenu()
    Fildword_2.show()
    sys.exit(app.exec())
