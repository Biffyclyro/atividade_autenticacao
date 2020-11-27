from tkinter import filedialog as fc
import socket

f = fc.askopenfile(mode = 'rb')

s = socket.socket()
s.connect(('localhost', 8090))

s.send(f.read())

s.close()









