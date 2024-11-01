import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 12345
BUFFER_SIZE = 1024
PASSWORD = "adamcarlen"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server berjalan di {SERVER_IP}:{SERVER_PORT}")

connected_clients = {}

while True:
    try:
        
        message, client_address = server_socket.recvfrom(BUFFER_SIZE)

        
        if client_address not in connected_clients:
            
            if message.decode() == PASSWORD:
                server_socket.sendto("Password diterima. Masukkan username:".encode(), client_address)
                
                username, _ = server_socket.recvfrom(BUFFER_SIZE)
                username = username.decode()

                
                if username in connected_clients.values():
                    server_socket.sendto("Username sudah digunakan!".encode(), client_address)
                else:
                    connected_clients[client_address] = username
                    server_socket.sendto("Anda terhubung.".encode(), client_address)
                    print(f"{username} ({client_address}) terhubung ke chatroom.")
            else:
                server_socket.sendto("Password salah!".encode(), client_address)
                continue

        else:
            username = connected_clients[client_address]
            print(f"Pesan dari {username} ({client_address}): {message.decode()}")
            for addr in connected_clients:
                if addr != client_address:
                    try:
                        server_socket.sendto(f"{username}: {message.decode()}".encode(), addr)
                    except Exception as e:
                        print(f"Error mengirim pesan ke {addr}: {e}")
                else:
                    server_socket.sendto(f"you: {message.decode()}".encode(), addr)

    except KeyboardInterrupt:
        print("\nServer dihentikan.")
        break
    except Exception as e:
        print(f"Error: {e}")

server_socket.close()
