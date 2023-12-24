import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
print(os.path.dirname(__file__) + os.pathsep + os.environ["PATH"])
import tkinter as tk
from pathlib import Path
import mpv
 
root=tk.Tk()
root.geometry("500x280")
player = mpv.MPV(wid=str(int(root.winfo_id())), input_default_bindings=True,input_vo_keyboard=True,osc=True)
video_f = Path(r"U:\Bodega\pro\desarrollo\agrega chapters\v0.1\life m.mp4").as_posix()
player.play(video_f)

print(root.winfo_id())
tk.mainloop()