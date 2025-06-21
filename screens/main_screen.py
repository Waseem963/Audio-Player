from kivy.uix.screenmanager import Screen
from logic.audio_player import AudioPlayer
from kivy.clock import Clock #######################################################
import os

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.audio_player = AudioPlayer()
        self.update_event = None
        self.is_paused = False

    def music_name(self): 
        self.ids.song_label.text = f"Playing music:{os.path.basename(self.audio_player.choose_music[self.audio_player.current_index])}"
        

    def music_image(self):
    # Supported image types
        types = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.heic', '.tif', '.raw')
        song_file = self.audio_player.choose_music[self.audio_player.current_index]
        base_name = os.path.splitext(os.path.basename(song_file))[0]
        img_path = ""
        for ext in types:
            candidate = f"assets/icons/{base_name}{ext}"
            if os.path.exists(candidate):
                img_path = candidate
                break
        
       
        print(f"Image path: {img_path}")
        if img_path:
            self.ids.music_image.source = img_path
            self.ids.music_image.opacity = 1
        else:
            img_path = "assets/icons/Default.png" 
            self.ids.music_image.source = img_path
            self.ids.music_image.opacity = 1

    def restart_pause_button(self):
        self.is_paused = False
        self.ids.pause_Image_button.source = "assets/icons/layout_images/button_images/ButtonPause.png"

    def play_music(self):
        self.ids.play_Image_button.source = "assets/icons/layout_images/button_images/ButtonPlayPressed.png"
        self.audio_player.play_music()
        if self.audio_player.load_music:
            duration = self.audio_player.load_music.length
            self.ids.progress_bar.max = duration if duration else 1
            if self.update_event:
                self.update_event.cancel()
            self.update_event = Clock.schedule_interval(self.update_slider, 0.5)
            self.music_name()
            self.music_image()
            self.restart_pause_button()

    def update_slider(self, dt):
        if self.audio_player.load_music and self.audio_player.load_music.state == "play":
            pos = self.audio_player.load_music.get_pos()
            if pos is not None:
                self.ids.progress_bar.value = pos
        else:
            self.ids.progress_bar.value = 0
            if self.update_event:
                self.update_event.cancel()
                self.update_event = None
    
    def seek_music(self, position):
        if self.audio_player.load_music:
            self.audio_player.load_music.seek(position)

    def pause_music(self):
       # self.ids.pause_Image_button.source = "assets/icons/layout_images/button_images/ButtonResume.png"
### ### ### ###
        sound = self.audio_player.load_music
        if sound:
            if not self.is_paused and sound.state == "play":
                # Simulate pause
                self.paused_pos = sound.get_pos() or 0
                sound.stop()
                self.is_paused = True
                self.ids.pause_Image_button.source = "assets/icons/layout_images/button_images/ButtonResume.png"
                if self.update_event:
                    self.update_event.cancel()
            elif self.is_paused:
                # Resume from paused position
                self.ids.pause_Image_button.source = "assets/icons/layout_images/button_images/ButtonPause.png"
                sound = self.audio_player.load_music
                self.audio_player.load_music = sound
                if sound:
                    sound.seek(self.paused_pos)
                    sound.play()
                    self.is_paused = False
                    if self.update_event:
                        self.update_event.cancel()
                    self.update_event = Clock.schedule_interval(self.update_slider, 0.5)
                    self.music_name()
        
        
    def update_volume(self, volume):
         # Convert slider value (0–100) to 0.0–1.0
        norm_volume = float(volume) / 100
        self.audio_player.volume(norm_volume)

    def stop_music(self):
        self.ids.stop_Image_button.source = "assets/icons/layout_images/button_images/ButtonStopPressed.png"
        # Logic to stop music
        self.audio_player.stop_music()
        self.ids.song_label.text = "Music stopped."
        self.restart_pause_button()

        # Restart slider update event
    def restart_slider(self):
        if self.update_event:
            self.update_event.cancel()
        self.update_event = Clock.schedule_interval(self.update_slider, 0.5)
        if self.audio_player.load_music and self.audio_player.load_music.length:
            self.ids.progress_bar.max = self.audio_player.load_music.length
        else:
            self.ids.progress_bar.max = 1

    def next_music(self):
        self.ids.next_Image_button.source = "assets/icons/layout_images/button_images/ButtonNextPressed.png"
        self.ids.progress_bar.value = 0
        self.audio_player.next_music()
        self.music_name()
        self.music_image() 
        self.restart_slider()
        self.restart_pause_button()


    def previous_music(self):
        self.ids.previous_Image_button.source = "assets/icons/layout_images/button_images/ButtonPreviousPressed.png"
        self.ids.progress_bar.value = 0
        self.audio_player.previous_music()
        self.music_name()
        self.music_image()
        # Restart slider update event
        self.restart_slider()
        self.restart_pause_button()













    

    # def shuffle_music(self):
    #     # Logic to shuffle music
    #     pass
    # def repeat_music(self):
    #     # Logic to repeat music
    #     pass
    # def show_playlist(self):
    #     # Logic to show the playlist
    #     pass
    # def add_to_playlist(self, song):
    #     # Logic to add a song to the playlist
    #     pass
    # def remove_from_playlist(self, song):
    #     # Logic to remove a song from the playlist
    #     pass
    # def show_now_playing(self):
    #     # Logic to show the currently playing song
    #     pass
    # def show_equalizer(self):
    #     # Logic to show the equalizer
    #     pass
    # def show_settings(self):
    #     # Logic to show the settings
    #     pass
    # def show_about(self):
    #     # Logic to show the about information
    #     pass
    # def show_help(self):
    #     # Logic to show the help information
    #     pass
    # def show_search(self):
    #     # Logic to show the search functionality
    #     pass
    # def show_history(self):
    #     # Logic to show the history of played songs
    #     pass
    # def show_favorites(self):
    #     # Logic to show the favorite songs
    #     pass
    # def show_playlists(self):
    #     # Logic to show the playlists
    #     pass
    # def show_genres(self):
    #     # Logic to show the genres
    #     pass
    # def show_artists(self):
    #     # Logic to show the artists
    #     pass
    