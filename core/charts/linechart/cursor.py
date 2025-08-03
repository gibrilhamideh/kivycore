from kivy.event import EventDispatcher
from kivy.properties import ColorProperty, BooleanProperty, ObjectProperty, NumericProperty, ListProperty

class Cursor(EventDispatcher):

    cursor = ObjectProperty(None, allownone=True)
    '''
    `cursor`

    :attr:`cursor` is a :class:`~kivy.properties.ObjectProperty`
    '''

    cursor_color = ColorProperty([0, 0, 0, 0.65])
    '''
    `cursor_color`

    :attr:`cursor_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 0, 0, 1]`.
    '''

    cursor_width = NumericProperty(1)
    '''
    `cursor_width`

    :attr:`cursor_width` is a :class:`~kivy.properties.NumericProperty`
    '''

    cursor_info = ListProperty([])
    '''
    `cursor_info`

    :attr:`cursor_info` is a :class:`~kivy.properties.ListProperty`
    '''

    is_visible = BooleanProperty(True)
    """
    Whether the cursor is visible.

    :attr:`is_visible` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """