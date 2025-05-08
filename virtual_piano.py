from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
import mido
# pip install mido pygame
mido.set_backend("mido.backends.pygame")
output = mido.open_output()

class PianoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎹 Virtual Piano")
        self.setFixedSize(800, 100)
        self.notes = {
            "C4": 60,
            "C#4": 61,
            "D4": 62,
            "D#4": 63,
            "E4": 64,
            "F4": 65,
            "F#4": 66,
            "G4": 67,
            "G#4": 68,
            "A4": 69,
            "A#4": 70,
            "B4": 71,
            "C5": 72,
        }
        self.key_map = {
            Qt.Key_Z: 60,
            Qt.Key_S: 61,
            Qt.Key_X: 62,
        }
        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        for name, pitch in self.notes.items():
            button = QPushButton(name)
            button.setFixedSize(30, 80)
            layout.addWidget(button)

            button.pressed.connect(lambda p=pitch: self.play_note(p))
            button.released.connect(lambda p=pitch: self.stop_note(p))
        self.setCentralWidget(central_widget)

    def play_note(self, pitch):
        message = mido.Message("note_on", note=pitch, velocity=64)
        output.send(message)
    def stop_note(self, pitch):
        message = mido.Message("note_off", note=pitch, velocity=64)
        output.send(message)
    
    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
        if event.key() in self.key_map:
            pitch = self.key_map[event.key()]
            self.play_note(pitch)
    
    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return
        if event.key() in self.key_map:
            pitch = self.key_map[event.key()]
            self.stop_note(pitch)
if __name__ == "__main__":
    app = QApplication([])
    window = PianoWindow()
    window.show()
    app.exec()
