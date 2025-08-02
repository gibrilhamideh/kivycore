from kivy.properties import ColorProperty, BooleanProperty, VariableListProperty, AliasProperty
from kivy.event import EventDispatcher


class Axis(EventDispatcher):
    # ================================= # 
    #           Axis Styling
    # ================================= #  
    x_axis_color = ColorProperty([0, 0, 0, 1])
    '''
    `x_axis_color`

    :attr:`x_axis_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    do_axis_x = BooleanProperty(True)
    '''
    `do_axis_x`

    :attr:`do_axis_x` is a :class:`~kivy.properties.BooleanProperty`
    '''

    y_axis_color = ColorProperty([0, 0, 0, 1])
    '''
    `y_axis_color`

    :attr:`y_axis_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    do_axis_y = BooleanProperty(False)
    '''
    `do_axis_y`

    :attr:`do_axis_y` is a :class:`~kivy.properties.BooleanProperty`
    '''


    def get_axis_color(self):
        return self.x_axis_color, self.y_axis_color
    
    def set_axis_color(self, value):
        self.x_axis_color = self.y_axis_color = value


    axis_color = AliasProperty(get_axis_color, set_axis_color, bind=['x_axis_color', 'y_axis_color'])
    '''
    `axis_color`

    :attr:`axis_color` is an :class:`~kivy.properties.AliasProperty`
    '''