from kivy.uix.label import CoreLabel
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line, Rectangle, SmoothLine, Ellipse
from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty
)

from core.effects import Style
from core.charts.tooltip import Tooltip
from core.charts.linechart.line import ChartLine
from core.charts.linechart.grid import Grid
from core.charts.linechart.axis import Axis
from core.charts.linechart.tick import Ticks


class CoreLineChart(Style, ChartLine, Ticks, Axis, Grid, RelativeLayout):


    items: list[dict] = ListProperty()
    '''
    `items`

    :attr:`items` is a :class:`~kivy.properties.ListProperty`
    '''

    x_range = ListProperty([0, 24])
    '''
    `x_range`

    :attr:`x_range` is a :class:`~kivy.properties.ListProperty`
    '''

    x_ticks = NumericProperty(12)
    '''
    `x_ticks`

    :attr:`x_ticks` is a :class:`~kivy.properties.NumericProperty`
    '''

    y_left_range = ListProperty([0, 50])
    '''
    `y_left_range`

    :attr:`y_left_range` is a :class:`~kivy.properties.ListProperty`
    '''

    y_right_range = ListProperty([0, 4000])
    '''
    `y_right_range`

    :attr:`y_right_range` is a :class:`~kivy.properties.ListProperty`
    '''
    
    y_ticks = NumericProperty(16)
    '''
    `y_ticks`

    :attr:`y_ticks` is a :class:`~kivy.properties.NumericProperty`
    '''

    # ================================= #
    #             Test Data
    # ================================= #
    test_data = [
        (0, 22), (4, 24), (8, 26), (12, 30), (16, 28), (20, 25), (24, 23)
    ]

    test_data_1 = [
        (0, 13), (4, 15), (8, 24), (12, 8), (16, 17), (20, 31), (24, 32)
    ]

    test_data_2 = [
        (0, 1000), (4, 2450), (8, 4000), (12, 3250), (16, 3000), (20, 1350), (24, 1500)
    ]


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(
            pos=self.redraw,
            size=self.redraw,
            x_range=self.redraw,
            y_left_range=self.redraw,
            y_right_range=self.redraw
        )

    #  ================================= # 
    #            Redraw Method
    #  ================================= #          
    def redraw(self, *args):
        
        self.clear_widgets()
        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0, 1)

            if self.do_axis_x:
                self.draw_x_axis()

            if self.do_x_ticks:
                self.draw_x_ticks()

            if self.do_axis_y:
                self.draw_y_axis()
                self.draw_y_axis(placement='right')

            if self.do_y_ticks:
                self.draw_y_ticks()
                self.draw_y_ticks(placement='right')

            if self.do_grid_x:
                self.draw_x_grid()

            if self.do_grid_y:
                self.draw_y_grid()

            self.draw_line(self.test_data, color=(0, 1, 0, 1), width=2)
            self.draw_line(self.test_data_1, color=(0, 0, 1, 1), width=2)
            self.draw_line(self.test_data_2, color=(1, 0, 0, 1), width=2, placement='right')

        self.tooltip = Tooltip()
        self.add_widget(self.tooltip)
            
    def draw_line(self, points, color=(1, 0, 0, 1), width=2, placement='left'):
        Color(*color)
        pixel_points = []

        if placement == 'left':
            for x_val, y_val in points:
                norm_x = (x_val - self.x_range[0]) / (self.x_range[1] - self.x_range[0])
                norm_y = (y_val - self.y_left_range[0]) / (self.y_left_range[1] - self.y_left_range[0])

                px = self.grid_x + norm_x * self.grid_width
                py = self.grid_y + norm_y * self.grid_height
                pixel_points.extend([px, py])

                dot_radius = self.dot_radius
                Ellipse(pos=(px - dot_radius, py - dot_radius), size=(dot_radius * 2, dot_radius * 2))

                self.line_info.append({
                    'data': (x_val, y_val),
                    'pos': (px, py),
                    'norm': (norm_x, norm_y)
                })

            SmoothLine(points=pixel_points, width=width)

        elif placement == 'right':
            for x_val, y_val in points:
                norm_x = (x_val - self.x_range[0]) / (self.x_range[1] - self.x_range[0])
                norm_y = (y_val - self.y_right_range[0]) / (self.y_right_range[1] - self.y_right_range[0])

                px = self.grid_x + norm_x * self.grid_width
                py = self.grid_y + norm_y * self.grid_height

                dot_radius = self.dot_radius
                pixel_points.extend([px, py])
                Ellipse(pos=(px - dot_radius, py - dot_radius), size=(dot_radius * 2, dot_radius * 2))

                self.line_info.append({
                    'data': (x_val, y_val),
                    'pos': (px, py),
                    'norm': (norm_x, norm_y)
                })

            SmoothLine(points=pixel_points, width=width)

    def draw_y_grid(self):
        
        x = self.grid_x
        y = self.grid_y
        height = self.grid_height
        right = self.grid_right

        Color(*self.grid_color)
        for i in range(self.y_ticks + 1):
            norm = i / self.y_ticks
            py = y + norm * height
            
            Line(points=[x, py, right, py], width=1)

    def draw_x_grid(self):

        x = self.grid_x
        y = self.grid_y
        width = self.grid_width
        top = self.grid_top

        Color(*self.grid_color)
        for i in range(self.x_ticks + 1):
            norm = i / self.x_ticks
            px = x + norm * width
            Line(points=[px, y, px, top], width=1)

    def draw_y_axis(self, placement='left'):

        
        top = self.grid_top
        if placement == 'left':
            x = self.grid_x
            y = self.grid_y

        elif placement == 'right':
            x = self.grid_right
            y = self.grid_y

        Color(*self.y_axis_color)
        Line(points=[x, y, x, top], width=1)

    def draw_x_axis(self):
        x = self.grid_x
        y = self.grid_y

        Color(*self.x_axis_color)
        Line(points=[x, y, self.grid_right, y], width=1)

    def draw_y_ticks(self, placement='left'):

        if placement == 'left':

            step_y = (self.y_left_range[1] - self.y_left_range[0]) / self.y_ticks
            x = self.grid_x
            y = self.grid_y
            height = self.grid_height
            length = self.y_tick_length

            if self.tick_position == 'outside':
                x -= length
            elif self.tick_position == 'center':
                x -= length / 2

            for i in range(self.y_ticks + 1):

                val = self.y_left_range[0] + i * step_y
                norm = (val - self.y_left_range[0]) / (self.y_left_range[1] - self.y_left_range[0])
                py = y + norm * height
                Color(*self.y_ticks_color)
                Line(points=[x, py, x + length, py], width=1)

                self.draw_tick_text(str(int(val)), x , py, axis='y', position='left')

        elif placement == 'right':

            step_y = (self.y_right_range[1] - self.y_right_range[0]) / self.y_ticks
            x = self.grid_right
            y = self.grid_y
            height = self.grid_height
            length = self.y_tick_length

            if self.tick_position == 'center':
                x -= length / 2

            for i in range(self.y_ticks + 1):
                val = self.y_right_range[0] + i * step_y
                norm = (val - self.y_right_range[0]) / (self.y_right_range[1] - self.y_right_range[0])
                py = y + norm * height

                Color(*self.y_ticks_color)
                Line(points=[x, py, x + length, py], width=1)
                self.draw_tick_text(str(int(val)), x, py, axis='y', position='right')

    def draw_x_ticks(self):

        Color(*self.x_ticks_color)
        
        x = self.grid_x
        y = self.grid_y
        width = self.grid_width
        step_x = (self.x_range[1] - self.x_range[0]) / self.x_ticks

        length = self.x_tick_length

        if self.tick_position == 'outside':
            y -= length
        elif self.tick_position == 'center':
            y -= length / 2

        for i in range(self.x_ticks + 1):
            val = self.x_range[0] + i * step_x
            norm = (val - self.x_range[0]) / (self.x_range[1] - self.x_range[0])
            px = x + norm * width 


            Color(*self.x_ticks_color)
            Line(points=[px, y, px, y + length], width=1)

            self.draw_tick_text(str(int(val)), px, y - 20, axis='x')

    def draw_tick_text(self, text, x, y, axis, position=None):
        label = CoreLabel(text=text, font_size=12, color=(1, 1, 1, 1))
        label.refresh()
        texture = label.texture
        tw, th = texture.size

        if axis == 'x':
            color = self.x_tick_text_color
            x -= tw / 2

        elif axis == 'y':
            color = self.y_tick_text_color
            y -= th / 2

            if position == 'left':
                x -= tw + 2
            elif position == 'right':
                x += self.y_tick_length + 2

        Color(*color)
        Rectangle(texture=texture, pos=(x, y), size=texture.size)

    def on_items(self, instance, value):
        self.line_info.clear()
        self.redraw()

