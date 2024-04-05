import socket

HOST = '127.0.0.1'
PORT_TCP = 65432
PORT_UDP = 65433

clientes = set()

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT_TCP))
tcp_socket.listen()

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT_UDP))

print(f"Servidor TCP ouvindo em {HOST}:{PORT_TCP}")
print(f"Servidor UDP ouvindo em {HOST}:{PORT_UDP}")

while True:

    conn_tcp, addr_tcp = tcp_socket.accept()
    print(f"Conexão TCP estabelecida com {addr_tcp}")
    clientes.add(conn_tcp)

    while True:
        data = conn_tcp.recv(1024)
        if not data:
            break
        print(f"Mensagem TCP recebida: {data.decode()}")
        for client in clientes:
            client.sendall(data)

    clientes.remove(conn_tcp)
    conn_tcp.close()

    data, addr_udp = udp_socket.recvfrom(1024)
    print(f"Mensagem UDP recebida de {addr_udp}: {data.decode()}")
    for client in clientes:
        udp_socket.sendto(data, client.getpeername())

