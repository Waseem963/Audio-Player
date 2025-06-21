from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
import os
from logic.file_loader import FileLoader  # Use correct import



class AudioPlayer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_loader = FileLoader()
        self.choose_music = self.file_loader.load_music()
        self.loaded_sounds = []
        self.current_index = 0  # Track the current song index
        for i in range(len(self.choose_music)):
            sound = SoundLoader.load(self.choose_music[i])
            self.loaded_sounds.append(sound)
        self.load_music = self.loaded_sounds[self.current_index] if self.loaded_sounds else None

    def play_music(self):
        if self.load_music and self.load_music.state == "play":
            print("Music is already playing.")
            return
        elif self.load_music:
            print(f"Playing music... {self.choose_music[self.current_index]}")
            self.load_music.play()

    def stop_music(self):
        if self.load_music and self.load_music.state == "play":
            self.load_music.stop()
            print("Music stopped.")
        else:
            print("No music is currently playing.")

    def next_music(self):
        if not self.loaded_sounds:
            print("No music loaded.")
            return
        # Stop current song if playing
        if self.load_music and self.load_music.state == "play":
            self.load_music.stop()
        # Move to next index (wrap around)
        self.current_index = (self.current_index + 1) % len(self.loaded_sounds) # Loop back to the first song 
        self.load_music = self.loaded_sounds[self.current_index]
        print(f"Next song: {self.choose_music[self.current_index]}")
        self.play_music()

    def volume(self, volume):
        if self.load_music and self.load_music.state == "play":
            self.load_music.volume = volume
            print(f"Volume set to {volume}.")
        else:
            print("No music is currently playing.")

    def previous_music(self):
        if not self.loaded_sounds:
            print("No music loaded.")
            return
        # Stop current song if playing
        if self.load_music and self.load_music.state == "play":
            self.load_music.stop()
        # Move to previous index (wrap around)
        self.current_index = (self.current_index - 1) % len(self.loaded_sounds)
        self.load_music = self.loaded_sounds[self.current_index]
        print(f"Previous song: {self.choose_music[self.current_index]}")

        self.play_music()

    