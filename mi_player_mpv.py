import tkinter as tk
from visor_player import VisorPlayer
from fmc import Controles
from threading import Thread


class MiPlayerMPV(tk.Frame):
    def __init__(self, parent, **kwargs):
        super(MiPlayerMPV, self).__init__(parent, **kwargs)
        
        self.vplayer = VisorPlayer(self)
        self.vplayer.pack(fill='both', expand=1)
        self.vplayer.fmb.destroy()
        self.cn = Controles(self, bg="#1A1A1A")
        self.cn.pack(fill='x')

        self.valores_iniciales()
        self.cn.ws_vol.bind("<ButtonRelease-1>", self.mueve_slide_volumen)
        self.vplayer.player.observe_property('time-pos', self.posicion_actual)
        self.cn.bt_play.config(command=self.vplayer.play_pause)
        self.cn.bt_stop.config(command=self.stop)

    def valores_iniciales(self):
        vol = 20
        self.vplayer.ajusta_volumen(vol)
        self.cn.volumen_asigna_valor(vol)
        self.entero = 0

    def mueve_slide_volumen(self, e):
        self.cn.mueve_slider_vol(e)
        vol = self.cn.obten_valor_volumen()
        self.vplayer.ajusta_volumen(vol)

    def reproduce(self, archivo_video, inicio=0):
        self.vplayer.reproduce(archivo_video, inicio)
        # pos = self.vplayer.posicion_obten()
        # self.cn.tiempo_entero = int(pos)

    def posicion_actual(self, _, segundos_f):
        if segundos_f is not None:
            self.cn.tiempo_asigna_valor(segundos_f)

    def stop(self):
        self.vplayer.stop()
        self.cn.lb_tm.config(text="00:00:00")
    

if __name__=="__main__":
    rz = tk.Tk()
    rz.geometry("400x240")
    mp = MiPlayerMPV(rz)
    vd1 = r"D:\PRO\VIDEO\CHAPTERS\MP4Tools_x32\bin\ab\vi\malvado.mp4"
    mp.reproduce(vd1, '00:00:20')
    # mp.reproduce(vd1)
    mp.pack(fill='both', expand=1)
    rz.mainloop()