import os

from kivy.core.window import Window
from kivy.base import Builder
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, SmoothLine
from kivy.properties import ListProperty, NumericProperty, ColorProperty, OptionProperty, BoundedNumericProperty
from kivy.graphics.texture import Texture

class LineSplitTextureWidget(Widget):
    points = ListProperty([
        [0.0, 0.8],
        [0.1, 0.3],
        [0.5, 0.6],
        [0.9, 0.4],
        [1.0, 0.6]
    ])

    spread = NumericProperty(500)  # How far the color glow reaches
    blur = NumericProperty(4)   # How soft the blur fades
    color = ColorProperty([0, 0, 1, 1])  # Single color
    blur_mode = OptionProperty("bottom", options=["center", "bottom"])
    strength = BoundedNumericProperty(0.3, min=0, max=1, errorvalue=0)  # Strength of the glow effect

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture = None
        self.bind(
            size=self._redraw,
            pos=self._redraw,
            points=self._redraw,
            spread=self._redraw,
            blur=self._redraw,
            color=self._redraw,
            blur_mode=self._redraw,
            strength=self._redraw
        )
        Clock.schedule_once(self._redraw)

    def _redraw(self, *args):
        width = int(self.width)
        height = int(self.height)
        self.texture = self.create_texture(width, height)
        self.draw_texture(self.texture, width, height)
        self.display_texture(self.texture, width, height)

    def create_texture(self, width, height):
        tex = Texture.create(size=(width, height), colorfmt='rgba')
        tex.mag_filter = 'nearest'
        tex.min_filter = 'nearest'
        return tex

    def draw_texture(self, tex, width, height):
        buf = bytearray(width * height * 4)
        pixel_points = self.get_pixel_points(width, height)
        r, g, b, a = [int(self.color[i] * 255) for i in range(4)]

        for y in range(height):
            for x in range(width):
                y_line = self.interpolate_line_y(x, pixel_points)
                dy = y_line - y

                # Blur mode logic
                if self.blur_mode == "center":
                    distance = abs(dy)
                    if distance > self.spread:
                        continue
                elif self.blur_mode == "bottom":
                    if dy < 0 or dy > self.spread:
                        continue
                    distance = dy

                fade = (1.0 - (distance / self.spread)) ** (self.blur * 1.5)
                alpha = int(a * fade * self.strength)
                # alpha = max(alpha, 10)

                self.set_pixel(buf, x, y, width, (r, g, b, alpha))

        tex.blit_buffer(bytes(buf), colorfmt='rgba', bufferfmt='ubyte')

    def get_pixel_points(self, width, height):
        return [
            (int(x * width), int(y * height))
            for x, y in self.points
        ]

    def interpolate_line_y(self, x, points):
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            if x1 <= x <= x2:
                return self.get_y_on_line(x, x1, y1, x2, y2)
        if x < points[0][0]:
            return points[0][1]
        return points[-1][1]

    def get_y_on_line(self, x, x1, y1, x2, y2):
        if x2 - x1 == 0:
            return y1
        m = (y2 - y1) / (x2 - x1)
        return y1 + m * (x - x1)

    def set_pixel(self, buf, x, y, width, rgba):
        index = (y * width + x) * 4
        r, g, b, a = rgba
        buf[index + 0] = r
        buf[index + 1] = g
        buf[index + 2] = b
        buf[index + 3] = a

    def to_pixel_coords(self, nx: float, ny: float) -> tuple[float, float]:
        '''
        Convert normalized (0.0 to 1.0) coordinates to actual pixel positions
        based on the widget's current width and height.

        :param nx: Normalized X (0.0 to 1.0)
        :param ny: Normalized Y (0.0 to 1.0)
        :return: (pixel_x, pixel_y)
        '''
        x = nx * self.width
        y = ny * self.height
        return x, y

    def display_texture(self, tex, width, height):
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(texture=tex, size=(width, height), pos=self.pos)

            Color(*self.color)
            SmoothLine(
                points=[self.to_pixel_coords(x, y) for x, y in self.points],
                width=dp(2)
            )


    def on_blur(self, instance, value):
        print(self.blur)

    def on_spread(self, instance, value):
        print(self.spread)

    def on_strength(self, instance, value):
        print(self.strength)


class Line(App):
    pass

if __name__ == "__main__":
    Line().run()