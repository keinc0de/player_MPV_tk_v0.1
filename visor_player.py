import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import mpv


class VisorPlayer(tk.Frame):
    def __init__(self, parent, **kwargs):
        super(VisorPlayer, self).__init__(parent, **kwargs)
        self.fma = tk.Frame(self, bg='#150D13')
        self.fma.pack(side='top', fill="both", expand=1)
        self.fmb = tk.Frame(self, bg='green', height=2)
        self.fmb.pack(side='bottom', fill="x")
        self.rowconfigure(1, minsize=1)

        self.player = mpv.MPV(
            wid=str(int(self.fma.winfo_id())), input_default_bindings=True,
            input_vo_keyboard=True, osc=True
        )
        # self.player = mpv.MPV(player_operation_mode='pseudo-gui',
        #          script_opts='osc-layout=box,osc-seekbarstyle=bar,osc-deadzonesize=0,osc-minmousemove=3',
        #          input_default_bindings=True,
        #          input_vo_keyboard=True,
        #          osc=True)


        s = ttk.Style()
        s.theme_use('clam')
        bv = '#2C2220'
        s.configure('sbv.Horizontal.TProgressbar',
            background="#E17756",
            troughcolor=bv,
            bordercolor=bv,
            lightcolor=bv,
            darkcolor=bv
        )
        bt = '#122224'
        s.configure(
            'sbt.Horizontal.TProgressbar',
            background="#2C8E7D",
            troughcolor=bt,
            bordercolor=bt,
            lightcolor=bt,
            darkcolor=bt
        )
        # BARRA DE PROGRESO -VOL
        self.var_vol = tk.IntVar()
        self.bp_vol = ttk.Progressbar(
            self.fmb,
            # length=100,
            # mode='determinate',
            variable=self.var_vol,
            maximum=100, value=75,
            style='sbv.Horizontal.TProgressbar'
        )
        self.bp_vol.pack(side='left', ipady=0, pady=0)
        # BARRA DE PROGRESO -VOL
        # BARRA DE PROGRESO -TIEMPO
        self.var_tiempo = tk.IntVar()
        self.bp_tiempo = ttk.Progressbar(
            self.fmb,
            mode='determinate',
            variable=self.var_tiempo,
            # maximum=100, value=75,
            style='sbt.Horizontal.TProgressbar'
        )
        self.bp_tiempo.pack(side='right', fill='x', expand=1, ipady=0, pady=0)
        self.var_vol.set(32)
        self.var_tiempo.set(65)
        # BARRA DE PROGRESO -TIEMPO

    def reproduce(self, archivo_video, tiempo=0):
        video = Path(archivo_video).as_posix()
        # self.player.play(video)
        self.player.loadfile(video, start=tiempo)
        self.player.wait_until_playing()

    def ajusta_volumen(self, vol):
        self.player._set_property('volume', vol)

    def obten_player(self):
        return self.player
    
    def duracion_obten(self):
        d = round(self.player._get_property('duration'), 2)
        return 0 if d is None else d
    
    def pause(self):
        self.player._set_property('pause', True)

    def play(self):
        self.player._set_property('pause', False)

    def stop(self):
        self.player.stop()

    def play_pause(self):
        std = self.player._get_property('core-idle')
        self.play() if std else self.pause()
        


if __name__=="__main__":
    rz = tk.Tk()
    rz.geometry("320x210")
    vp = VisorPlayer(rz)
    vp.pack(fill='both', expand=1)

    rz.mainloop()