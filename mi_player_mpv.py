import tkinter as tk
from visor_player import VisorPlayer
from fmc import Controles
# from threading import Thread


class MiPlayerMPV(tk.Frame):
    def __init__(self, parent, volumen=50, **kwargs):
        super(MiPlayerMPV, self).__init__(parent, **kwargs)
        
        self.vplayer = VisorPlayer(self)
        self.vplayer.pack(fill='both', expand=1)
        self.vplayer.fmb.destroy()
        self.cn = Controles(self, bg="#1A1A1A")
        self.cn.pack(fill='x')

        self.valores_iniciales(vol=volumen)
        self.cn.ws_vol.bind("<ButtonRelease-1>", self.mueve_slide_volumen)
        self.vplayer.player.observe_property('time-pos', self.posicion_actual)
        self.cn.bt_play.config(command=self.vplayer.play_pause)
        self.cn.bt_stop.config(command=self.stop)

    def valores_iniciales(self, vol):
        self.vplayer.ajusta_volumen(vol)
        self.cn.volumen_asigna_valor(vol)
        # self.entero = 0

    def mueve_slide_volumen(self, e):
        self.cn.mueve_slider_vol(e)
        vol = self.cn.obten_valor_volumen()
        self.vplayer.ajusta_volumen(vol)

    def reproduce(self, archivo_video, inicio=0):
        self.vplayer.reproduce(archivo_video, inicio)
        # pos = self.vplayer.posicion_obten()
        # self.cn.tiempo_entero = int(pos)
        dr = self.vplayer._obten_duracion()
        self.cn.tiempo_maximo_valor(int(dr))

    def posicion_actual(self, _, segundos_f):
        if segundos_f is not None:
            self.cn.tiempo_asigna_valor(segundos_f)

    def stop(self):
        self.vplayer.stop()
        self.cn.lb_tm.config(text="00:00:00")

    def pause(self):
        self.vplayer.pause()

    def play(self):
        self.vplayer.play()

    def play_pause(self, e=None):
        self.vplayer.play_pause()

    def volumen_inicial(self, vol):
        self.vplayer.volumen_asigna_valor(vol)

    def _teclas_rapidas_mi_player(self, parent):
        d = {
            '<space>':self.play_pause,
            '<Up>':self.sube_volumen,
            '<Down>':self.baja_volumen
        }
        for c, v in d.items():
            parent.bind(c, v)
    
    def key_handler(self, event):
        print(event.char, event.keysym, event.keycode)

    def sube_volumen(self, e=None):
        vol = self.vplayer._obten_volumen_actual()
        nvol = vol+5
        if nvol<201:
            self.vplayer.ajusta_volumen(nvol)
            self.cn.var_vol.set(int(nvol))
            self.cn.lb_vol.config(text=str(int(nvol)))

    def baja_volumen(self, e=None):
        vol = self.vplayer._obten_volumen_actual()
        nvol = vol-5
        if nvol>-1:
            self.vplayer.ajusta_volumen(nvol)
            self.cn.var_vol.set(int(nvol))
            self.cn.lb_vol.config(text=str(int(nvol)))


if __name__=="__main__":
    rz = tk.Tk()
    rz.geometry("400x240")
    mp = MiPlayerMPV(rz, volumen=60)
    vd1 = r"C:\Users\mortadela\Desktop\Europe - The Final Countdown (Official Video).mp4"
    # mp.reproduce(vd1, '00:01:10')
    mp.reproduce(vd1, 64)
    mp._teclas_rapidas_mi_player(rz)
    mp.pack(fill='both', expand=1)
    rz.mainloop()