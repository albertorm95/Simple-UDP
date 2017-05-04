import socket

# IP del Socket
UDP_IP = "127.0.0.1"
# Puerto del Socket
UDP_PORT = 1111

condicion = True

def mandarmensaje(UDP_IP, UDP_PORT):
	# Le pedimos al usuario ingresar el mensaje
	MESSAGE = raw_input("Mensaje a mandar: ")
	# AF_INET = IPv4, SOCK_DGRAM = Datagrama
	enchufe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# Mandar mensaje
	enchufe.sendto(MESSAGE, (UDP_IP,UDP_PORT))

while condicion:
	respuesta = raw_input("\nDesea mandar un mensaje? (s/n): ")
	if respuesta == 's':
		mandarmensaje(UDP_IP, UDP_PORT)
		condicion = True
	elif respuesta == 'n':
		condicion = False
	else:
		print "Solo se acepta un /'s/' o /'n/'como respuesta. \n"