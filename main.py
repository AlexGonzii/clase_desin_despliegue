import sys
from PySide6.QtWidgets import QApplication
from ui_main import CounterView
from logic import CounterLogic

class AppController:
    def __init__(self):
        self.view = CounterView()
        self.model = CounterLogic()

        # UI → lógica
        self.view.btn_increment.clicked.connect(self.model.increment)
        self.view.btn_decrement.clicked.connect(self.model.decrement)

        # lógica → UI
        self.model.valueChanged.connect(self.view.update_label)

    def run(self):
        self.view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.run()
    sys.exit(app.exec())