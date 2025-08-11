from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty

from resources.icons.md_icons import md_icons

class Marker(RelativeLayout):

    chart = ObjectProperty(None, allownone=True)
    '''
    `chart`

    :attr:`chart` is a :class:`~kivy.properties.ObjectProperty`
    '''

    selected_index = NumericProperty(0)
    '''
    `selected_index`

    :attr:`selected_index` is a :class:`~kivy.properties.NumericProperty`
    '''


    def __init__(self, chart, **kwargs):
        super().__init__(**kwargs)

        self.chart = chart
        
        self._touch_offset = (0, 0)
        
        outer_icon = Label(color=self.chart.marker_background_color)
        outer_icon.font_size = 42
        outer_icon.markup = True
        outer_icon.text = f"[font=Icons]{md_icons['water'] if 'water' in md_icons else ''}[/font]"
        outer_icon.texture_update()

        self.size_hint = (None, None)
        self.size = outer_icon.texture_size

        inner_icon = Label(color=self.chart.marker_text_color)
        inner_icon.font_size = 12
        inner_icon.markup = True
        inner_icon.text = f"[font=Icons]{md_icons['file-chart'] if 'file-chart' in md_icons else ''}[/font]"
        inner_icon.y = -2


        self.chart.bind(marker_text_color=inner_icon.setter('color'))
        self.chart.bind(marker_background_color=outer_icon.setter('color'))

        self.add_widget(outer_icon)
        self.add_widget(inner_icon)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._touch_offset = (self.center_x - touch.x, 0)
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.center_x = min(max(touch.x + self._touch_offset[0], self.chart.grid_x), self.chart.grid_right)
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)

            line_info = []
            for name, info in self.chart.dot_info.items():
                if info:  # make sure the list is not empty
                    line_info = info
                    break
            else:
                return True  # nothing to do, no valid data

            local_x = touch.x - self.chart.grid_x
            if not line_info:  # additional safety, just in case
                return True

            try:
                closest_point = min(line_info, key=lambda item: abs(item['pos'][0] - (local_x + self.chart.grid_x)))
                index = line_info.index(closest_point)
            except (ValueError, IndexError, KeyError):
                return True  # something unexpected happened, silently fail

            self.move(index)
            return True

        return super().on_touch_up(touch)
        
    def move(self, value):
        first_line_info = []
        for name, line in self.chart.dot_info.items():
            first_line_info = line
            break
        else:
            return  # No line info, abort

        # Step 2: Validate the index against that first line
        if not (0 <= value < len(first_line_info)):
            return

        # Step 3: Set marker position
        self.center_x = first_line_info[value]['pos'][0]
        self.selected_index = value

        # Step 4: Collect items for all lines
        items = {}
        for name, info in self.chart.dot_info.items():
            if 0 <= value < len(info):
                items[name] = info[value]

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

        if not self.chart.dot_info:
            return False
        
        line_info = None
        for name, info in self.chart.dot_info.items():
            line_info = info
            break

        else:
            return False
        

        return 0 <= index < len(line_info) if self.chart.dot_info else False
        