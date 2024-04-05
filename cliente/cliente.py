import socket
import threading

HOST = '127.0.0.1'
PORT_TCP = 65432
PORT_UDP = 65433

def enviar_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.connect((HOST, PORT_TCP))
        while True:
            mensagem = input("Digite sua mensagem (TCP): ")
            tcp_socket.sendall(mensagem.encode())

def enviar_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        while True:
            mensagem = input("Digite sua mensagem (UDP): ")
            udp_socket.sendto(mensagem.encode(), (HOST, PORT_UDP))

threading.Thread(target=enviar_tcp).start()
threading.Thread(target=enviar_udp).start()
