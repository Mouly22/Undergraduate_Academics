import socket
port = 5050
buffer = 16
format = 'utf-8'

hostname = socket.gethostname()

server_ip_add = socket.gethostbyname(hostname)
client_ip_add = socket.gethostbyname(hostname)
server_socket_add = (server_ip_add, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_socket_add)

def sending_encoded_message(msg):
    message = msg.encode(format)
    msg_len = len(message)
    send_len = str(msg_len).encode(format)
    send_len += b" "*(buffer - len(send_len))

    client.send(send_len)
    client.send(message)

    sent_from_server = client.recv(2024).decode(format)
    print("Sent from server:",sent_from_server)

while True:
    inp = input("Enter the amount(s) of working hour(s): ")
    sending_encoded_message(inp)
    if inp == 0:
        break
