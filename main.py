from kivy.config import Config              ##################
Config.set('graphics', 'width', '900')   
Config.set('graphics', 'height', '750')  
Config.set('graphics', 'resizable', 0)  # Disable window resizing
Config.set('graphics', 'show_cursor', 1)  # Show cursor

from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from screens.main_screen import MainScreen

class MusicPlayerApp(App):
    def build(self):

        Builder.load_file("player.kv")
        sm = ScreenManager()
        sm.add_widget(MainScreen(name ="MainScreen"))
        return sm
    
if __name__ == "__main__":
    MusicPlayerApp().run()
    # This is where the app starts running. The main loop will be initiated here.
    # The app will load the KV file and create the screen manager with the main screen.