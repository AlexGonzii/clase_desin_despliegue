from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class CounterView(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)

        self.setWindowTitle("Contador")

        self.label = QLabel("0")
        self.label.setStyleSheet("font-size: 30px; text-align: center;")

        self.btn_increment = QPushButton("Incrementar")
        self.btn_decrement = QPushButton("Decrementar")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_increment)
        layout.addWidget(self.btn_decrement)

        self.setLayout(layout)

    def update_label(self, value):
        self.label.setText(str(value))