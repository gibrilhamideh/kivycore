import os

def set_environment(mode):
    """
    Set the environment variables for the application.
    """
    if mode == 'development':
        os.environ['KIVY_METRICS_FONTSCALE'] = '1.0'
    else:  # production mode
        pass
