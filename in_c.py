from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QSpinBox
from PySide6.QtCore import Qt
import time
import mido
import threading
import random
# pip install mido pygame
mido.set_backend("mido.backends.pygame")
output = mido.open_output("loopMIDI Port")

score = [
    [(60, 0.1), (64, 0.9), (60, 0.1), (64, 0.9), (60, 0.1), (64, 0.9)],
    [(60, 0.1), (64, 0.4), (65, 0.5), (64, 1)],
    [(0, 0.5), (64, 0.5), (65, 0.5), (64, 0.5)],
    [(0, 0.5), (64, 0.5), (65, 0.5), (67, 0.5)],
    [(64, 0.5), (65, 0.5), (67, 0.5), (0, 0.5)],
    [(72, 4)]
]

class InstrumentWidget(QWidget):
    def __init__(self, name, channel):
        super().__init__()
        self.name = name
        self.channel = channel
        self.speed = random.uniform(0.9, 1.1)
        self.is_playing = False
        self.current_sequence = 0
        self.label_instrument = QLabel(name)
        self.label_sequence = QLabel("Sequence: " + str(self.current_sequence))
        self.spin = QSpinBox()
        self.spin.setMaximum(len(score) - 1)
        self.spin.valueChanged.connect(self.change_sequence)
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.toggle_play)

        layout = QHBoxLayout()
        layout.addWidget(self.label_instrument)
        layout.addWidget(self.label_sequence)
        layout.addWidget(self.spin)
        layout.addWidget(self.play_button)
        self.setLayout(layout)
    
    def change_sequence(self, value):
        self.current_sequence = value
        self.label_sequence.setText("Sequence: " + str(self.current_sequence))

    def toggle_play(self):
        if self.is_playing:
            self.is_playing = False
            self.play_button.setText("Play")
        else:
            self.is_playing = True
            threading.Thread(target=self.play_loop, daemon=True).start()
            self.play_button.setText("Pause")
    def play_note(self, note, velocity=64, channel=0, duration=1):
        if note == 0:
            time.sleep(duration)
            return
        output.send(mido.Message("note_on", note=note, velocity=velocity, channel=channel))
        time.sleep(duration)
        output.send(mido.Message("note_off", note=note, velocity=velocity,channel=channel))
    def play_loop(self):
        while self.is_playing:
            for note, duration in score[self.current_sequence]:
                if not self.is_playing:
                    break
                self.play_note(note, channel=self.channel, duration=duration * self.speed)

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
