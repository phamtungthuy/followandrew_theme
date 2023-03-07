import struct
import socket
ip = "112.137.129.129"
port = 27002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

s.send(struct.pack('<ii8s', 0, 8, "21020412".encode()))

while True:
    packet = s.recv(1024)
    if len(packet) < 8 : continue
    pk_type, pk_len = struct.unpack('<ii', packet[:8])
    print(pk_type, pk_len)
    if pk_type == 0:
        s.send(struct.pack('<ii8s', 0, 8, "21020412".encode()))
    elif pk_type == 1:
        len_int = (pk_len - 8) / 4
        format = '<' + str(len_int) + 'i';
        print(format)
        date_list = struct.unpack(format, packet[8:pk_len])
        n, m, x = data_list[:3]
        ans = data_list[3]
        print(n, m, x)
        for i in range(4, len(date_list)):
            print(i)
        break
    elif pk_type == 3:
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(struct.pack('<ii8s', 0, 8, "21020412".encode()))