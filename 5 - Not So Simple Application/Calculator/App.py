from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot
import operator

from ui_mainwindow import Ui_MainWindow

# Calculator state.
READY = 0
INPUT = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None

        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).released.connect(lambda v=n: self.input_number(v))

        self.pushButton_add.released.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.released.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.released.connect(lambda: self.operation(operator.mul))
        self.pushButton_div.released.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7

        self.pushButton_pc.released.connect(self.operation_pc)
        self.pushButton_eq.released.connect(self.equals)

        self.actionReset.triggered.connect(self.reset)
        self.pushButton_ac.released.connect(self.reset)

        self.pushButton_m.released.connect(self.memory_store)
        self.pushButton_mr.released.connect(self.memory_recall)

        self.memory = 0
        self.reset()

        self.show()

    def display(self):
        self.lcdNumber.display(self.stack[-1])

    @Slot()
    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    @Slot()
    def memory_store(self):
        self.memory = self.lcdNumber.value()

    @Slot()
    def memory_recall(self):
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()

    @Slot(int)
    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()

    def operation(self, op):
        if self.current_op:
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    @Slot()
    def operation_pc(self):
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()

    @Slot()
    def equals(self):
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()


if __name__ == '__main__':
    app = QApplication()
    app.setApplicationName("Calculator")

    window = MainWindow()
    app.exec_()
