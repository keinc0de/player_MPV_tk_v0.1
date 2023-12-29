# widget tkinter video player
widget para tkinter de video usando MPV embebido (incrustado), tiene opciones basicas, para usar como widget de vista previa de video para otros programas

![](files_md/cap-wg.jpg)


realizado con python 3.12 y tkinter

**Librerias**
* [python-mpv	0.3.0](https://github.com/jaseg/python-mpv)

La libreria **mpv.py** no es nesesario instalarla se puede copiar directamente en el proyecto, igualmente el dll `mpv-2.dll`

```python
rz = tk.Tk()
rz.geometry("400x240")
mp = MiPlayerMPV(rz)
mp.reproduce(r"mi_video.mp4")
mp.pack(fill='both', expand=1)
rz.mainloop()
```
