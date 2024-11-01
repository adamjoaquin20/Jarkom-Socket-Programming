import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

BUFFER_SIZE = 1024
client_socket = None 
connected = False  

def receive_messages():
    global connected
    while connected:
        try:
            message, _ = client_socket.recvfrom(BUFFER_SIZE)
            chat_display.insert(tk.END, f"{message.decode()}\n")
        except OSError:
            break

def send_message():
    global connected
    message = message_entry.get()
    if not connected:
        chat_display.insert(tk.END, "Anda belum terhubung ke server.\n")
        return
    
    if message.lower() == "exit":
        chat_display.insert(tk.END, "Keluar dari chat.\n")
        client_socket.close()
        connected = False
        window.quit()
    else:
        try:
            client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
            message_entry.delete(0, tk.END)
        except OSError as e:
            chat_display.insert(tk.END, f"Error saat mengirim pesan: {str(e)}\n")

def start_socket_communication():
    global connected, password, username
    try:
        
        client_socket.sendto(password.encode(), (SERVER_IP, SERVER_PORT))

        response, _ = client_socket.recvfrom(BUFFER_SIZE)
        response_message = response.decode()
        if response_message != "Password diterima. Masukkan username:":
            chat_display.insert(tk.END, "Gagal masuk ke chatroom.\n")
            client_socket.close()
            connected = False
            return

        
        client_socket.sendto(username.encode(), (SERVER_IP, SERVER_PORT))

        
        response, _ = client_socket.recvfrom(BUFFER_SIZE)
        response_message = response.decode()
        if response_message != "Anda terhubung.":
            chat_display.insert(tk.END, "Gagal masuk ke chatroom.\n")
            client_socket.close()
            connected = False
            return

        
        connected = True
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        chat_display.insert(tk.END, "Terhubung ke chatroom. Ketik 'exit' untuk keluar.\n")

    except Exception as e:
        chat_display.insert(tk.END, f"Error: {str(e)}\n")
        connected = False

def start_chat():
    global SERVER_IP, SERVER_PORT, client_socket, username, password

    
    SERVER_IP = simpledialog.askstring("IP Server", "Masukkan IP server:")
    SERVER_PORT = simpledialog.askinteger("Port Server", "Masukkan port server:")

    
    password = simpledialog.askstring("Password", "Masukkan password untuk chatroom:", show="*")

    
    username = simpledialog.askstring("Username", "Masukkan username:")

    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connected = True
    except OSError as e:
        chat_display.insert(tk.END, f"Gagal membuat socket: {str(e)}\n")
        connected = False
        return

    
    socket_thread = threading.Thread(target=start_socket_communication)
    socket_thread.daemon = True
    socket_thread.start()

window = tk.Tk()
window.title("UDP Chat Client")

chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=20, width=50)
chat_display.pack(padx=10, pady=10)

message_entry = tk.Entry(window, width=40)
message_entry.pack(padx=10, pady=10)

send_button = tk.Button(window, text="Kirim", command=send_message)
send_button.pack(padx=10, pady=10)

window.after(100, start_chat)
window.mainloop()
