#  Simple Audio Player – Python + Kivy

>  This is a **simple and educational music player**, not a full-featured media application.  

---

##  How It Works

This app allows you to play music from your local folder using a custom Kivy-based UI.  
It supports basic playback controls and automatically displays song-specific images if provided.

###  Music Files
Place your `.mp3`, `.wav`, or `.ogg` files in:
assets/music/


###  Cover Images (Optional)
You can display a custom image for each song by placing an image in:
assets/icons/

- The image **must have the same name** as the song (excluding the extension).
- Example:
assets/music/my_song.mp3
assets/icons/my_song.png


- Supported image formats:
`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.webp`, `.svg`, `.ico`, `.heic`, `.tif`, `.raw`

- If no matching image is found, a default image will be used from:
assets/icons/Default.png


---

##  Features

-  Play local audio files
-  Next / Previous song navigation
-  Play, Pause/Resume, and Stop controls
-  Playback progress bar
-  Volume control slider
-  Displays cover image (if available)

---

##  Project Structure
project/
├── main.py # App entry point
├── player.kv # UI layout (Kivy language)
├── main_screen.py # Main screen logic
├── logic/
│ ├── audio_player.py # Core audio control
│ └── file_loader.py # File discovery logic
├── assets/
│ ├── music/ # Put your audio files here
│ └── icons/ # Put your song images here
└── README.md


---

## 🧪 Requirements

- Python 3.8 or later
- [Kivy](https://kivy.org/#download)

Install dependencies:

```bash
pip install kivy

python main.py



