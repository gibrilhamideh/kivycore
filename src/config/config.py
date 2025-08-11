from kivy.config import Config

def set_config(mode):
    """
    Set the Kivy configuration for the application.
    """
    
    if mode == 'development':
        Config.set('graphics', 'height', 800)
        Config.set('graphics', 'width', 1200)
        Config.set('graphics', 'allow_screensaver', False)
        Config.set('kivy', 'keyboard_mode', 'systemanddock')

    else: # production mode
        pass