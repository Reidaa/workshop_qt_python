Comme pour tout framework, commencez par faire une fenetre affichant «Hello World».

Voici un exemple simple d'une application Hello World dans PySide2:

```python
import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec_()
```

For a widget application using PySide2, you must always start by importing the appropriate class from the PySide2.QtWidgets module.

After the imports, you create a QApplication instance. As Qt can receive arguments from command line, you may pass any argument to the QApplication object. Usually, you don’t need to pass any arguments so you can leave it as is, or use the following approach:

```python
app = QApplication([])
```

After the creation of the application object, we have created a QLabel object. A QLabel is a widget that can present text (simple or rich, like html), and images:

```python
label = QLabel("<font color=red size=40>Hello World!</font>")
```
```
Note:
   After creating the label, we call show() on it. 
```

Finally, we call app.exec_() to enter the Qt main loop and start to execute the Qt code. In reality, it is only here where the label is shown, but this can be ignored for now.