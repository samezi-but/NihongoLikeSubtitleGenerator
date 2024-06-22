
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
            {"role": "user", "content": "This is recognized screen result. Make live commentary in Japanese. make 30 messages and differents comment, export for strict JSON style. Style use this [{'"'comment'"': '"'XXXX'"'},{'"'comment'"': '"'YYYY'"'}]You are limited answer JSON format text only. Don't say application name. :"+screen_text}
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
    root.geometry("1400x1400")
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
    yplus = 64
    xplus = 40
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
        random_x_start = random.randint(-100, 300)
        label.place(x=screen_width + label_width + (xplus*forcount) + random_x_start, y=yplus*forcount)  # 初期位置を画面右端の外側に設定
        labels.append(label)
        forcount += 1

    def move_subtitles():
        speed = 15    # 字幕の移動速度
        yplus = 64
        def update_position():
            forcount = 0
            for label in labels:
                x_pos = label.winfo_x() - speed 
                label.place(x=x_pos, y=yplus*forcount)
                forcount += 1
                if forcount == 10:
                    forcount = 0
            root.after(10, update_position)  # 10msごとに移動

        update_position()

    move_subtitles()

def periodic_capture(root, api_key):
    print("Recognizing screen content...")
    screen_text = recognize_screen_content()
    subtitles = generate_subtitles(screen_text, api_key)
    print("Subtitles: ", subtitles)
    display_subtitles(subtitles, root)
    root.after(5000, periodic_capture, root, api_key)  # 5000ミリ秒後にもう一度呼び出す

def main():
    api_key = load_api_key('apikey.txt')
    if not api_key:
        raise ValueError("API key is missing. Please provide a valid API key in 'apikey.txt'.")
    root = setup_display()
    root.after(0, periodic_capture, root, api_key)  # 最初の呼び出し
    root.mainloop()

if __name__ == "__main__":
    main()


