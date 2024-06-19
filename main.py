import sys
from PySide6 import QtWidgets
from app.splashScreen import SplashScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = SplashScreen()
    main_window.show()
    sys.exit(app.exec())
