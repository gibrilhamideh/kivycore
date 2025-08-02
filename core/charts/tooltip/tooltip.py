import os

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import BooleanProperty, ColorProperty, ObjectProperty

from core.effects import Style

from resources import core_path

with open(
    os.path.join(core_path, "charts", "tooltip", "tooltip.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class Tooltip(Label, Style):


    text_color = ColorProperty((0, 0, 0, 1))
    '''
    `text_color`

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    is_in_progress = BooleanProperty(False)
    '''
    `is_in_progress`

    :attr:`is_in_progress` is a :class:`~kivy.properties.BooleanProperty`
    '''

    animation = ObjectProperty(None, allownone=True)
    '''
    `animation`

    :attr:`animation` is a :class:`~kivy.properties.ObjectProperty`
    '''
    

    def open(self, x, y, text):
        """
        Opens the tooltip at the specified position with the given text.
        """

        if self.is_in_progress:
            self.animation.stop(self)
        
        self.text = text
        self.texture_update()

        size = self.texture_size
        self.pos = (x, y)

        self.is_in_progress = True
        self.animation = Animation(size=size, opacity=1.0, duration=0.2)
        self.animation.bind(on_complete=self.on_complete)
        self.animation.start(self)


    def dismiss(self):
        """
        Dismisses the tooltip with an animation.
        """
        if self.is_in_progress:
            self.animation.stop(self)

        self.is_in_progress = True
        self.animation = Animation(opacity=0, size=(0, 0), duration=0.2)
        self.animation.bind(on_complete=self.on_complete)
        self.animation.start(self)

    def on_complete(self, *args):
        """
        Called when the tooltip is done with its animation.
        """
        self.is_in_progress = False
