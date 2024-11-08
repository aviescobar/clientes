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
      keyboard.block_key('esc')  # Se bloquean todas las teclas excepto "esc" en este ejemplo
    time.sleep(0.1)

# Función para bloquear el mouse
def block_mouse(x, y, button, pressed):
  return not lock_enabled  # Si está bloqueado, ignora el evento de mouse

# Iniciar los hilos
listener_thread = threading.Thread(target=server_listener)
listener_thread.start()

keyboard_thread = threading.Thread(target=block_keyboard)
keyboard_thread.start()

with MouseListener(on_click=block_mouse) as listener:
      listener.join()
