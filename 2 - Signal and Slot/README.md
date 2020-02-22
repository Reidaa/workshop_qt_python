In this tutorial, we’ll show you how to handle **signals and slots** using Qt for Python. 
**Signals and slots** is a Qt feature that lets your graphical widgets communicate with other graphical widgets or your python code. 
Our application creates a button that logs the _Button clicked, Hello!_ message to the python console each time you click it.

Let’s start by importing the necessary PySide2 classes and python sys module:

```python
import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot
```

Let’s also create a python function that logs the message to the console:

```python
# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")
```

`
The @Slot() is a decorator that identifies a function as a slot. It is not important to understand why for now, but use it always to avoid unexpected behavior. 
`

Now, as mentioned in previous examples you must create the _QApplication_ to run your PySide2 code:

```python
# Create the Qt Application
app = QApplication(sys.argv)
```

Let’s create the clickable button, which is a _QPushButton_ instance. 
To label the button, we pass a python string to the constructor:

```python
# Create a button
button = QPushButton("Click me")
```

Before we show the button, we must connect it to the _say_hello()_ function that we defined earlier.
There are two ways of doing this; using the old style or the new style, which is more pythonic. 
Let’s use the new style in this case. 
You can find more information about both these styles in the [Signals and Slots in PySide2 wiki page](https://wiki.qt.io/Qt_for_Python_Signals_and_Slots).

The _QPushButton_ has a predefined signal called **clicked**, which is triggered every time the button is clicked. We’ll connect this signal to the _say_hello()_ function:

```python
# Connect the button to the function
button.clicked.connect(say_hello)
```

Finally, we show the button and start the Qt main loop:

```python
# Show the button
button.show()
# Run the main Qt loop
app.exec_()
```