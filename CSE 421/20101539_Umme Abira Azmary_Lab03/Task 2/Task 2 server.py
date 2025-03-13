import socket
port = 5050
format = 'utf-8'

hostname = socket.gethostname()

server_ip_add = socket.gethostbyname(hostname)

server_socket_add = (server_ip_add, port)
print(f"Server's socket address is {server_socket_add}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_add)

server.listen()

print("I am listening to requests....")

while True:
    conn, client_sock_addr = server.accept()
    print("Connected to client",client_sock_addr)
    connected = True
    while connected:
        next_msg_length = conn.recv(16).decode(format)
        print("Upcoming message length is",next_msg_length)

        if next_msg_length:
            message = conn.recv(int(next_msg_length)).decode(format)

            if message == "Terminate":
                print("Terminating connection with",client_sock_addr)
                conn.send("Connection terminated as you have wished".encode(format))
                connected = False
            else:
                count = 0
                for x in message:
                    if x in "aeiouAEIOU":
                        count += 1
                        
                if count == 0:
                    conn.send(f"Not enough vowels".encode(format))
                elif count <= 2:
                    conn.send(f"Enough vowels I guess".encode(format))
                else:
                    conn.send(f"Too many vowels".encode(format))

    conn.close()