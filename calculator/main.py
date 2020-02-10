from PySide2.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculator")

    window = QMainWindow()
    window.show()
    app.exec_()