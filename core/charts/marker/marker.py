from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, ListProperty, NumericProperty

from core.icon_definitions import icons

class Marker(RelativeLayout):

    chart = ObjectProperty(None, allownone=True)
    '''
    `chart`

    :attr:`chart` is a :class:`~kivy.properties.ObjectProperty`
    '''

    background_color = ListProperty([0.2, 0.5, 1, 1])
    '''
    `background_color`

    :attr:`background_color` is a :class:`~kivy.properties.ListProperty`
    '''

    selected_index = NumericProperty(0)
    '''
    `selected_index`

    :attr:`selected_index` is a :class:`~kivy.properties.NumericProperty`
    '''


    def __init__(self, chart, **kwargs):
        super().__init__(**kwargs)

        self.chart = chart

        self._dragging = False
        self._touch_offset = (0, 0)
        
        outer_icon = Label(color=self.background_color)
        outer_icon.font_size = 42
        outer_icon.markup = True
        outer_icon.text = f"[font=Icons]{icons['water'] if 'water' in icons else ''}[/font]"
        outer_icon.texture_update()

        self.size_hint = (None, None)
        self.size = outer_icon.texture_size

        inner_icon = Label()
        inner_icon.font_size = 12
        inner_icon.markup = True
        inner_icon.text = f"[font=Icons]{icons['file-chart'] if 'file-chart' in icons else ''}[/font]"
        inner_icon.y = -2

        self.add_widget(outer_icon)
        self.add_widget(inner_icon)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._dragging = True
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self._dragging:
            self.center_x = min(max((touch.x), self.chart.grid_x), self.chart.grid_right)
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if not self._dragging:
            return super().on_touch_up(touch)

        self._dragging = False
        lines = self.chart.line_info
        if not lines or not lines[0]:
            return True

        local_x = touch.x - self.chart.grid_x
        base_line = lines[0]
        closest_point = min(base_line, key=lambda item: abs(item['pos'][0] - (local_x + self.chart.grid_x)))
        index = base_line.index(closest_point)
        self.move(index)
        return True
    
    def move(self, value):
        lines = self.chart.line_info
        self.center_x = lines[0][value]['pos'][0]

        items = []
        for line in lines:
            items.append(line[self.selected_index])

        self.selected_index = value
        self.chart.dispatch('on_cursor_items', items)

    def move_left(self):
        index = self.selected_index - 1
        if self.is_index_allowed(index):
            self.move(index)

    def move_right(self):
        index = self.selected_index + 1
        if self.is_index_allowed(index):
            self.move(index)
        
    def is_index_allowed(self, index):
        """
        Checks if the index is within the allowed range of the chart.
        """
        return 0 <= index < len(self.chart.line_info[0]) if self.chart.line_info else False
        