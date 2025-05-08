from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QSpinBox
from PySide6.QtCore import Qt
import mido
# pip install mido pygame
mido.set_backend("mido.backends.pygame")
output = mido.open_output()

class InstrumentWidget(QWidget):
    def __init__(self, name, channel):
        super().__init__()
        self.name = name
        self.channel = channel
        self.current_sequence = 0
        self.label_instrument = QLabel(name)
        self.label_sequence = QLabel("Sequence: " + str(self.current_sequence))
        self.spin = QSpinBox()
        self.play_button = QPushButton("Play")

        layout = QHBoxLayout()
        layout.addWidget(self.label_instrument)
        layout.addWidget(self.label_sequence)
        layout.addWidget(self.spin)
        layout.addWidget(self.play_button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("In C")

        self.instruments = [
            InstrumentWidget("Piano", 0),
            InstrumentWidget("Flute", 1),
            InstrumentWidget("Violin", 2)
        ]

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        for instrument in self.instruments:
            layout.addWidget(instrument)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
