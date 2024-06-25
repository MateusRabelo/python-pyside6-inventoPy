from pathlib import Path

ROOT_DIR = (Path(__file__).parent.parent)

RESOURCES_DIR = ROOT_DIR / 'resources'
STYLE_DIR = RESOURCES_DIR / 'style'

WINDOW_ICON_PATH = RESOURCES_DIR / 'images/icons/app-icon.png'
LOGIN_STYLESHEET_PATH = STYLE_DIR / 'loginStyle.qss'

SPLASHSCREEN_PATH = RESOURCES_DIR / 'images/splash-image.png'