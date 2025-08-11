
from typing import Literal

from kivy.event import EventDispatcher
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.properties import (
    ColorProperty,
    OptionProperty,
    NumericProperty,
    VariableListProperty,
    AliasProperty,
    ListProperty
)

class Theme(EventDispatcher):

    # ==================================================================================================================
    #   Theme Color Properties
    # ==================================================================================================================

    mode: Literal['Dark', 'Light'] = OptionProperty(None, options=['Dark', 'Light'])

    primaryColor = ColorProperty()
    primaryDark = get_color_from_hex('1b1e33')
    primaryLight = get_color_from_hex('1b1e33')

    onPrimaryColor = ColorProperty()
    onPrimaryDark = get_color_from_hex('ffffff')
    onPrimaryLight = get_color_from_hex('ffffff')

    secondaryColor = ColorProperty()
    secondaryDark = get_color_from_hex('7aa3cc')
    secondaryLight = get_color_from_hex('7aa3cc')

    onSecondaryColor = get_color_from_hex('ffffff')
    onSecondaryDark = get_color_from_hex('ffffff')
    onSecondaryLight = get_color_from_hex('ffffff')

    secondaryBackgroundColor = ColorProperty()
    secondaryBackgroundDark = get_color_from_hex('7aa3cc')[:3] + [0.15]
    secondaryBackgroundLight = get_color_from_hex('7aa3cc')[:3] + [0.15]

    accentColor = ColorProperty()
    accentDark = get_color_from_hex('ccad00')
    accentLight = get_color_from_hex('ccad00')

    onAccentColor = ColorProperty()
    onAccentDark = get_color_from_hex('ffffff')
    onAccentLight = get_color_from_hex('ffffff')

    infoColor = ColorProperty()
    infoDark = get_color_from_hex('2196F3')
    infoLight = get_color_from_hex('2196F3')

    onInfoColor = ColorProperty()
    onInfoDark = get_color_from_hex('ffffff')
    onInfoLight = get_color_from_hex('ffffff')

    infoBackgroundColor = ColorProperty()
    infoBackgroundDark = get_color_from_hex('2196F3')[:3] + [0.15]
    infoBackgroundLight = get_color_from_hex('2196F3')[:3] + [0.15]

    errorColor = ColorProperty()
    errorDark = get_color_from_hex('B00020')
    errorLight = get_color_from_hex('B00020')

    onErrorColor = ColorProperty()
    onErrorDark = get_color_from_hex('ffffff')
    onErrorLight = get_color_from_hex('ffffff')

    errorBackgroundColor = ColorProperty()
    errorBackgroundDark = get_color_from_hex('B00020')[:3] + [0.1]
    errorBackgroundLight = get_color_from_hex('B00020')[:3] + [0.1]

    warningColor = ColorProperty()
    warningDark = get_color_from_hex('F57C00')
    warningLight = get_color_from_hex('F57C00')

    onWarningColor = ColorProperty()
    onWarningDark = get_color_from_hex('ffffff')
    onWarningLight = get_color_from_hex('ffffff')

    warningBackgroundColor = ColorProperty()
    warningBackgroundDark = get_color_from_hex('F57C00')[:3] + [0.1]
    warningBackgroundLight = get_color_from_hex('F57C00')[:3] + [0.1]

    successColor = ColorProperty()
    successDark = get_color_from_hex('00C853')
    successLight = get_color_from_hex('00C853')

    onSuccessColor = ColorProperty()
    onSuccessDark = get_color_from_hex('ffffff')
    onSuccessLight = get_color_from_hex('ffffff')

    successBackgroundColor = ColorProperty()
    successBackgroundDark = get_color_from_hex('00C853')[:3] + [0.1]
    successBackgroundLight = get_color_from_hex('00C853')[:3] + [0.1]

    backgroundColor = ColorProperty()
    backgroundDark = get_color_from_hex('000000')
    backgroundLight = get_color_from_hex('FFFFFF')

    onBackgroundColor = ColorProperty()
    onBackgroundDark = get_color_from_hex('ffffff')
    onBackgroundLight = get_color_from_hex('000000')

    surfaceColor = ColorProperty()
    surfaceDark = get_color_from_hex('0d0d0d')
    surfaceLight = get_color_from_hex('f2f2f2')

    onSurfaceColor = ColorProperty()
    onSurfaceDark = get_color_from_hex('d9d9d9')
    onSurfaceLight = get_color_from_hex('262626')

    shadowColor = ColorProperty()
    shadowDark = [0, 0, 0, 0.65]
    shadowLight =[0, 0, 0, 0.65]

    scrimColor = ColorProperty()
    scrimDark = [0, 0, 0, 0.35]
    scrimLight = [0, 0, 0, 0.35]

    onScrimColor = ColorProperty()
    onScrimDark = get_color_from_hex('ffffff')
    onScrimLight = get_color_from_hex('ffffff')

    focusColor = ColorProperty()
    focusDark = get_color_from_hex('ccc28f')[:3] + [0.35]
    focusLight = get_color_from_hex('ccc28f')[:3] + [0.35]

    rippleColor = ColorProperty()
    rippleDark = get_color_from_hex('ADB1A9')
    rippleLight = get_color_from_hex('ADB1A9')

    neutralLightColor = ColorProperty(get_color_from_hex('cccccc'))
    neutralMediumColor = ColorProperty(get_color_from_hex('999999'))
    neutralDarkColor = ColorProperty(get_color_from_hex('666666'))


    def get_neutral_light_color(self):
        return self.neutralLightColor

    def get_neutral_medium_color(self):
        return self.neutralMediumColor

    def get_neutral_dark_color(self):
        return self.neutralDarkColor
    
    dividerColor = AliasProperty(get_neutral_light_color, None, bind=['neutralLightColor'])

    borderColor = ColorProperty()
    borderDarkColor = AliasProperty(get_neutral_dark_color, None, bind=['neutralDarkColor'])
    borderLightColor = AliasProperty(get_neutral_light_color, None, bind=['neutralLightColor'])

    hintColor = AliasProperty(get_neutral_dark_color, None, bind=['neutralDarkColor'])

    disabledColor = AliasProperty(get_neutral_dark_color, None, bind=['neutralDarkColor'])
    onDisabledColor = AliasProperty(get_neutral_light_color, None, bind=['neutralLightColor'])
    disabledBackgroundColor = ColorProperty(get_color_from_hex('BDBDBD')[:3] + [0.1])
    

    @property
    def dark_colors(self):
        return {
            'primaryColor': self.primaryDark,
            'onPrimaryColor': self.onPrimaryDark,
            'secondaryColor': self.secondaryDark,
            'onSecondaryColor': self.onSecondaryDark,
            'errorColor': self.errorDark,
            'onErrorColor': self.onErrorDark,
            'warningColor': self.warningDark,
            'onWarningColor': self.onWarningDark,
            'successColor': self.successDark,
            'onSuccessColor': self.onSuccessDark,
            'surfaceColor': self.surfaceDark,
            'onSurfaceColor': self.onSurfaceDark,
            'backgroundColor': self.backgroundDark,
            'onBackgroundColor': self.onBackgroundDark,
            'shadowColor': self.shadowDark,
            'scrimColor': self.scrimDark,
            'onScrimColor': self.onScrimDark,
            'focusColor': self.focusDark,
            'rippleColor': self.rippleDark,
            'accentColor': self.accentDark,
            'onAccentColor': self.onAccentDark,
            'errorBackgroundColor': self.errorBackgroundDark,
            'warningBackgroundColor': self.warningBackgroundDark,
            'successBackgroundColor': self.successBackgroundDark,
            'secondaryBackgroundColor': self.secondaryBackgroundDark,
            'infoColor': self.infoDark,
            'onInfoColor': self.onInfoDark,
            'infoBackgroundColor': self.infoBackgroundDark,
            'borderColor': self.borderDarkColor

        }
    
    @property
    def light_colors(self):
        return {
            'primaryColor': self.primaryLight,
            'onPrimaryColor': self.onPrimaryLight,
            'secondaryColor': self.secondaryLight,
            'onSecondaryColor': self.onSecondaryLight,
            'errorColor': self.errorLight,
            'onErrorColor': self.onErrorLight,
            'warningColor': self.warningLight,
            'onWarningColor': self.onWarningLight,
            'successColor': self.successLight,
            'onSuccessColor': self.onSuccessLight,
            'surfaceColor': self.surfaceLight,
            'onSurfaceColor': self.onSurfaceLight,
            'backgroundColor': self.backgroundLight,
            'onBackgroundColor': self.onBackgroundLight,
            'shadowColor': self.shadowLight,
            'scrimColor': self.scrimLight,
            'onScrimColor': self.onScrimLight,
            'focusColor': self.focusLight,
            'rippleColor': self.rippleLight,
            'accentColor': self.accentLight,
            'onAccentColor': self.onAccentLight,
            'errorBackgroundColor': self.errorBackgroundLight,
            'warningBackgroundColor': self.warningBackgroundLight,
            'successBackgroundColor': self.successBackgroundLight,
            'secondaryBackgroundColor': self.secondaryBackgroundLight,
            'infoColor': self.infoLight,
            'onInfoColor': self.onInfoLight,
            'infoBackgroundColor': self.infoBackgroundLight,
            'borderColor': self.borderLightColor
        }

    def toggle(self):
        """
        Toggle between dark and light themes.
        """
        if self.mode == 'Dark':
            self.mode = 'Light'
        else:
            self.mode = 'Dark'

    def on_mode(self, instance, value):
        
        if value == 'Dark':
            colors = self.dark_colors
        elif value == 'Light':
            colors = self.light_colors

        anim = None
        for key, color in colors.items():
            a = Animation(**{key: color}, d=0.3,  t='out_expo') # in_out_quad, out_expo
            anim = a if anim is None else anim & a
            
        anim.start(self)

    # ==================================================================================================================
    #   Theme Size Properties
    # ==================================================================================================================
    itemWidth: float = NumericProperty(dp(200))
    itemHeight: float = NumericProperty(dp(30))
    itemRadius: float = NumericProperty(dp(5))
    itemBorderWidth: float = NumericProperty(dp(1))

    labelPadding: list = VariableListProperty([dp(0), dp(6)])

    floatingButtonRadius: float = NumericProperty(dp(6))
    floatingButtonWidth: float = NumericProperty(dp(56))
    floatingButtonHeight: float = NumericProperty(dp(56))
    floatingButtonFontSize: float = NumericProperty(dp(28))

    itemDividerWidth    = NumericProperty(dp(1))
    sectionDividerWidth = NumericProperty(dp(2))
    tabBarDividerWidth  = NumericProperty(dp(2))

    # ======================== #
    #          Fields
    # ======================== #
    fieldRadius: float = VariableListProperty([dp(5), dp(5), dp(0), dp(0)])
    fieldPadding: list[int] = VariableListProperty([dp(6), dp(6), dp(30), dp(6)])

    # ======================== #
    #        VKeyboard
    # ======================== #
    vkeyboardFontSize: float = NumericProperty(dp(21))

    # ======================== #
    #          Frame
    # ======================== #
    framePadding: list[int] = VariableListProperty([dp(200), dp(25)])
    frameElevation: float = NumericProperty(dp(3))
    frameShadowOffset: list[int] = ListProperty([0, -dp(5)])
    frameShadowSoftness: float = NumericProperty(dp(5))
    frameRadius: float = VariableListProperty([dp(10), dp(10), 0, 0])

    # ======================== #
    #          Table
    # ======================== #
    tableSizeHint: list[float] = ListProperty([0.8, 0.8])
    tableElevation: float = NumericProperty(dp(3))
    tableShadowOffset: list[int] = ListProperty([0, -dp(5)])
    tableShadowSoftness: float = NumericProperty(dp(5))
    tableRadius: float = VariableListProperty([dp(10), dp(10), 0, 0])


    # ======================== #
    #      History Table
    # ======================== #
    historyHeaderFontSize: float = NumericProperty(dp(18))
    historyHeaderHeight: float = NumericProperty(dp(30))

    historyItemFontSize: float = NumericProperty(dp(14))
    historyItemHeight: float = NumericProperty(dp(30))

    historyTablePadding: list[int] = VariableListProperty([dp(5), dp(0)])
