from __future__ import annotations
from typing import Type

from kivy.core.window import Window
from kivy.properties import ObjectProperty
from core.app import CoreApp


from widgets.uix.theme import Theme

class Main(CoreApp):

    theme: Type[Theme] = ObjectProperty(None)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme = Theme()
        self.theme.mode = 'Light'

        Window.size = (1200, 800)


if __name__ == "__main__":
    Main().run() 
