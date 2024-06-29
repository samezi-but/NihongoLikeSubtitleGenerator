
import openai
import time
import tkinter as tk
import json
import random

import vision,display,subtitles

running = True
display_thread = None
capture_thread = None

def load_api_key(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        print(f"Error: API key file '{file_path}' not found.")
        return None

def recognize_screen_content(x, y, width, height):
    return vision.recognize_screen_content_detail(x, y, width, height)

def periodic_capture(root, api_key):
    print("Recognizing screen content...")
    screen_text = recognize_screen_content(root.winfo_x(), root.winfo_y(), root.winfo_width(), root.winfo_height())
    return_subtitles = subtitles.generate_subtitles(screen_text, api_key)
    if return_subtitles == None:
        print("Error: Failed to generate subtitles.")
        root.after(1000, periodic_capture, root, api_key) 
        return
    display.display_subtitles(return_subtitles, root)
    root.after(15000, periodic_capture, root, api_key) 


def main():
    api_key = load_api_key('apikey.txt')
    if not api_key:
        raise ValueError("API key is missing. Please provide a valid API key in 'apikey.txt'.")
    root = display.setup_display()
    root.after(0, periodic_capture, root, api_key)
    root.mainloop()

if __name__ == "__main__":
    main()



