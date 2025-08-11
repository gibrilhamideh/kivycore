from __future__ import annotations
from typing import Callable, Type

import random

from kivy.uix.label import CoreLabel
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line, Rectangle, SmoothLine, Ellipse
from kivy.properties import (
    ListProperty,
    NumericProperty,
    DictProperty,
    ObjectProperty,
    ColorProperty,
    BooleanProperty,
    OptionProperty,
    AliasProperty,
    VariableListProperty,
    StringProperty
)


from core.effects import Style
from core.charts.marker import Marker
from core.charts.tooltip import Tooltip

class CoreLineChart(Style, RelativeLayout):

    # ================================= # 
    #           Axis Styling
    # ================================= #  

    do_axis_x = BooleanProperty(True)
    '''
    `do_axis_x`

    :attr:`do_axis_x` is a :class:`~kivy.properties.BooleanProperty`
    '''

    x_range = ListProperty([0, 23])
    '''
    `x_range`

    :attr:`x_range` is a :class:`~kivy.properties.ListProperty`
    '''

    x_ticks = NumericProperty(12)
    '''
    `x_ticks`

    :attr:`x_ticks` is a :class:`~kivy.properties.NumericProperty`
    '''

    x_axis_color = ColorProperty([0, 0, 0, 1])
    '''
    `x_axis_color`

    :attr:`x_axis_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    do_axis_y = BooleanProperty(False)
    '''
    `do_axis_y`

    :attr:`do_axis_y` is a :class:`~kivy.properties.BooleanProperty`
    '''

    y_left_range = ListProperty([0, 50], allownone=True)
    '''
    `y_left_range`

    :attr:`y_left_range` is a :class:`~kivy.properties.ListProperty`
    '''

    y_left_formatter: Callable | None = ObjectProperty(None, allownone=True)
    '''
    `y_left_formatter`

    :attr:`y_left_formatter` is a callable that formats the left y-axis values.
    '''

    y_right_range = ListProperty(None, allownone=True)
    '''
    `y_right_range`

    :attr:`y_right_range` is a :class:`~kivy.properties.ListProperty`
    '''

    y_right_formatter: Callable | None = ObjectProperty(None, allownone=True)
    '''
    `y_right_formatter`

    :attr:`y_right_formatter` is a callable that formats the right y-axis values.
    '''
    
    y_ticks = NumericProperty(16)
    '''
    `y_ticks`

    :attr:`y_ticks` is a :class:`~kivy.properties.NumericProperty`
    '''

    y_axis_color = ColorProperty([0, 0, 0, 1])
    '''
    `y_axis_color`

    :attr:`y_axis_color` is a :class:`~kivy.properties.ColorProperty`
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

    y_tick_length = NumericProperty(0)
    '''
    `y_tick_length`

    :attr:`y_tick_length` is a :class:`~kivy.properties.NumericProperty`
    '''

    y_tick_label_spacing = NumericProperty(8)
    '''
    `y_tick_label_spacing`

    :attr:`y_tick_label_spacing` is a :class:`~kivy.properties.NumericProperty`
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
    # Info
    # ================================= #
    cursor = ObjectProperty(None, allownone=True)
    '''
    `cursor`

    :attr:`cursor` is a :class:`~kivy.properties.ObjectProperty`
    '''

    cursor_color = ColorProperty([0, 0, 0, 0.65])
    '''
    `cursor_color`

    :attr:`cursor_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    cursor_width = NumericProperty(1)
    '''
    `cursor_width`

    :attr:`cursor_width` is a :class:`~kivy.properties.NumericProperty`
    '''

    cursor_info = ListProperty([])
    '''
    `cursor_info` holds information about the cursor position and the data points it intersects.

    :attr:`cursor_info` is a :class:`~kivy.properties.ListProperty`
    '''

    tooltip: Type[Tooltip] = ObjectProperty(None)
    '''
    `tooltip`

    :attr:`tooltip` is a :class:`~kivy.properties.ObjectProperty`
    '''

    tooltip_text_color = ColorProperty((0, 0, 0, 1))
    '''
    `tooltip_text_color`

    :attr:`tooltip_text_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    tooltip_background_color = ColorProperty((0.2, 0.5, 1, 1))
    '''
    `tooltip_background_color`

    :attr:`tooltip_background_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    marker: Type[Marker] = ObjectProperty(None)
    '''
    `marker`

    :attr:`marker` is a :class:`~kivy.properties.ObjectProperty`
    '''

    marker_text_color = ColorProperty((0, 0, 0, 1))
    '''
    `marker_text_color`

    :attr:`marker_text_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    marker_background_color = ColorProperty((0.2, 0.5, 1, 1))
    '''
    `marker_background_color`

    :attr:`marker_background_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    dot_info: dict[str, dict] = DictProperty()
    '''
    `dot_info`

    :attr:`dot_info` is a :class:`~kivy.properties.ListProperty`
    '''

    dot_radius = NumericProperty(0)
    '''
    `dot_radius`

    :attr:`dot_radius` is a :class:`~kivy.properties.NumericProperty`
    '''

    touch_tolerance = NumericProperty(20)
    '''
    `touch_tolerance` is a property that defines the touch tolerance area for interacting with the tooltip

    :attr:`touch_tolerance` is a :class:`~kivy.properties.NumericProperty`
    '''


    # ================================= # 
    # Grid
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
    # Grid Position
    # ================================= # 
    def get_grid_x(self):
        x, y = self.to_local(self.x, self.y)
        return x + self.padding[0]

    def get_grid_y(self):
        x, y = self.to_local(self.x, self.y)
        return y + self.padding[3]
    
    def get_grid_right(self):
        x, y = self.to_local(self.x, self.y)
        return x + self.width - self.padding[2]
    
    def get_grid_top(self):
        x, y = self.to_local(self.x, self.y)
        return y + self.height - self.padding[1]
    
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

    # ================================= #
    # References
    # ================================= #
    color_instructions: dict = DictProperty({})
    '''

    :attr:`color_instructions` is a :class:`~kivy.properties.DictProperty`
    '''

    line_instructions: dict = DictProperty()
    '''
    `lines`

    :attr:`lines` is a :class:`~kivy.properties.DictProperty`
    '''

    focus_key = StringProperty(None, allownone=True)
    '''
    `focus_key`

    :attr:`focus_key` is a :class:`~kivy.properties.StringProperty`
    '''


    __events__ = ('on_cursor_items', )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.trigger = Clock.create_trigger(self.redraw, -1)

        self.bind(
            pos=self.trigger_redraw,
            size=self.trigger_redraw,
            x_range=self.trigger_redraw,
            y_left_range=self.trigger_redraw,
            y_right_range=self.trigger_redraw
        )

    #  ================================= # 
    #            Redraw Method
    #  ================================= #          
    def trigger_redraw(self, *args):
        self.trigger.cancel()
        self.trigger()

    def redraw(self, *args):

        self.clear_widgets()
        self.canvas.clear()
        with self.canvas:

            self.draw_grid_background()

            if self.do_axis_x:
                self.draw_x_axis()

            if self.do_x_ticks:
                self.color_instructions['x_ticks_color'] = Color(*self.x_ticks_color)
                self.draw_x_ticks()

            if self.do_axis_y:
                self.color_instructions['y_axis_color'] =  Color(*self.y_axis_color)

                if self.y_left_range is not None:
                    self.draw_y_axis()

                if self.y_right_range is not None:
                    self.draw_y_axis(placement='right')

            if self.do_y_ticks:
                self.color_instructions['y_ticks_color'] = Color(*self.y_ticks_color)

                if self.y_left_range is not None:
                    self.draw_y_ticks()

                if self.y_right_range is not None:
                    self.draw_y_ticks(placement='right')

            self.color_instructions['grid_color'] = Color(*self.grid_color)
            if self.do_grid_x:
                self.draw_x_grid()

            if self.do_grid_y:
                self.draw_y_grid()

            self.draw_cursor()

        if self.tooltip is None:
            self.tooltip = Tooltip(self)

        if self.marker is None:
            self.marker = Marker(self)
            self.marker.bind(center_x=self.on_marker_x)

        self.marker.top = self.grid_y
        self.marker.center_x = self.grid_x
        self.add_widget(self.marker)
        self.add_widget(self.tooltip)

    def draw_grid_background(self):
        self.color_instructions['grid_background'] = Color(*self.grid_background_color)
        Rectangle(pos=self.grid_pos, size=self.grid_size)

    def draw_y_grid(self):
        
        x = self.grid_x
        y = self.grid_y
        height = self.grid_height
        right = self.grid_right

        for i in range(self.y_ticks + 1):
            norm = i / self.y_ticks
            py = y + norm * height
            
            Line(points=[x, py, right, py], width=1)

    def draw_x_grid(self):

        x = self.grid_x
        y = self.grid_y
        width = self.grid_width
        top = self.grid_top

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

        
        Line(points=[x, y, x, top], width=1)

    def draw_x_axis(self):
        x = self.grid_x
        y = self.grid_y

        self.color_instructions['x_axis_color'] = Color(*self.x_axis_color)
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

                if self.y_left_formatter:
                    text = self.y_left_formatter(val)
                else:
                    text = str(int(val))

                Line(points=[x, py, x + length, py], width=1)
                self.draw_tick_text(text, x, py, axis='y', position='left')

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

                if self.y_right_formatter:
                    text = self.y_right_formatter(val)

                else:
                    text = str(int(val))

                Line(points=[x, py, x + length, py], width=1)
                self.draw_tick_text(text, x, py, axis='y', position='right')

    def draw_x_ticks(self):

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

            Line(points=[px, y, px, y + length], width=1)
            self.draw_tick_text(str(int(val)), px, y - 20, axis='x')

    def draw_tick_text(self, text, x, y, axis, position=None):
        label = CoreLabel(text=text, font_size=11, color=(1, 1, 1, 1))
        label.refresh()
        texture = label.texture
        tw, th = texture.size

        if axis == 'x':
            x -= tw / 2

        elif axis == 'y':
            y -= th / 2

            if position == 'left':
                x -= tw + self.y_tick_label_spacing
            elif position == 'right':
                x += self.y_tick_length + self.y_tick_label_spacing

        Rectangle(texture=texture, pos=(x, y), size=texture.size)

    def draw_cursor(self):
        self.color_instructions['cursor_color'] = Color(*self.cursor_color)
        self.cursor = Line(
            points=[self.grid_x, self.grid_y, self.grid_x, self.grid_top],
            dash_length=10,
            dash_offset=5,
            width=self.cursor_width
        )

    #  ================================= # 
    #                Line
    #  ================================= #   
    def draw_line(self, name, points, color=None, width=2, placement='left'):

        if color is None:
            color = self.get_random_color()

        self.line_instructions[name] = {'color': None, 'line': None, 'ellipse': []}
        y_range = self.y_left_range if placement == 'left' else self.y_right_range
        pixel_points = []
        data = []

        with self.canvas:
            if self.focus_key is None:
                set_color = color
            else:
                if self.focus_key == name:
                    set_color = color
                else:
                    set_color = self.to_grayscale(color)

            self.line_instructions[name]['color'] = Color(*set_color)
            self.line_instructions[name]['base_color'] = color
            self.line_instructions[name]['grayscale'] = self.to_grayscale(color)

            for x_val, y_val in points:

                cap_x_val = max(self.x_range[0], min(x_val, self.x_range[1]))
                cap_y_val = max(y_range[0], min(y_val, y_range[1]))

                norm_x = (cap_x_val - self.x_range[0]) / (self.x_range[1] - self.x_range[0])
                norm_y = (cap_y_val - y_range[0]) / (y_range[1] - y_range[0])

                px = self.grid_x + norm_x * self.grid_width
                py = self.grid_y + norm_y * self.grid_height
                pixel_points.extend([px, py])

                dot_radius = self.dot_radius
                ellipse = Ellipse(pos=(px - dot_radius, py - dot_radius), size=(dot_radius * 2, dot_radius * 2))
                self.line_instructions[name]['ellipse'].append(ellipse)

                data.append({'data': (x_val, y_val), 'pos': (px, py)})

            self.line_instructions[name]['line'] = SmoothLine(points=pixel_points, width=width)
            self.dot_info[name] = data

    def undraw_line(self, name):
        if name in self.line_instructions:
            instructions = self.line_instructions[name]
            if instructions['line'] in self.canvas.children:
                self.canvas.remove(instructions['line'])

            if instructions['color'] in self.canvas.children:
                self.canvas.remove(instructions['color'])

            for ellipse in instructions['ellipse']:
                children = list(self.canvas.children)
                if ellipse in children:
                    self.canvas.remove(ellipse)

            del self.dot_info[name]
            del self.line_instructions[name]

    def clear_lines(self):
        names = list(self.line_instructions.keys())
        for name in names:
            self.undraw_line(name)

    def focus(self, name):
        for key, value in self.line_instructions.items():

            if key == name:
                self.bring_on_top(key)
                color_instructions = value['color']
                color_instructions.rgba = value['base_color']

                self.focus_key = key
                continue
            
            color_instructions = value['color']
            color_instructions.rgba = value['grayscale']

    def unfocus(self):
        for key, value in self.line_instructions.items():
            color_instructions = value['color']
            color_instructions.rgba = value['base_color']

        self.focus_key = None

    def bring_on_top(self, name):
        if name in self.line_instructions:
            instructions = self.line_instructions[name]

            if instructions['color'] in self.canvas.children:
                self.canvas.remove(instructions['color'])
                self.canvas.add(instructions['color'])

            if instructions['line'] in self.canvas.children:
                self.canvas.remove(instructions['line'])
                self.canvas.add(instructions['line'])

            for ellipse in instructions['ellipse']:
                if ellipse in self.canvas.children:
                    self.canvas.remove(ellipse)
                    self.canvas.add(ellipse)

    #  ================================= # 
    #          Cursor Movement
    #  ================================= #   
    def move_marker_right(self):
        self.marker.move_right()

    def move_marker_left(self):
        self.marker.move_left()

    #  ================================= # 
    #               Events
    #  ================================= #   
    def on_marker_x(self, instance, value):
        self.cursor.points= [value, self.grid_y, value, self.grid_top]

    def on_cursor_items(self, value):
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            x, y = self.to_local(*touch.pos)
            for series in self.dot_info.values():
                for point in series:
                    px, py = point['pos']
                    if (
                        px - self.touch_tolerance <= x <= px + self.touch_tolerance and
                        py - self.touch_tolerance <= y <= py + self.touch_tolerance
                    ):
                        self.tooltip.text = f"X: {point['data'][0]}, Y: {point['data'][1]}"
                        self.tooltip.top = self.grid_top
                        self.tooltip.right = self.grid_right
                        self.tooltip.open()
                        return True

        self.tooltip.dismiss()
        return super().on_touch_down(touch)

    #  ================================= # 
    #             Color Events
    #  ================================= #
    def on_cursor_color(self, instance, value):

        if 'cursor_color' in self.color_instructions:
            self.color_instructions['cursor_color'].rgba = value

    def on_grid_background_color(self, instance, value):

        if 'grid_background' in self.color_instructions:
            self.color_instructions['grid_background'].rgba = value

    def on_grid_color(self, instance, value):

        if 'grid_color' in self.color_instructions:
            self.color_instructions['grid_color'].rgba = value

    def on_x_axis_color(self, instance, value):

        if 'x_axis_color' in self.color_instructions:
            self.color_instructions['x_axis_color'].rgba = value

    def on_y_axis_color(self, instance, value):

        if 'y_axis_color' in self.color_instructions:
            self.color_instructions['y_axis_color'].rgba = value

    def on_x_ticks_color(self, instance, value):
        if 'x_ticks_color' in self.color_instructions:
            self.color_instructions['x_ticks_color'].rgba = value

    def on_y_ticks_color(self, instance, value):
        if 'y_ticks_color' in self.color_instructions:
            self.color_instructions['y_ticks_color'].rgba = value

    #  ================================= # 
    #            Color Utils
    #  ================================= #
    def to_grayscale(self, color):
        r, g, b, a = color
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        return [gray, gray, gray, 0.25]
    
    def get_random_color(self, alpha=1.0):
        return [random.random() for _ in range(3)] + [alpha]