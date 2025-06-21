import os

class FileLoader:
    def __init__(self):
        # Set the path to the music directory
        self.music_files = []
        self.music_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../assets/music")
        )
        
        
    def load_music(self):
        if os.path.exists(self.music_dir):

            self.music_files = [f for f in os.listdir(self.music_dir) if f.endswith(('.mp3', '.wav', '.ogg'))] #important
            for i in range(len(self.music_files)):
                self.music_files[i] = os.path.join(self.music_dir, self.music_files[i])
            
            
            return self.music_files
        else:
            print("Music directory does not exist.")
            return []

