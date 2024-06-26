from pathlib import Path

ROOT_DIR = (Path(__file__).parent.parent)

RESOURCES_DIR = ROOT_DIR / 'resources'
STYLE_DIR = RESOURCES_DIR / 'style'
IMAGE_DIR = RESOURCES_DIR / 'images'

WINDOW_ICON_PATH = IMAGE_DIR / 'icons/app/app-icon.png'
LOGIN_STYLESHEET_PATH = STYLE_DIR / 'loginStyle.qss'

SPLASHSCREEN_PATH = IMAGE_DIR / 'splash-image.png'

LOGIN_IMAGE_PATH = IMAGE_DIR / 'login-image.png'
