import tkinter as tk
import random

def setup_display():
    root = tk.Tk()
    root.geometry("1400x1200")
    root.title("Comment Window")

    # 透明にする色を設定
    root.wm_attributes("-transparentcolor", "black")
    root.attributes("-topmost", True)
    frame = tk.Frame(root, background="black")
    frame.pack(expand=True, fill=tk.BOTH)
    root.frame = frame
    root.update_idletasks()  # これでウィンドウサイズが確定します
    return root

def display_subtitles(subtitles, root):
    forcount = 0
    labels = []
    yplus = 64
    xplus = 40
    screen_width = root.winfo_screenwidth()  # 画面幅を取得
    print(f"Screen width: {screen_width}")

    for subtitle in subtitles:
        if isinstance(subtitle, dict):
            comment = subtitle['comment']
        else:
            comment = subtitle
        label = tk.Label(root.frame, text=comment, bg="black", fg="white", font=("Arial", 48))
        label.update_idletasks()  # ラベルのサイズを確定
        label_width = label.winfo_width()  # ラベルの幅を取得
        random_x_start = random.randint(-100, 2000)
        label.place(x=screen_width + label_width + (xplus * forcount) + random_x_start, y=yplus * forcount)  # 初期位置を画面右端の外側に設定
        labels.append(label)
        forcount += 1

    def move_subtitles():
        speed = 40  # 字幕の移動速度
        yplus = 64
        def update_position():
            forcount2 = 0
            for label in labels:
                x_pos = label.winfo_x() - speed 
                label.place(x=x_pos, y=yplus * forcount2)
                forcount2 += 1
                if forcount2 == 10:
                    forcount2 = 0
            root.after(10, update_position)

        update_position()
    move_subtitles()
    for label in labels:
        if label.winfo_x() < -root.winfo_width():
            labels.remove(label)
            label.destroy()