## Hello World

```python
import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec_()
```

For a widget application using PySide2, you must always start by importing the appropriate class from the _PySide2.QtWidgets_ module.
After the imports, you create a _QApplication_ instance. As Qt can receive arguments from command line, you may pass any argument to the _QApplication_ object. 
Usually, you don’t need to pass any arguments so you can leave it as is, or use the following approach:

```python
app = QApplication()
```

After the creation of the application object, we have created a _QLabel_ object.
A _QLabel_ is a widget that can present text (simple or rich, like html), and images:

```python
label = QLabel("<font color=red size=40>Hello World!</font>")
```
`
After creating the label, we call show() on it. 
`

Finally, we call _app.exec\_()_ to enter the Qt main loop and start to execute the Qt code.
