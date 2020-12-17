import socket
import sys
import tkinter as tk
from tkinter import ttk

win = tk.Tk()

def invia_comandi(s, comando):
    global ffre
    s.send(comando.encode())
    data = s.recv(4096)
    print("Killing connection...")
    s.close()
    ffre = data.decode()

def conn_sub_server(indirizzo_server, richie):
    try:
        s = socket.socket()
        s.connect(indirizzo_server)
        print(f"Succesfully connected to { indirizzo_server }")
        invia_comandi(s, richie)
    except socket.error as errore:
        print(f"Connection error \n{errore}")

def ope():
    global but, c, b, serie, episodio
    global ib, port
    global req
    global out
    
    ib, port = serie.get(), episodio.get()
    
    tit = tk.Label(text='Our Net')
    req = tk.Entry()
    sei = tk.Button(text='Search', command=lolf)
    out = tk.Label(text='-   -   -')
    
    conn_sub_server((ib, int(port)), 'index')
    out.configure(text=ffre)
    
    but.destroy()
    c.destroy()
    b.destroy()
    serie.destroy()
    episodio.destroy()
    
    tit.pack()
    req.pack()
    sei.pack()
    out.pack()
    
    win.mainloop()
    
def lolf():
    global req
    global out
    global ib, port
    conn_sub_server((ib, int(port)), req.get())
    out.configure(text=f'result:\n' + ffre)

ib = art = port = req = out = ferb = art = canc = fin = None
ffre = '---'

b = tk.Label(text='ip')
serie = tk.Entry()
c = tk.Label(text='port')
episodio = tk.Entry()
but = tk.Button(text='Connect', command=ope)

b.pack()
serie.pack()
c.pack()
episodio.pack()
but.pack()

win.mainloop()