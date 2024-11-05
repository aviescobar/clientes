import socket
import threading
import time
from pynput.mouse import Listener as MouseListener
import keyboard

# Configuración del cliente
server_ip = '172.168.0.161'  # Dirección IP del servidor
port = 12345  # Puerto del servidor

# Variable para el bloqueo
lock_enabled = False

# Función para manejar la conexión con el servidor
def server_listener():
  global lock_enabled
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((server_ip, port))
    print("Conectado al servidor.")

    while True:


