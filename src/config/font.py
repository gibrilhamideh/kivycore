import os

from paths import resources_path
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase

def set_fonts():
    """
    Set the fonts for the application.
    """
    # Set the font path for the application
    font_path = os.path.join(resources_path, 'fonts')
    resource_add_path(font_path)
    
    # Register the fonts
    LabelBase.register('arial', 'arial.ttf')
    LabelBase.register('Icons', 'materialdesignicons-webfont.ttf')
