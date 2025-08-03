from kivy.properties import ColorProperty, BooleanProperty, VariableListProperty, AliasProperty
from kivy.event import EventDispatcher


class Grid(EventDispatcher):

    # ================================= # 
    #               Styling
    # ================================= # 
    grid_background_color = ColorProperty([1, 1, 1, 1])
    '''
    `grid_background_color`

    :attr:`grid_background_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    grid_color = ColorProperty([0, 0, 0, 0.1])
    '''
    `grid_color`

    :attr:`grid_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    do_grid_x = BooleanProperty(False)
    '''
    `do_grid_x`

    :attr:`do_grid_x` is a :class:`~kivy.properties.BooleanProperty`
    '''

    do_grid_y = BooleanProperty(True)
    '''
    `do_grid_y`

    :attr:`do_grid_y` is a :class:`~kivy.properties.BooleanProperty`
    '''

    padding = VariableListProperty([75, 75], length=4)
    '''
    `padding`
    
    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    '''



    # ================================= # 
    #          Positioning
    # ================================= # 
    def get_grid_x(self):
        x, y = self.to_local(self.x, self.y)
        return x + self.padding[0]

    def get_grid_y(self):
        x, y = self.to_local(self.x, self.y)
        return y + self.padding[2]

    def get_grid_top(self):
        x, y = self.to_local(self.x, self.y)
        return y + self.height - self.padding[3]

    def get_grid_right(self):
        x, y = self.to_local(self.x, self.y)
        return x + self.width - self.padding[1]

    def get_grid_pos(self):
        return self.get_grid_x(), self.get_grid_y()
    
    def get_grid_width(self):
        return self.width - self.padding[0] - self.padding[2]
    
    def get_grid_height(self):
        return self.height - self.padding[1] - self.padding[3]
    
    def get_grid_size(self):
        return self.get_grid_width(), self.get_grid_height()
    

    grid_x = AliasProperty(get_grid_x, bind=['padding'])
    '''
    `grid_x`

    :attr:`grid_x` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_y = AliasProperty(get_grid_y, bind=['padding'])
    '''
    `grid_y`

    :attr:`grid_y` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_top = AliasProperty(get_grid_top, bind=['padding', 'height'])
    '''
    `grid_top`

    :attr:`grid_top` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_right = AliasProperty(get_grid_right, bind=['padding', 'width'])
    '''
    `grid_right`

    :attr:`grid_right` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_pos = AliasProperty(get_grid_pos, bind=['padding'])
    '''
    `grid_pos`

    :attr:`grid_pos` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_width = AliasProperty(get_grid_width, bind=['padding', 'width'])
    '''
    `grid_width`

    :attr:`grid_width` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_height = AliasProperty(get_grid_height, bind=['padding', 'height'])
    '''
    `grid_height`

    :attr:`grid_height` is an :class:`~kivy.properties.AliasProperty`
    '''

    grid_size = AliasProperty(get_grid_size, bind=['padding', 'width', 'height'])
    '''
    `grid_size`

    :attr:`grid_size` is an :class:`~kivy.properties.AliasProperty`
    '''