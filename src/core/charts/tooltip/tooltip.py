import os

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import BooleanProperty, ColorProperty, ObjectProperty

from core.effects import Style
from paths import core_path

with open(
    os.path.join(core_path, "charts", "tooltip", "tooltip.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class Tooltip(Label, Style):


    chart = ObjectProperty(None, allownone=True)
    '''
    `chart`

    :attr:`chart` is a :class:`~kivy.properties.ObjectProperty`
    '''


    text_color = ColorProperty((0, 0, 0, 1))
    '''
    `text_color`

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    background_color = ColorProperty((0.2, 0.5, 1, 1))
    '''
    `background_color`

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty`
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

    def __init__(self, chart, **kwargs):
        super().__init__(**kwargs)

        self.chart = chart
        self.chart.bind(tooltip_text_color=self.setter('text_color'))
        self.chart.bind(tooltip_background_color=self.setter('background_color'))

        self.text_color = self.chart.tooltip_text_color
        self.background_color = self.chart.tooltip_background_color

    def open(self):
        """
        Opens the tooltip at the specified position with the given text.
        """

        if self.is_in_progress:
            self.animation.stop(self)
        
        self.is_in_progress = True
        self.animation = Animation(opacity=1.0, duration=0.2)
        self.animation.bind(on_complete=self.on_complete)
        self.animation.start(self)


    def dismiss(self):
        """
        Dismisses the tooltip with an animation.
        """
        if self.is_in_progress:
            self.animation.stop(self)

        self.is_in_progress = True
        self.animation = Animation(opacity=0, duration=0.2)
        self.animation.bind(on_complete=self.on_complete)
        self.animation.start(self)

    def on_complete(self, *args):
        """
        Called when the tooltip is done with its animation.
        """
        self.is_in_progress = False
