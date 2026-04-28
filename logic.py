from PySide6.QtCore import QObject, Signal

class CounterLogic(QObject):
    valueChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._value = 0

    def increment(self):
        self._value += 1
        self.valueChanged.emit(self._value)

    def decrement(self):
        self._value -= 1
        self.valueChanged.emit(self._value)