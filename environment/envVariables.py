from pathlib import Path

ROOT_DIR = (Path(__file__).parent.parent)

RESOURCES_DIR = ROOT_DIR / 'resources'
STYLE_DIR = RESOURCES_DIR / 'style'
IMAGE_DIR = RESOURCES_DIR / 'images'

WINDOW_ICON_PATH = IMAGE_DIR / 'icons/app/app-icon.png'
LOGIN_STYLESHEET_PATH = STYLE_DIR / 'loginStyle.qss'
HOME_STYLESHEET_PATH = STYLE_DIR / 'homeStyle.qss'
CLIENTS_STYLESHEET_PATH = STYLE_DIR / 'clientsStyle.qss'
COLABORATORS_STYLESHEET_PATH = STYLE_DIR / 'colaboratorsStyle.qss'
PRODUCTS_STYLESHEET_PATH = STYLE_DIR / 'productsStyle.qss'
SALES_STYLESHEET_PATH = STYLE_DIR /'salesStyle.qss'
SUPPLIERS_STYLESHEET_PATH = STYLE_DIR /'suppliersStyle.qss'
APPLICATION_STYLESHEET_PATH = STYLE_DIR / 'applicationStyle.qss'


SPLASHSCREEN_PATH = IMAGE_DIR / 'splash-image.png'

LOGIN_IMAGE_PATH = IMAGE_DIR / 'login-image.png'
