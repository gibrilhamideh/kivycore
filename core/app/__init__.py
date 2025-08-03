
import os

from resources import data_path
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase

from .app import CoreApp

# Set the font path for the application
font_path = os.path.join(data_path, 'fonts')
resource_add_path(font_path)

# Register the fonts
LabelBase.register('arial', 'arial.ttf')
LabelBase.register('Icons', 'materialdesignicons-webfont.ttf')