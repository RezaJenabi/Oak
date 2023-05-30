import sys

from PyQt6.QtWidgets import QApplication

from Src.Services.Presentation.Oak.Oak import Oak as Oak


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Oak()
    window.show()
    sys.exit(app.exec())
