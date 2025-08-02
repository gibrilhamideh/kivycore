from kivy.factory import Factory

register = Factory.register
register("Card", module="widgets.uix.card.card")


register("LineChart", module="widgets.uix.charts.linechart.linechart")