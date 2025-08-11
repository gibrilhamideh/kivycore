"""
Register GabTech widgets to use without import.
"""

from kivy.factory import Factory

def set_factory():
    register = Factory.register

    # ------------------------------------------------------------------------- Core UI Components
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
    # Selection
    # ==================================================== #
    register("CoreSelection", module="core.selection.selection")

    # ==================================================== #
    # Charts
    # ==================================================== #
    register("CoreLineChart", module="core.charts.linechart.linechart")



    # ------------------------------------------------------------------------- Theme UI Components
    # ==================================================== #
    # Card
    # ==================================================== #
    register("Card", module="theme.components.card.card")

    # ==================================================== #
    # Button
    # ==================================================== #
    register("ElevatedButton", module="theme.components.button.button")
    register("IconButton", module="theme.components.button.button")
    register("FloatingButton", module="theme.components.button.button")

    # ==================================================== #
    # LineChart
    # ==================================================== #
    register("LineChart", module="theme.components.charts.linechart")