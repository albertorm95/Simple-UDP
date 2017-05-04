import socket

# IP del Socket
UDP_IP = "127.0.0.1"
# Puerto del Socket
UDP_PORT = 1111

timeout = 60

# AF_INET = IPv4, SOCK_DGRAM = Datagrama
enchufe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Enlazamos los dos sockets, el que recibe debe tener el .bind()
enchufe.bind((UDP_IP, UDP_PORT))

while True:
	# buffer de 4096 bytes
	print "\nEn " + str(timeout) + " segundos el servidor cerrara."
	enchufe.settimeout(timeout)
	MESSAGE = enchufe.recv(4096)
	print "Mensaje recivido: ", MESSAGE