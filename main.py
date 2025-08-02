import core.factory_registers
import widgets.factory_registers

from kivy.core.window import Window
from kivy.app import App

class Main(App):
    
    def on_start(self):
        Window.size = (1200, 800)


if __name__ == "__main__":
    Main().run() 
