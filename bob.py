import socket

with socket.socket() as ss:
    ss.bind(('localhost', 8090))
    
    ss.listen()
    
    conn, addr = ss.accept()
    
    with conn:
        print('{} connectou!'.format(addr))
        data = conn.recv()    
        print(len(data))
        print('recebeu {}'.format(data.decode('UTF-8')))

