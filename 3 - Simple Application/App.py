import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create widgets
        self.edit = QLineEdit("Write your name here")
        self.button = QPushButton("Show Greetings")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

        # Show the form
        self.show()

    # Greets the user
    def greetings(self):
        print("Hello %s" % self.edit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())
