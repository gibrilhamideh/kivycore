from kivy.properties import ColorProperty, BooleanProperty, NumericProperty, OptionProperty, AliasProperty
from kivy.event import EventDispatcher

class Ticks(EventDispatcher):
    # ================================= # 
    #           Tick Styling
    # ================================= # 

    tick_position = OptionProperty('outside', options=('center', 'outside'))
    '''
    `tick_position`

    :attr:`tick_position` is a :class:`~kivy.properties.OptionProperty`
    '''

    x_ticks_color = ColorProperty([0, 0, 0, 1])
    '''
    `x_ticks_color`

    :attr:`x_ticks_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    x_tick_length = NumericProperty(8)
    '''
    `x_tick_length`

    :attr:`x_tick_length` is a :class:`~kivy.properties.NumericProperty`
    '''

    do_x_ticks = BooleanProperty(True)
    '''
    `do_x_ticks`

    :attr:`do_x_ticks` is a :class:`~kivy.properties.BooleanProperty`
    '''

    y_ticks_color = ColorProperty([0, 0, 0, 1])
    '''
    `y_ticks_color`

    :attr:`y_ticks_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    y_tick_length = NumericProperty(8)
    '''
    `y_tick_length`

    :attr:`y_tick_length` is a :class:`~kivy.properties.NumericProperty`
    '''

    do_y_ticks = BooleanProperty(True)
    '''
    `do_y_ticks`

    :attr:`do_y_ticks` is a :class:`~kivy.properties.BooleanProperty`
    '''

    def get_ticks_color(self):
        return self.x_ticks_color, self.y_ticks_color
    
    def set_ticks_color(self, value):
        self.x_ticks_color = self.y_ticks_color = value

    ticks_color = AliasProperty(get_ticks_color, set_ticks_color, bind=['x_ticks_color', 'y_ticks_color'])
    '''
    `ticks_color`

    :attr:`ticks_color` is an :class:`~kivy.properties.AliasProperty`
    '''

    # ================================= # 
    #          Axis Text Styling
    # ================================= # 
    x_tick_text_color = ColorProperty([0, 0, 0, 1])
    '''
    `x_tick_text_color`

    :attr:`x_tick_text_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    y_tick_text_color = ColorProperty([0, 0, 0, 0.65])
    '''
    `y_tick_text_color`

    :attr:`y_tick_text_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    def get_tick_text_color(self):
        return self.x_tick_text_color, self.y_tick_text_color

    def set_tick_text_color(self, value):
        self.x_tick_text_color = self.y_tick_text_color = value

    tick_text_color = AliasProperty(get_tick_text_color, set_tick_text_color, bind=['x_tick_text_color', 'y_tick_text_color'])
    '''
    `tick_text_color`

    :attr:`tick_text_color` is an :class:`~kivy.properties.AliasProperty`
    '''