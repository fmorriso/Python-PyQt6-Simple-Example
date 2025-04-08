import sys
from PyQt6.QtWidgets import QApplication, QWidget

def get_python_version() -> str:
	return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

app = QApplication(sys.argv)

w = QWidget()
w.resize(800, 450)
w.setWindowTitle(f'HelloWorld using Python {get_python_version()}')
w.show()

sys.exit(app.exec())
