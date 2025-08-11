from __future__ import annotations
from typing import Type


from kivy.app import App as KivyApp
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty
from theme import Theme

class App(KivyApp):

    theme: Type[Theme] = ObjectProperty(None)
    '''
    Theme object to manage the application's theme.
    
    :attr:`theme` is a :class:`~kivy.properties.ObjectProperty`
    '''

    screen_cls: list = ListProperty([])
    '''
    List of screen classes to be used in the application.

    :attr:`screen_cls` is a :class:`~kivy.properties.ListProperty`
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme = Theme()
        self.theme.mode = 'Dark'  # Default theme mode