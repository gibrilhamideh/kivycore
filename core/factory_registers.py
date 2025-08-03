from kivy.factory import Factory
register = Factory.register

# ==================================================== #
# Effects
# ==================================================== #
register("Style", module="core.effects.style")

# ==================================================== #
# Button
# ==================================================== #
register("CoreButton", module="core.button.button")

# ==================================================== #
# Switch
# ==================================================== #
register("CoreSwitch", module="core.switch.switch")

# ==================================================== #
# Charts
# ==================================================== #
register("CoreLineChart", module="core.charts.linechart.linechart")