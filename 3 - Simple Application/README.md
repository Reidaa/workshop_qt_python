## Creating a Simple PySide2 Dialog Application

This tutorial shows how to build a simple dialog with some basic widgets.
The idea is to let users provide their name in a _QLineEdit_, and the dialog greets them on click of a _QPushButton_.

Let us just start with a simple stub that creates and shows a dialog.
This stub is updated during the course of this tutorial, but you can use this stub as is if you need to:

```python
import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
```

The imports aren’t new to you, the same for the creation of the _QApplication_ and the execution of the Qt main loop. The only novelty here is the **class definition**.

You can create any class that subclasses PySide2 widgets. 
In this case, we are subclassing _QDialog_ to define a custom dialog, which we name as **Form**.
We have also implemented the _init()_ method that calls the _QDialog_’s init method with the parent widget, if any. 
Also, the new _setWindowTitle()_ method just sets the title of the dialog window.
In _main()_, you can see that we are creating a _Form object_ and showing it to the world.

## Create the Widgets

We are going to create two widgets: a _QLineEdit_ where users can enter their name, and a _QPushButton_ that prints the contents of the _QLineEdit_.
So, let’s add the following code to the _init()_ method of our **Form**:

````python
# Create widgets
self.edit = QLineEdit("Write my name here..")
self.button = QPushButton("Show Greetings")
````

It’s obvious from the code that both widgets will show the corresponding texts.

## Create a layout to organize the Widgets


Qt comes with layout-support that helps you organize the widgets in your application.
In this case, let’s use _QVBoxLayout_ to lay out the widgets vertically.
Add the following code to the _init()_ method, after creating the widgets:
```python
# Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(self.edit)
layout.addWidget(self.button)
# Set dialog layout
self.setLayout(layout)
```

So, we create the layout, add the widgets with _addWidget()_, and finally we say that our **Form** will have our _QVBoxLayout_ as its layout.

## Create the function to greet and connect the Button

Finally, we just have to add a function to our custom **Form** and connect our button to it.
Our function will be a part of the **Form**, so you have to add it after the _init()_ function:
````python
# Greets the user
def greetings(self):
    print ("Hello {}".format(self.edit.text()))
````
Our function just prints the contents of the _QLineEdit_ to the python console.
We have access to the text by means of the _QLineEdit.text()_ method.

Now that we have everything, we just need to connect the _QPushButton_ to the _Form.greetings()_ method.
To do so, add the following line to the _init()_ method:
````python
# Add button signal to greetings slot
self.button.clicked.connect(self.greetings)
````
Once executed, you can enter your name in the _QLineEdit_ and watch the console for greetings.
