import socket
import threading

HOST = 'localhost'
PORT = 13120

ip = input(str("IP [{}]: ".format(HOST)))
if ip != "":
    HOST = ip.strip()
port = input(str("PORT [{}]: ".format(PORT)))
if port != "":
    PORT = int(port)

# Función para enviar mensajes al servidor
def send_message(s: socket.socket):
    while True:
        message = input("> ")
        if message.lower() == '!D':
            print("Cerrando conexión.")
            s.close()  # Cerrar el socket
            break
        # Enviar el mensaje al servidor
        s.sendall(message.encode())

# Función para recibir mensajes del servidor
def receive_message(s: socket.socket):
    while True:
        data = s.recv(1024)
        if not data:
            print("Conexión cerrada por el servidor.")
            break
        print(f"{data.decode()}")

# Función para conectar al servidor y manejar la comunicación
def connect_to_server():
    # Crear un socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Conectarse al servidor
        s.connect((HOST, PORT))
        print("Conectado al servidor en {}:{}".format(HOST, PORT))

        # Crear un hilo para enviar mensajes
        send_thread = threading.Thread(target=send_message, args=(s,))
        send_thread.start()

        # Crear un hilo para recibir mensajes
        receive_thread = threading.Thread(target=receive_message, args=(s,))
        receive_thread.start()

        # Esperar que los hilos terminen
        send_thread.join()
        receive_thread.join()

if __name__ == "__main__":
    connect_to_server()
