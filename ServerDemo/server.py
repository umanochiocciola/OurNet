import socket
import sys
import pickle as pk
import server_index as si

banca = si.main
try: deferr = si.error_response
except: deferr = "Error: no item found."

def ricevi_comandi(conn):
    richiesta = conn.recv(4096)
    stuff = richiesta.decode().split('_')
    print(stuff)
    data = banca.get(richiesta.decode().split('/')[0], deferr)
    
    while isinstance(data, dict):
        if not('/' in richiesta.decode()): richiesta = richiesta.decode() + '/index'; richiesta = richiesta.encode()
        data = data.get(richiesta.decode().split('/')[1], deferr)
    
    conn.sendall(data.encode())


def sub_server(indirizzo, backlog=1):
    print("Kane Stream server started")
    while 1:
        try:
            s = socket.socket()                    
            s.bind(indirizzo)                     
            s.listen(backlog)                     
            print('Ready to accept a new connection')
        except socket.error as errore:
            print(f"Something went wrong\n{errore}")
            print(f"Server reboot aptempt")
            sub_server(indirizzo, backlog=1)
        conn, indirizzo_client = s.accept()
        print(f"Connection: {indirizzo_client}")
        ricevi_comandi(conn)

sub_server(("", int(sys.argv[1])))
