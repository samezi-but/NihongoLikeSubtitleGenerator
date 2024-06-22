
import openai
import time
import tkinter as tk
import json
import random

from vision import recognize_screen_content_detail

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


def recognize_screen_content():
    return recognize_screen_content_detail()

def generate_subtitles(screen_text, api_key):
    client = openai.OpenAI(api_key=api_key)
    
    parameters = {
        'engine': 'gpt-4o',
        'max_tokens': 1024,
        'temperature': 0.5,
        'stop': None
    }
    response = client.chat.completions.create(
        model=parameters['engine'],
        messages=[
            {"role": "system", "content": "Make feel casual middle volume and short shout text. Generate subtitles for the screen content in Japanese language. It is one line of text. Be like niconico douga. be like brainless."},
            {"role": "user", "content": "This is recognized screen result. Make live commentary in Japanese. make 20 messages and differents comment, export for strict JSON style. You are limited answer JSON format text only. :"+screen_text}
        ],
        max_tokens=parameters['max_tokens'],
        temperature=parameters['temperature'],
        stop=parameters['stop']
    )
    print(response.choices[0].message.content.strip())
    try:
        subtitles = json.loads(response.choices[0].message.content.strip("```").strip("json"))
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return generate_subtitles(screen_text, api_key)
    return subtitles

def setup_display():
    root = tk.Tk()
    root.geometry("1024x800")
    root.title("Transparent Window")

    # 透明にする色を設定
    root.wm_attributes("-transparentcolor", "black")
    root.attributes("-topmost", True)
    return root

def display_subtitles(subtitles, root):
    forcount = 0
    frame = tk.Frame(root, background="black")
    frame.pack(expand=True, fill=tk.BOTH)
    labels = []
    yplus = 32
    root.update_idletasks()  # これでウィンドウサイズが確定します
    screen_width = root.winfo_screenwidth()  # 画面幅を取得
    print(f"Screen width: {screen_width}")

    for subtitle in subtitles:
        if isinstance(subtitle, dict):
            comment = subtitle['comment']
        else:
            comment = subtitle
        label = tk.Label(frame, text=comment, bg="black", fg="white", font=("Arial", 48))
        label.update_idletasks()  # ラベルのサイズを確定
        label_width = label.winfo_width()  # ラベルの幅を取得
        random_x_start = random.randint(screen_width, screen_width + 100)
        label.place(x=screen_width + label_width + (xplus*forcount) + random_x_start, y=yplus*forcount)  # 初期位置を画面右端の外側に設定
        labels.append(label)
        forcount += 1
    def move_subtitles():
        speed = 5    # 字幕の移動速度
        yplus = 32
        def update_position():
            forcount = 0  # Define forcount within the scope of the function
            for label in labels:
                x_pos = label.winfo_x() - speed 
                label.place(x=x_pos, y=yplus*forcount)
                forcount += 1
            root.after(10, update_position)  # 10msごとに移動

        update_position()

    move_subtitles()

def main():
    global running, capture_thread
    api_key = load_api_key('apikey.txt')
    if not api_key:
        raise ValueError("API key is missing. Please provide a valid API key in 'apikey.txt'.")
    root = setup_display()
    while running:
        print("Recognizing screen content...")
        screen_text = recognize_screen_content()
        subtitles = generate_subtitles(screen_text, api_key)
        print("Subtitles: ", subtitles)
        display_subtitles(subtitles,root)
        root.mainloop()
        time.sleep(5)   # Adjust sleep time as needed
if __name__ == "__main__":
    main()

