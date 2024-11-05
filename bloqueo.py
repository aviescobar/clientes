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
      comando = client_socket.recv(1024).decode()
      if comando == "LOCK":
        lock_enabled = True
        print("Teclado y mouse bloqueados por el servidor.")
      elif comando == "UNLOCK":
        lock_enabled = False
        print("Teclado y mouse desbloqueados por el servidor.")

# Función para bloquear el teclado
def block_keyboard():
  global lock_enabled
  while True:
    if lock_enabled:


