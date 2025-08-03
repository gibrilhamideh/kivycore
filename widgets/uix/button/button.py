import os
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import StringProperty

from core.button import CoreButton
from core.icon_definitions import icons

from resources import widgets_path


with open(
    os.path.join(widgets_path, "uix", "button", "button.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())

class ElevatedButton(CoreButton):
    text_key = StringProperty()
    """
    Key for translation lookup.

    :attr:`text_key` is a :class:`~kivy.properties.StringProperty`
    """

class IconButton(CoreButton):
    icon_markup = StringProperty()
    """
    Markup string for the icon.

    :attr:`icon_markup` is a :class:`~kivy.properties.StringProperty`
    """
    
    def on_icon(self, instance, value):
        if value:
            if value in icons:
                value = icons[value]
            else:
                value = ''
                Logger.error(f"Icon '{value}' not found in icons.")

            self.icon_markup = f'[font=Icons]{value}[/font]'
        else:
            self.icon_markup = ''

    def on_font_size(self, instance, value):
        """Fired when the value of :attr:`font_size` changes."""
        
        size = value * 1.5
        self.size = [size, size]
        self.radius = [size / 2]


class FloatingButton(CoreButton):
    icon_markup = StringProperty()
    """
    Markup string for the icon.

    :attr:`icon_markup` is a :class:`~kivy.properties.StringProperty`
    """

    def on_icon(self, instance, value):
        if value:
            if value in icons:
                value = icons[value]
            else:
                value = ''
                Logger.error(f"Icon '{value}' not found in icons.")

            self.icon_markup = f'[font=Icons]{value}[/font]'
        else:
            self.icon_markup = ''