from __future__ import annotations
from typing import Type

from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.event import EventDispatcher



from core.charts.tooltip import Tooltip

class ChartLine(EventDispatcher):
    line_info: list[dict] = ListProperty()
    '''
    `line_info`

    :attr:`line_info` is a :class:`~kivy.properties.ListProperty`
    '''

    dot_radius = NumericProperty(4)
    '''
    `dot_radius`

    :attr:`dot_radius` is a :class:`~kivy.properties.NumericProperty`
    '''

    touch_tolerance = NumericProperty(20)
    '''
    `touch_tolerance`

    :attr:`touch_tolerance` is a :class:`~kivy.properties.NumericProperty`
    '''

    tooltip: Type[Tooltip] = ObjectProperty(None)
    '''
    `tooltip`

    :attr:`tooltip` is a :class:`~kivy.properties.ObjectProperty`
    '''


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            for series in self.line_info:
                for point in series:
                    if 'pos' in point:
                        px, py = point['pos']
                        if (
                            px - self.touch_tolerance <= touch.x <= px + self.touch_tolerance and
                            py - self.touch_tolerance <= touch.y <= py + self.touch_tolerance
                        ):
                            self.open_tooltip(**point)
                            return True

        self.dismiss_tooltip()
        return super().on_touch_down(touch)

    def open_tooltip(self, **kwargs):
        """
        This method can be overridden to handle selection of a point on the graph.
        It receives the x and y values of the selected point.
        """

        self.tooltip.open(
            x=kwargs['pos'][0],
            y=kwargs['pos'][1],
            text=f"X: {kwargs['data'][0]}, Y: {kwargs['data'][1]}"
        )

    def dismiss_tooltip(self):
        """
        Dismisses the tooltip if it is open.
        """
        self.tooltip.dismiss()
            