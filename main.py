import struct
import socket
ip = "112.137.129.129"
port = 27002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

s.send(struct.pack('<ii8s', 0, 8, "21020412".encode()))

def powMod(a, n, m):
    if n <= 0: return 1
    res = powMod(a, n // 2, m) % m
    if n % 2 == 1: return ((res * res) % m * (a % m)) % m
    return (res * res) % m
while True:
    packet = s.recv(2048)
    print('next')
    if len(packet) < 8 : continue
    pk_type, pk_len = struct.unpack('<ii', packet[:8])
    print(pk_type, pk_len)
    if pk_type == 0:
        s.send(struct.pack('<ii8s', 0, 8, "21020412".encode()))
    elif pk_type == 1:
        len_int = int((pk_len - 8) / 4)
        format = '<' + str(len_int) + 'i';
        data_list = list(struct.unpack(format, packet[8:pk_len]))
        n, m, x = data_list[:3]
        ans = 0
        # tmp = 0
        # for i in range(3, 5):
        #     tmp += ((data_list[i]%m) * ((x ** (i - 3)) % m))%m
        #     tmp %= m
        #     print(m);
        print(f'm = {m}')
        print(f'x ={x}')
        # print('2 so dau: ', data_list[3], data_list[4], tmp)
        
        for i in range(3, len(data_list)):
            ans += ((data_list[i]%m) * powMod(x, i - 3, m)) % m
            ans %= m
        print(ans)
        # print(format);
        # print(ans)
        s.send(struct.pack('<iii', 2, 4, ans))
    elif pk_type == 3:
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(struct.pack('<ii8s', 0, 8, "21020412".encode()))
    elif pk_type == 4:
        print(packet[8:8+pk_len].decode())
        break
