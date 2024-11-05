import socket
import threading
import time
from pynput.mouse import Listener as MouseListener
import keyboard

# Configuración del cliente
server_ip = '172.168.0.161'  # Dirección IP del servidor
port = 12345  # Puerto del servidor


