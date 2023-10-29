import io
import sys

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
list = '''<?xml version="1.0" encoding="UTF-8"?>
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


class Fildword_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(menu)
        uic.loadUi(f, self)
        self.recordButton.clicked.connect(self.open_records)
        self.generatorButton.clicked.connect(self.generate)
        self.radioButton.clicked.connect(self.choosing_a_theme)
        self.radioButton_2.clicked.connect(self.choosing_a_theme)
        self.radioButton_3.clicked.connect(self.choosing_a_theme)
        self.radioButton_4.clicked.connect(self.choosing_a_theme)

    def open_records(self):
        self.Fildword_list_open = Fildword_list()
        self.Fildword_list_open.show()

    def generate(self):
        self.Fildword_tabel_open = Fildword_tabel()
        self.Fildword_tabel_open.show()

    def choosing_a_theme(self):
        pass


class Fildword_tabel(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(tabel)
        uic.loadUi(f, self)


class Fildword_list(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(list)
        uic.loadUi(f, self)


class Fildword_game(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(game)
        uic.loadUi(f, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Fildword_2 = Fildword_menu()
    Fildword_2.show()
    sys.exit(app.exec())
