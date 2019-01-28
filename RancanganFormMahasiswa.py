#! /usr/bin/env python

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import RancanganFormMahasiswa_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    RancanganFormMahasiswa_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    RancanganFormMahasiswa_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("315x215+439+161")
        top.title("Mahasiswa: Nimas Fauziah")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#f0f0f0f0f0f0")

        self.LabelNPM = tk.Label(top)
        self.LabelNPM.place(relx=0.032, rely=0.047, height=21, width=33)
        self.LabelNPM.configure(background="#d9d9d9")
        self.LabelNPM.configure(disabledforeground="#a3a3a3")
        self.LabelNPM.configure(foreground="#000000")
        self.LabelNPM.configure(text='''NPM''')

        self.LabelNama = tk.Label(top)
        self.LabelNama.place(relx=0.032, rely=0.14, height=21, width=38)
        self.LabelNama.configure(background="#d9d9d9")
        self.LabelNama.configure(disabledforeground="#a3a3a3")
        self.LabelNama.configure(foreground="#000000")
        self.LabelNama.configure(text='''Nama''')

        self.LabelJurusan = tk.Label(top)
        self.LabelJurusan.place(relx=0.032, rely=0.279, height=21, width=46)
        self.LabelJurusan.configure(background="#d9d9d9")
        self.LabelJurusan.configure(disabledforeground="#a3a3a3")
        self.LabelJurusan.configure(foreground="#000000")
        self.LabelJurusan.configure(text='''Jurusan''')

        self.LabelKelas = tk.Label(top)
        self.LabelKelas.place(relx=0.032, rely=0.395, height=21, width=34)
        self.LabelKelas.configure(background="#d9d9d9")
        self.LabelKelas.configure(disabledforeground="#a3a3a3")
        self.LabelKelas.configure(foreground="#000000")
        self.LabelKelas.configure(text='''Kelas''')

        self.LabelAlamat = tk.Label(top)
        self.LabelAlamat.place(relx=0.032, rely=0.512, height=21, width=44)
        self.LabelAlamat.configure(background="#d9d9d9")
        self.LabelAlamat.configure(disabledforeground="#a3a3a3")
        self.LabelAlamat.configure(foreground="#000000")
        self.LabelAlamat.configure(text='''Alamat''')

        self.LabelNomorHP = tk.Label(top)
        self.LabelNomorHP.place(relx=0.016, rely=0.628, height=21, width=74)
        self.LabelNomorHP.configure(background="#d9d9d9")
        self.LabelNomorHP.configure(disabledforeground="#a3a3a3")
        self.LabelNomorHP.configure(foreground="#000000")
        self.LabelNomorHP.configure(text='''Nomor_HP''')
        self.LabelNomorHP.configure(width=74)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.LabelTitikDua1 = tk.Label(top)
        self.LabelTitikDua1.place(relx=0.286, rely=0.047, height=21, width=9)
        self.LabelTitikDua1.configure(background="#d9d9d9")
        self.LabelTitikDua1.configure(disabledforeground="#a3a3a3")
        self.LabelTitikDua1.configure(foreground="#000000")
        self.LabelTitikDua1.configure(text=''':''')

        self.LabelTitikDua3 = tk.Label(top)
        self.LabelTitikDua3.place(relx=0.286, rely=0.279, height=21, width=9)
        self.LabelTitikDua3.configure(activebackground="#f9f9f9")
        self.LabelTitikDua3.configure(activeforeground="black")
        self.LabelTitikDua3.configure(background="#d9d9d9")
        self.LabelTitikDua3.configure(disabledforeground="#a3a3a3")
        self.LabelTitikDua3.configure(foreground="#000000")
        self.LabelTitikDua3.configure(highlightbackground="#d9d9d9")
        self.LabelTitikDua3.configure(highlightcolor="black")
        self.LabelTitikDua3.configure(text=''':''')

        self.LabelTitikDua2 = tk.Label(top)
        self.LabelTitikDua2.place(relx=0.286, rely=0.14, height=21, width=9)
        self.LabelTitikDua2.configure(activebackground="#f9f9f9")
        self.LabelTitikDua2.configure(activeforeground="black")
        self.LabelTitikDua2.configure(background="#d9d9d9")
        self.LabelTitikDua2.configure(disabledforeground="#a3a3a3")
        self.LabelTitikDua2.configure(foreground="#000000")
        self.LabelTitikDua2.configure(highlightbackground="#d9d9d9")
        self.LabelTitikDua2.configure(highlightcolor="black")
        self.LabelTitikDua2.configure(text=''':''')

        self.LabelTitikDua4 = tk.Label(top)
        self.LabelTitikDua4.place(relx=0.286, rely=0.395, height=21, width=9)
        self.LabelTitikDua4.configure(background="#d9d9d9")
        self.LabelTitikDua4.configure(disabledforeground="#a3a3a3")
        self.LabelTitikDua4.configure(foreground="#000000")
        self.LabelTitikDua4.configure(text=''':''')

        self.LabelTitikDua5 = tk.Label(top)
        self.LabelTitikDua5.place(relx=0.286, rely=0.512, height=21, width=9)
        self.LabelTitikDua5.configure(background="#d9d9d9")
        self.LabelTitikDua5.configure(disabledforeground="#a3a3a3")
        self.LabelTitikDua5.configure(foreground="#000000")
        self.LabelTitikDua5.configure(text=''':''')

        self.LabelTitikDua6 = tk.Label(top)
        self.LabelTitikDua6.place(relx=0.286, rely=0.628, height=21, width=9)
        self.LabelTitikDua6.configure(background="#d9d9d9")
        self.LabelTitikDua6.configure(disabledforeground="#a3a3a3")
        self.LabelTitikDua6.configure(foreground="#000000")
        self.LabelTitikDua6.configure(text=''':''')

        self.TextBoxNPM = tk.Entry(top)
        self.TextBoxNPM.place(relx=0.317, rely=0.047,height=20, relwidth=0.648)
        self.TextBoxNPM.configure(background="white")
        self.TextBoxNPM.configure(disabledforeground="#a3a3a3")
        self.TextBoxNPM.configure(font="TkFixedFont")
        self.TextBoxNPM.configure(foreground="#000000")
        self.TextBoxNPM.configure(insertbackground="black")
        self.TextBoxNPM.configure(width=204)

        self.TextBoxNAMA = tk.Entry(top)
        self.TextBoxNAMA.place(relx=0.317, rely=0.163, height=20, relwidth=0.648)

        self.TextBoxNAMA.configure(background="white")
        self.TextBoxNAMA.configure(disabledforeground="#a3a3a3")
        self.TextBoxNAMA.configure(font="TkFixedFont")
        self.TextBoxNAMA.configure(foreground="#000000")
        self.TextBoxNAMA.configure(highlightbackground="#d9d9d9")
        self.TextBoxNAMA.configure(highlightcolor="black")
        self.TextBoxNAMA.configure(insertbackground="black")
        self.TextBoxNAMA.configure(selectbackground="#c4c4c4")
        self.TextBoxNAMA.configure(selectforeground="black")
        self.TextBoxNAMA.configure(width=204)

        self.TextBoxJURUSAN = tk.Entry(top)
        self.TextBoxJURUSAN.place(relx=0.317, rely=0.279, height=20
                , relwidth=0.648)
        self.TextBoxJURUSAN.configure(background="white")
        self.TextBoxJURUSAN.configure(disabledforeground="#a3a3a3")
        self.TextBoxJURUSAN.configure(font="TkFixedFont")
        self.TextBoxJURUSAN.configure(foreground="#000000")
        self.TextBoxJURUSAN.configure(insertbackground="black")
        self.TextBoxJURUSAN.configure(width=204)

        self.TextBoxKELAS = tk.Entry(top)
        self.TextBoxKELAS.place(relx=0.317, rely=0.395, height=20
                , relwidth=0.648)
        self.TextBoxKELAS.configure(background="white")
        self.TextBoxKELAS.configure(disabledforeground="#a3a3a3")
        self.TextBoxKELAS.configure(font="TkFixedFont")
        self.TextBoxKELAS.configure(foreground="#000000")
        self.TextBoxKELAS.configure(insertbackground="black")
        self.TextBoxKELAS.configure(width=204)

        self.TextBoxALAMAT = tk.Entry(top)
        self.TextBoxALAMAT.place(relx=0.317, rely=0.512, height=20
                , relwidth=0.648)
        self.TextBoxALAMAT.configure(background="white")
        self.TextBoxALAMAT.configure(disabledforeground="#a3a3a3")
        self.TextBoxALAMAT.configure(font="TkFixedFont")
        self.TextBoxALAMAT.configure(foreground="#000000")
        self.TextBoxALAMAT.configure(insertbackground="black")
        self.TextBoxALAMAT.configure(width=204)

        self.TextBoxNOMOR_HP = tk.Entry(top)
        self.TextBoxNOMOR_HP.place(relx=0.317, rely=0.628, height=20
                , relwidth=0.648)
        self.TextBoxNOMOR_HP.configure(background="white")
        self.TextBoxNOMOR_HP.configure(disabledforeground="#a3a3a3")
        self.TextBoxNOMOR_HP.configure(font="TkFixedFont")
        self.TextBoxNOMOR_HP.configure(foreground="#000000")
        self.TextBoxNOMOR_HP.configure(insertbackground="black")
        self.TextBoxNOMOR_HP.configure(width=204)

        self.ButtonSIMPAN = tk.Button(top)
        self.ButtonSIMPAN.place(relx=0.651, rely=0.767, height=34, width=97)
        self.ButtonSIMPAN.configure(activebackground="#ececec")
        self.ButtonSIMPAN.configure(activeforeground="#000000")
        self.ButtonSIMPAN.configure(background="#d9d9d9")
        self.ButtonSIMPAN.configure(disabledforeground="#a3a3a3")
        self.ButtonSIMPAN.configure(foreground="#000000")
        self.ButtonSIMPAN.configure(highlightbackground="#d9d9d9")
        self.ButtonSIMPAN.configure(highlightcolor="black")
        self.ButtonSIMPAN.configure(pady="0")
        self.ButtonSIMPAN.configure(text='''SIMPAN''')
        self.ButtonSIMPAN.configure(width=97)

if __name__ == '__main__':
    vp_start_gui()





