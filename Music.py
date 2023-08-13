import os
import pygame
from tkinter import *
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        self.playlist = []
        self.current_track = 0
        
        self.load_button = Button(root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=20)
        
        self.play_button = Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)
        
        self.pause_button = Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)
        
        self.stop_button = Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)
        
    def load_music(self):
        music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
        if music_file:
            pygame.mixer.init()
            pygame.mixer.music.load(music_file)
            self.playlist.append(music_file)
            print("Music loaded:", os.path.basename(music_file))
            
    def play_music(self):
        if self.playlist:
            pygame.mixer.music.play()
            print("Playing:", os.path.basename(self.playlist[self.current_track]))
            
    def pause_music(self):
        pygame.mixer.music.pause()
        print("Paused")
        
    def stop_music(self):
        pygame.mixer.music.stop()
        print("Stopped")
        
if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()