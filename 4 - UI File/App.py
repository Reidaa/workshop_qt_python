import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QUiLoader().load("mainwindow.ui")

    window.show()

    sys.exit(app.exec_())
