## Using UI Files

This page describes the use of **QtDesigner** to create graphical interfaces for your Qt for Python project. 
You will need **QtDesigner** to design and modify your interface (UI file).

In case you haven't listen, to install **QtDesigner** follow this [link](http://bit.ly/qt-designer-win
) on Windows or _sudo apt install qtcreator_ on Ubuntu.


In **QtDesigner**, create a new Qt Design Form, choose “Main Window” for template. 
And save as _mainwindow.ui_. 
Add a _QPushButton_ to the center of the centralwidget.

Your file (mainwindow.ui) should look something like this:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralWidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>80</y>
      <width>201</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menuBar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>400</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QToolBar" name="mainToolBar">
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
  </widget>
  <widget class="QStatusBar" name="statusBar"/>
 </widget>
 <layoutdefault spacing="6" margin="11"/>
 <resources/>
 <connections/>
</ui>
```

Now we are ready to decide how to use the **UI file** from Python.

## Generating a Python class

Another option to interact with a **UI file** is to generate a Python class from it. 
This is possible thanks to the _pyside2-uic_ tool.
To use this tool, you need to run the following command on a console

Linux:
```shell script
pyside2-uic mainwindow.ui > ui_mainwindow.py
```

Windows:
```shell script
pyside2-uic mainwindow.ui -o ui_mainwindow.py
```

We redirect all the output of the command to a file called _ui_mainwindow.py_, which will be imported directly:

```python
from ui_mainwindow import Ui_MainWindow
```

Now to use it, we should create a personalized class for our widget to **setup** this generated design.

To understand the idea, let’s take a look at the whole code:

```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
```

Our class contains only two new lines that are in charge of loading the generated python class from the UI file:

```python
self.ui = Ui_MainWindow()
self.ui.setupUi(self)
```

`You must run pyside2-uic again every time you make changes to the UI file.`

## Loading it directly

You can also load the UI file directly, drawback is that you cannot extend the loaded class, you will have to use it as is.

We will need a class from the **QtUiTools** module:
```python
from PySide2.QtUiTools import QUiLoader
```
The _QUiLoader_ lets us load the **ui file** dynamically and use it right away:
```python
ui_file = QFile("mainwindow.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)
window.show()
```

Since PySide accepts high-level Python objects a lot of the time, your UI loader function can be simplified to something like:
```python
window = QUiLooader().load("mainwindow.ui")
window.show()
```