from __future__ import annotations
from typing import Type

import os
from time import perf_counter

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty, ObjectProperty, ColorProperty

from core.effects import Style

from paths import core_path

with open(
    os.path.join(core_path, "bottomsheet", "bottomsheet.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())

class BottomSheetScrim(Style, FloatLayout):
    '''
    A scrim that appears behind the BottomSheet to dim the background when the sheet is open.
    It can be used to indicate that the user should interact with the BottomSheet.
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0.0)

class BottomSheet(Style, BoxLayout):
    
    drag_threshold = NumericProperty(dp(21))
    '''
    The threshold in pixels for touch events to be considered for opening or dismissing the bottom sheet.

    :attr:`drag_threshold` is a :class:`~kivy.properties.NumericProperty`
    '''

    swipe_threshold = NumericProperty(60)
    '''
    The minimum distance in pixels that the user must swipe to trigger the opening or closing of the bottom sheet.

    
    :attr:`swipe_threshold` is a :class:`~kivy.properties.NumericProperty`
    '''

    swipe_max_duration = NumericProperty(0.25)
    '''
    The maximum duration in seconds for a swipe gesture to be considered valid for opening or closing the bottom sheet.

    
    :attr:`swipe_max_duration` is a :class:`~kivy.properties.NumericProperty`
    '''


    velocity_threshold = NumericProperty(700.0)
    '''
    The minimum velocity in pixels per second that the user must swipe to trigger the opening or closing of the bottom sheet.

    :attr:`velocity_threshold` is a :class:`~kivy.properties.NumericProperty`
    '''

    scrim: Type[BottomSheetScrim] = ObjectProperty()
    '''
    The scrim that appears behind the BottomSheet when it is open. It dims the background

    :attr:`scrim` is a :class:`~kivy.properties.ObjectProperty`
    '''

    scrim_color = ColorProperty((0, 0, 0, 0.35))
    '''
    The color of the scrim that appears behind the BottomSheet when it is open.

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    current_scrim_color = ColorProperty((0, 0, 0, 0.35), allownone=True)
    '''
    The current color of the scrim. This is used to update the scrim's color

    :attr:`current_scrim_color` is a :class:`~kivy.properties.ColorProperty`
    '''

    _y_delta_pos = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.scrim = BottomSheetScrim()
        self.scrim.add_widget(self)
        Window.add_widget(self.scrim)

    def open(self):
        Animation.cancel_all(self, 'y')
        Animation(y=0, duration=0.18, t='out_cubic').start(self)

    def dismiss(self):
        Animation.cancel_all(self, 'y')
        Animation(y=self.min_y, duration=0.18, t='out_cubic').start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # start drag only if you already have handle checks etc.
            self._y_delta_pos = touch.y - self.y
            self._swipe_start_y = touch.y
            self._swipe_start_t = perf_counter()
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self and self._y_delta_pos is not None:
            y = touch.y - self._y_delta_pos
            # clamp between open (0) and closed (min_y)
            y = min(0, max(self.min_y, y))
            self.y = y
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)

            dt = max(1e-6, perf_counter() - getattr(self, "_swipe_start_t", perf_counter()))
            dy = touch.y - getattr(self, "_swipe_start_y", touch.y)
            v = dy / dt  # +v = swipe up, -v = swipe down

            is_fast = (abs(dy) >= self.swipe_threshold and dt <= self.swipe_max_duration) or (abs(v) >= self.velocity_threshold)

            if is_fast:
                # Decide by direction
                if v > 0:
                    self.open()     # fast swipe up -> open
                else:
                    self.dismiss()  # fast swipe down -> hide
            else:
                # Not a swipe: snap to nearest (open or closed)
                target_open = 0
                target_closed = self.min_y
                target = target_open if abs(self.y - target_open) < abs(self.y - target_closed) else target_closed
                Animation.cancel_all(self, 'y')
                Animation(y=target, duration=0.18, t='out_cubic').start(self)

            # cleanup
            self._y_delta_pos = None
            return True

        return super().on_touch_up(touch)

    def on_current_scrim_color(self, instance, value):
        """Update the scrim color when the property changes."""
        if self.scrim:
            self.scrim.background_color = value

    def on_y(self, instance, value):
        """Update the scrim's position and alpha to match the bottom sheet's position."""
        # unpack the base scrim color (RGBA)
        r, g, b, base_a = self.scrim_color  

        # normalize y between [min_y, 0] → [0.0, 1.0]
        progress = (value - self.min_y) / (0 - self.min_y)
        progress = max(0.0, min(progress, 1.0))  # clamp

        # interpolate alpha
        a = base_a * progress

        # store the updated color
        self.current_scrim_color = (r, g, b, a)
            


    @property
    def min_y(self):
        """The minimum y position of the bottom sheet, which is the closed position."""
        return self.drag_threshold - self.height