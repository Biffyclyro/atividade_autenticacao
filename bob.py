import socket

with socket.socket() as ss:
    ss.bind(('localhost', 8090))
    
    ss.listen()
    
    conn, addr = ss.accept()
    
    with conn:
        print('{} connectou!'.format(addr))
        arquivo_completo = []
        while data := conn.recv(1024):
            arquivo_completo.append(data)

        # print('recebeu {}'.format(data.decode('UTF-8')))

        with open('saida.txt', 'wb') as f:
            for i in arquivo_completo:
                f.write(i)

        print(arquivo_completo)

