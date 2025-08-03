from kivy.factory import Factory
register = Factory.register

# ==================================================== #
# Card
# ==================================================== #
register("Card", module="widgets.uix.card.card")

# ==================================================== #
# Button
# ==================================================== #
register("ElevatedButton", module="widgets.uix.button.button")
register("IconButton", module="widgets.uix.button.button")
register("FloatingButton", module="widgets.uix.button.button")

# ==================================================== #
# LineChart
# ==================================================== #
register("LineChart", module="widgets.uix.charts.linechart")