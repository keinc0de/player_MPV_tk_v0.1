import tkinter as tk
from tkinter import ttk
from datetime import timedelta


class MiIcono():
    def __init__(self):
        self.icos = {
            'play':"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAABWElEQVR4nI2RsYoaYRRGz/3/QVGYV9HeQqNkExPMcy
            TgCwgKUwYXRQth8TVkkKAGXHwAGxtb7bRwBIuFde5NsdmwbJaQU3/ng/tdeKIC3ACICGYmgOctgiD4GkWRjUYjq9VqS6AB4Jx7Ww
            zD8G6xWNh+v39cr9c2HA6tWq0ugU8vRPcsOhF5uFwunE4nuV6vWq/Xtd/vV3q93rRcLs9V9UZEVERSQBwgzjm8fyo4n88OSBuNhg
            4Gg/fdbndWKpV+mFkFMPf6Ju89qupfiuPx+GOr1VrmcrnbvwQAM0NE8N5jZiRJQpIkqKoEr4NmRiaTSbPZrBwOBx/HMZPJZLbdbr
            8DywAwVSVNU7z3ms/nOR6PfjqdEsfxz81mcwvMnHOoqhCG4d18Prfdbve4Wq2s0+lYoVC4Bz4/zxpF0Z9ZCYLgW7PZtHa7bcVi8R
            748s/H/eYd8OF/gr8AC12q1/kKMz4AAAAASUVORK5CYII=""",
            'stop':"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAiklEQVR4nOWQsRGEMBADV2d7iOiAzJEDaqAnuqA2aq
            AKMsDnjz5708Ar3pVmpFKKL8uiWiu9tNYYhoF93z3mnLWuK8/zdAV3ZxxHtm2zeN8353nytuDuAFzXRZSEmdFa6woAZoYk7JX6Jf
            6T8H0xSiKE8ApLIqVECAFN01TneTZ3R1K3PaXEcRz+Ad8hNYTWzlQkAAAAAElFTkSuQmCC""",
            'stop2':"""iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAc0lEQVR4nJWSMQ6AIAxFXw2ORgdP4v3P4EkcdNYEl
            0KwlhDeAjSf/ykgfBF8YqXeRsx8dlIicKWUoIKo4h1YiiMIcAKbjhJMwgpMJiGZ5kXJre5lwl0KBr+1OjZhVFcxNXdDBA7g4d90f
            ofua+3GujW/xgsQBxcZ1PkCSAAAAABJRU5ErkJggg=="""
        }

    def play(self):
        return tk.PhotoImage(data=self.icos.get('play'))
    
    def stop(self):
        return tk.PhotoImage(data=self.icos.get('stop'))


class Controles(tk.Frame):
    def __init__(self, parent, **kwargs):
        super(Controles, self).__init__(parent, **kwargs)

        self.mic = MiIcono()
        self.ico_stop = self.mic.stop()
        self.ico_play = self.mic.play()
        s_bt = {
            "bg":'gray10',
            "activebackground":"gray40",
            'relief':'flat'
        }
        s_sv = {
            "bg":'#F06E53',
            "activebackground":"#F08053",
            "sliderlength":12,
            'sliderrelief':'flat',
            'troughcolor':'#404040', # fondo
            'highlightthickness': 0,
            'border':0
        }
        s_st = {
            "bg":'#71A338',
            "activebackground":"#83A35F",
            "sliderlength":12,
            'sliderrelief':'flat',
            'troughcolor':'#404040', # fondo
            'highlightthickness': 0,
            'border':0,
            'from_':0,
            'to':100
        }
        s_lb = {
            "font":('Arial', 8, 'bold'),
            "fg":"white",
            "bg":"gray10",
            "justify":"center"
        }
        self.st = ttk.Style()
        self.st.theme_use('clam')
        bt = '#122224'
        self.st.configure(
            'sbt.Horizontal.TProgressbar',
            background="#2C8E7D",
            troughcolor=bt,
            bordercolor=bt,
            lightcolor=bt,
            darkcolor=bt
        )
        self.bt_stop = tk.Button(self, width=16, image=self.ico_stop, **s_bt)
        self.bt_stop.pack(side='left')
        self.var_vol = tk.IntVar()
        self.ws_vol = tk.Scale(
            self, orient='horizontal',
            variable=self.var_vol,
            showvalue=0, length=50, **s_sv
        )
        self.ws_vol.pack(side='left')
        # self.ws_vol.bind("<ButtonRelease-1>", self.mueve_slider_vol)
        self.lb_vol = tk.Label(self, text='100', width=3, **s_lb)
        self.lb_vol.pack(side='left')
        self.var_tm = tk.DoubleVar()
        # self.ws_tiempo = tk.Scale(
        #     self, orient='horizontal',
        #     variable=self.var_tm,
        #     showvalue=0, **s_st,
        #     state='disabled'
        # )
        # self.ws_tiempo.pack(side='left', fill='x', expand=1)

        self.wb_tiempo = ttk.Progressbar(
            self, variable=self.var_tm,
            mode='determinate',
            style='sbt.Horizontal.TProgressbar'
        )
        self.wb_tiempo.pack(side='left', fill='x', expand=1,pady=0,ipady=0)

        self.lb_tm = tk.Label(self, text='00:00:00', width=7, **s_lb)
        self.lb_tm.pack(side='left')
        self.bt_play = tk.Button(self, width=16, image=self.ico_play, **s_bt)
        self.bt_play.pack(side='left')

        # VARIALbles
        self.tiempo_entero = 0

    def mueve_slider_vol(self, e):
        n = self.var_vol.get()
        self.lb_vol.config(text=str(n))

    def obten_valor_volumen(self):
        return self.var_vol.get()
    
    def volumen_asigna_valor(self, valor):
        self.var_vol.set(valor)
        self.lb_vol.config(text=str(valor))

    def tiempo_maximo_valor(self, valor):
        self.wb_tiempo.config(maximum=valor)

    def tiempo_asigna_valor(self, segundos_float):
        if segundos_float is not None:
            segundos = round(segundos_float, 2)
            if int(segundos)!=self.tiempo_entero:
                _, decimales = str(segundos).split('.')
                if int(decimales)==0:
                    try:
                        # print("segundos::::: ", segundos)
                        self.var_tm.set(segundos)
                        t = f"0{timedelta(seconds=segundos)}"
                        self.lb_tm.config(text=t)
                        self.tiempo_entero = int(segundos_float) # para mover por segundos
                    except Exception as ex:
                        pass
                        # print("ex::: ", ex, _, decimales)
                        # print(segundos_float, segundos)

                # self.st.configure(
                #     'sbt.Horizontal.TProgressbar',
                #     text=t
                # )


if __name__=="__main__":
    rz = tk.Tk()
    rz.geometry('280x16')
    cn = Controles(rz, bg='gray10')
    cn.pack(fill='x')
    rz.mainloop()
    
