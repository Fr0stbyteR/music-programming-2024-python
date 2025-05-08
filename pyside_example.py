from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hit Me !!")
        self.setFixedSize(300, 100)

        self.buttonClicked = 0

        button = QPushButton()
        button.setText("Clicked: " + str(self.buttonClicked))
        button.setStyleSheet("background-color: black; color: yellow;")
        button.clicked.connect(self.on_button_click)
        self.button = button
        
        self.setCentralWidget(button)

    def on_button_click(self):
        self.buttonClicked += 1
        self.button.setText("Clicked: " + str(self.buttonClicked))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window2 = MainWindow()
    window.show()
    window2.show()
    app.exec()
