import sys

from PyQt6.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
from PyQt6.QtWidgets import QApplication, QWidget


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


print(f"Qt version: {QT_VERSION_STR}")
print(f"PyQt6 version: {PYQT_VERSION_STR}")

app = QApplication(sys.argv)

w = QWidget()
w.resize(800, 450)
w.setWindowTitle(f'HelloWorld using Python {get_python_version()}')
w.show()

sys.exit(app.exec())
