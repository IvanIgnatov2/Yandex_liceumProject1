import io
import sqlite3
import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

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
      <widget class="QLabel" name="label">
       <property name="text">
        <string>TextLabel</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLCDNumber" name="lcdNumber_2"/>
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
   <string>MainWindow</string>
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
        <string>Тема 1</string>
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
        <string>Тема 2</string>
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
        <string>Тема 3</string>
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
        <string>Тема 4</string>
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
    <width>241</width>
    <height>202</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QListView" name="listView">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>1</y>
      <width>256</width>
      <height>201</height>
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
    <width>296</width>
    <height>306</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>10</y>
      <width>281</width>
      <height>281</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QTableWidget" name="tableWidget">
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
       <attribute name="verticalHeaderDefaultSectionSize">
        <number>25</number>
       </attribute>
       <attribute name="verticalHeaderMinimumSectionSize">
        <number>25</number>
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


class Filword_menu(QMainWindow):
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
        self.Fildword_list_open = True
        self.database_name = []
        self.letters_for_table = []
        self.list_of_tems_ids = []
        self.words_for_filword = []

    def open_records(self):
        self.Fildword_list_open = Filword_list()
        self.Fildword_list_open.show()

    def generate(self):
        Filword_tabel.generate_2(self)
        # Filword_game.start_time(self)

    def choosing_a_theme_1(self):
        self.database_name.append('database_1.db')

    def choosing_a_theme_2(self):
        self.database_name.append('database_2.db')

    def choosing_a_theme_3(self):
        self.database_name.append('database_3.db')

    def choosing_a_theme_4(self):
        self.database_name.append('database_4.db')


class Filword_tabel(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(tabel)
        uic.loadUi(f, self)
        self.letters_for_table = []
        self.list_of_tems_ids = []
        self.words_for_filword = []
        self.Fildword_tabel_open = True

    def generate_2(self):
        # print(self.database_name)
        for _ in range(10):
            self.letters_for_table.append([])
        for _ in range(self.spinBox.value()):
            self.list_of_tems_ids.append(randint(0, len(self.database_name) - 1))
        for list_ids in self.list_of_tems_ids:
            conn = sqlite3.connect(f'{self.database_name[list_ids]}')
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM words')
            row_count = cursor.fetchone()[0]
            conn.close()
            conn = sqlite3.connect('database_1.db')
            cursor = conn.cursor()
            id_for_table = randint(0, row_count)
            cursor.execute(f"SELECT word FROM words WHERE id = {id_for_table}")
            result = cursor.fetchone()
            self.words_for_filword.append(result[0])
            # Закрываем соединение с базой данных
            conn.close()
        # print(self.words_for_filword)
        counter = 0
        for word in self.words_for_filword:
            for letter in word:
                self.letters_for_table[counter].append(letter)
            counter += 1
        # print(self.letters_for_table)
        self.Fildword_tabel_open = Filword_tabel()
        self.Fildword_tabel_open.show()


class Filword_list(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(records_list)
        uic.loadUi(f, self)

    def correction(self):
        pass


class Filword_game(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(game)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.to_answer())
        self.pushButton_3.clicked.connect(self.end)
        self.Filword_tabel_open = True

    def to_answer(self):
        pass

    def end(self):
        pass

    def start_time(self):
        self.timer.start(1000)
        self.Filword_tabel_open = Filword_game()
        self.Filword_tabel_open.show()

    def update_time(self):
        time = self.label.text()
        time_list = time.split(':')
        hours, minutes, seconds = map(int, time_list)

        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1

            if minutes == 60:
                minutes = 0
                hours += 1

                if hours == 24:
                    hours = 0

        self.label.setText(f'{hours:02}:{minutes:02}:{seconds:02}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Fildword_2 = Filword_menu()
    Fildword_2.show()
    sys.exit(app.exec())

