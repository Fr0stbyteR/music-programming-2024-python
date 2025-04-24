from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Example")

        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_click)

        self.setCentralWidget(button)

    def on_button_click(self):
        text1 = "Pikachu"
        text2 = "PikachuUUUUUUUU"
        text3 = 1233
        print(text1 + " " + text2 + text3)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()