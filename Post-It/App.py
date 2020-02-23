from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
from PySide2.QtCore import Qt
import sys

from ui_mainwindow import Ui_MainWindow


def create_new_note(parent=None):
    window = MainWindow()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.closeButton.released.connect(self.delete_window)
        self.moreButton.released.connect(create_new_note)

        # Flags to store dragged-dropped
        self._drag_active = False
        self.show()

    def mousePressEvent(self, e):
        self.previous_pos = e.globalPos()

    def mouseMoveEvent(self, e):
        delta = e.globalPos() - self.previous_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previous_pos = e.globalPos()

        self._drag_active = True

    def mouseReleaseEvent(self, e):
        if self._drag_active:
            self._drag_active = False

    def delete_window(self):
        result = QMessageBox.question(self, "Confirm delete", "Are you sure you want to delete this note?")
        if result == QMessageBox.Yes:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Brown Note")
    app.setStyle("Fusion")

    # Custom brown palette.
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(188, 170, 164))
    palette.setColor(QPalette.WindowText, QColor(121, 85, 72))
    palette.setColor(QPalette.ButtonText, QColor(121, 85, 72))
    palette.setColor(QPalette.Text, QColor(121, 85, 72))
    palette.setColor(QPalette.Base, QColor(188, 170, 164))
    palette.setColor(QPalette.AlternateBase, QColor(188, 170, 164))
    app.setPalette(palette)

    window = MainWindow()

    app.exec_()
