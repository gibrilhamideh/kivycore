# ====================================== #
#            Setup Environment
# ====================================== #
mode = 'development' # or 'production', 'development'

from config import set_environment, set_config, set_fonts, set_factory
set_environment(mode)
set_config(mode)
set_fonts()
set_factory()


from theme.components.app import App

class Main(App):
    pass

if __name__ == "__main__":
    Main().run() 
