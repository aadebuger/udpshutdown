import socket
import sys
def shutdowncomputer(ip):
#UDP_IP = "192.168.3.116"
    UDP_PORT = 10001
    MESSAGE = chr(0x1)

    print "UDP target IP:", ip
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (ip, UDP_PORT))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "python ip"
        sys.exit(1)
    shutdowncomputer(sys.argv[1])